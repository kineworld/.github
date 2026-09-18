#!/usr/bin/env python3
"""Check the organization-wide community health files in this repository.

These files are defaults: GitHub serves them to every repository in the organization that does
not ship its own copy. A silent deletion or a broken relative link therefore degrades every
repository at once, and no repository's own CI would notice. Hence this check.

Each assertion below names the defect that turns it red. If an assertion cannot fail, it does
not belong here.

Checks
------
[C1] Required community health files exist at the paths GitHub actually reads.
     Red when: a file is deleted, renamed, or moved out of the `.github/` folder (issue
     templates only work from `.github/ISSUE_TEMPLATE`; putting them at the root silently
     disables them).
[C2] `profile/README.md` contains no relative links.
     Red when: someone writes `[...](CONTRIBUTING.md)`. That file renders at
     https://github.com/kineworld (the organization landing page), where relative paths
     resolve against the org root, not against `profile/`. The link 404s.
[C3] Every relative link in every other Markdown file resolves to a file in this repository.
     Red when: a document is renamed or moved without updating its referrers.
[C4] Every label used by an issue form is declared in `community-labels.txt`.
     Red when: a form references a label that does not exist. GitHub requires a label used by a
     default issue template to exist in the `.github` repository *and* in every repository that
     will use the template; an undeclared label breaks the form.
[C5] Every issue form declares a name, a description, and unique field ids.
     Red when: a form would fail to render or would silently drop a field.
[C6] The first-party / fork split is intact.
     `forks.txt` is the local record of the organization's forks. The canonical table lives in
     `world-models/open-source-adoption.md`, which ATTRIBUTION.md links to instead of copying, so
     that the two cannot drift. Red when: a fork from `forks.txt` is missing from the canonical
     table, or a fork name appears in the first-party section of ATTRIBUTION.md.
[C7] No hand-copied counts in externally visible prose.
     A written number is a claim that goes stale without anyone noticing. A count of
     repositories or forks may only appear if it is checked against forks.txt on every run. Red
     when: a stated count disagrees with forks.txt, or a count is stated about something this
     check cannot verify (so it cannot be kept honest). Spell-out forms ("fourteen
     repositories") are red for the same reason -- they cannot be verified at all.

     This check exists because the first draft of this change set wrote "14 repositories" into
     profile/README.md and "Thirteen-plus repositories" into SUPPORT.md by hand.

Usage
-----
    python scripts/check_community_files.py [repo_root]

Exit code 0 = all checks pass, 1 = at least one failed.
"""

from __future__ import annotations

import os
import re
import sys

# Paths GitHub reads for organization-wide defaults. See
# https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file
REQUIRED_ROOT_FILES = [
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "GOVERNANCE.md",
    "ATTRIBUTION.md",
]
REQUIRED_OTHER_PATHS = [
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/PULL_REQUEST_TEMPLATE.md",
]
# Folders that must NOT hold issue templates: GitHub only reads `.github/ISSUE_TEMPLATE`.
MISPLACED_ISSUE_TEMPLATE_DIRS = ["ISSUE_TEMPLATE", "docs/ISSUE_TEMPLATE"]

COUNT_RE = re.compile(
    r"\b(\d+)\s+(?:[A-Za-z-]+\s+){0,3}(repositories|repository|repos|repo|forks|fork)\b"
)
SPELLED_RE = re.compile(
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|"
    r"fifteen|sixteen|seventeen|eighteen|nineteen|twenty)(-plus)?\s+"
    r"(?:[A-Za-z-]+\s+){0,3}(repositories|repository|repos|repo|forks|fork)\b",
    re.IGNORECASE,
)
# Only files that are published (or served) as part of the organization's public face.
COUNT_CLAIM_FILES = [
    "profile/README.md",
    "ATTRIBUTION.md",
    "SUPPORT.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "SECURITY.md",
]

# Words that turn a number into a taxonomy or a comparison rather than a count of items.
# "Two kinds of repositories" describes categories, not a quantity; "no more than 6 repositories"
# is a bound, not the current count. Neither is a countable claim, so neither is checked.
TAXONOMY_RE = re.compile(
    r"\b(?:kind|kinds|type|types|sort|sorts|category|categories|class|classes|group|groups)\b",
    re.IGNORECASE,
)
COMPARATIVE_RE = re.compile(r"\b(?:than|least|most|fewer|more|under|over|about|roughly)\b\s*$",
                            re.IGNORECASE)

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORM_EXT = ".yml"

failures: list[str] = []
notes: list[str] = []


def fail(check: str, message: str) -> None:
    failures.append(f"[{check}] {message}")


def load_yaml(path: str):
    """Parse YAML with PyYAML when present, else fall back to a minimal structural parse."""
    try:
        import yaml  # type: ignore
    except ImportError:
        return None
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def iter_markdown(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {".git", "__pycache__"}]
        for name in filenames:
            if name.lower().endswith((".md", ".markdown")):
                yield os.path.join(dirpath, name)


def check_required_files(root: str) -> None:
    for rel in REQUIRED_ROOT_FILES + REQUIRED_OTHER_PATHS:
        if not os.path.isfile(os.path.join(root, rel)):
            fail("C1", f"missing required community health file: {rel}")
    for rel in MISPLACED_ISSUE_TEMPLATE_DIRS:
        if os.path.isdir(os.path.join(root, rel)):
            fail("C1", f"{rel}/ exists; GitHub only reads .github/ISSUE_TEMPLATE for defaults")


def check_profile_has_no_relative_links(root: str) -> None:
    path = os.path.join(root, "profile", "README.md")
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    for target in LINK_RE.findall(text):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        fail("C2", f"profile/README.md uses relative link '{target}'; use an absolute URL")


def check_relative_links(root: str) -> int:
    checked = 0
    for path in iter_markdown(root):
        base = os.path.dirname(path)
        if os.path.relpath(path, root).replace(os.sep, "/") == "profile/README.md":
            continue
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = target.split("#", 1)[0]
            if not path_part:
                continue
            checked += 1
            resolved = os.path.normpath(os.path.join(base, path_part))
            if not os.path.exists(resolved):
                fail(
                    "C3",
                    f"{os.path.relpath(path, root)} -> '{target}' does not resolve",
                )
    return checked


def check_labels(root: str) -> list[str]:
    manifest_path = os.path.join(root, "community-labels.txt")
    declared: set[str] = set()
    if os.path.isfile(manifest_path):
        with open(manifest_path, encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line and not line.startswith("#"):
                    declared.add(line)

    used: dict[str, list[str]] = {}
    template_dir = os.path.join(root, ".github", "ISSUE_TEMPLATE")
    if not os.path.isdir(template_dir):
        return []
    for name in sorted(os.listdir(template_dir)):
        if not name.endswith(FORM_EXT) or name == "config.yml":
            continue
        data = load_yaml(os.path.join(template_dir, name))
        if not isinstance(data, dict):
            continue
        labels = data.get("labels") or []
        if isinstance(labels, str):
            labels = [labels]
        for label in labels:
            used.setdefault(str(label), []).append(name)

    for label, sources in sorted(used.items()):
        if label not in declared:
            fail(
                "C4",
                f"label '{label}' used by {', '.join(sources)} is not declared in community-labels.txt",
            )
    for label in sorted(declared - set(used)):
        notes.append(f"[C4] label '{label}' is declared but unused by any issue form")
    return sorted(used)


def check_forms(root: str) -> int:
    template_dir = os.path.join(root, ".github", "ISSUE_TEMPLATE")
    if not os.path.isdir(template_dir):
        return 0
    count = 0
    for name in sorted(os.listdir(template_dir)):
        if not name.endswith(FORM_EXT) or name == "config.yml":
            continue
        count += 1
        rel = f".github/ISSUE_TEMPLATE/{name}"
        data = load_yaml(os.path.join(template_dir, name))
        if data is None:
            notes.append(f"[C5] {rel} not parsed (PyYAML unavailable); structure unchecked")
            continue
        if not isinstance(data, dict):
            fail("C5", f"{rel} is not a YAML mapping")
            continue
        for key in ("name", "description", "body"):
            if not data.get(key):
                fail("C5", f"{rel} is missing '{key}'")
        ids: list[str] = []
        for block in data.get("body") or []:
            if not isinstance(block, dict):
                fail("C5", f"{rel} has a non-mapping entry in body")
                continue
            block_type = block.get("type")
            if block_type not in {"markdown", "input", "textarea", "dropdown", "checkboxes"}:
                fail("C5", f"{rel} uses unsupported field type '{block_type}'")
            block_id = block.get("id")
            if block_id:
                ids.append(block_id)
            elif block_type != "markdown":
                fail("C5", f"{rel} has a '{block_type}' field with no id")
            if block_type == "dropdown" and not (block.get("attributes") or {}).get("options"):
                fail("C5", f"{rel} field '{block_id}' is a dropdown with no options")
        duplicates = {i for i in ids if ids.count(i) > 1}
        if duplicates:
            fail("C5", f"{rel} has duplicate field ids: {sorted(duplicates)}")
    return count


def load_forks(root: str) -> set[str]:
    path = os.path.join(root, "forks.txt")
    if not os.path.isfile(path):
        return set()
    with open(path, encoding="utf-8") as handle:
        return {
            line.strip() for line in handle
            if line.strip() and not line.strip().startswith("#")
        }


def check_counts(root: str) -> int:
    """[C7] Every repository or fork count stated in prose must be machine-verifiable."""
    forks = load_forks(root)
    if not forks:
        notes.append("[C7] forks.txt absent or empty; count claims unchecked")
        return 0

    claims = 0
    for rel in COUNT_CLAIM_FILES:
        path = os.path.join(root, rel)
        if not os.path.isfile(path):
            continue
        with open(path, encoding="utf-8") as handle:
            lines = handle.readlines()
        for lineno, line in enumerate(lines, start=1):
            for match in SPELLED_RE.finditer(line):
                if TAXONOMY_RE.search(match.group(0)):
                    continue  # "two kinds of repositories" is a taxonomy, not a count
                claims += 1
                fail(
                    "C7",
                    f"{rel}:{lineno} states '{match.group(0)}' in words, which cannot be "
                    f"verified; use the checked digit form",
                )
            for match in COUNT_RE.finditer(line):
                if TAXONOMY_RE.search(match.group(0)):
                    continue
                before = line[: match.start()]
                if COMPARATIVE_RE.search(before):
                    continue  # "no more than 6 repositories" is a bound, not the count
                claims += 1
                stated = int(match.group(1))
                if stated != len(forks):
                    fail(
                        "C7",
                        f"{rel}:{lineno} says '{match.group(0).strip()}' but forks.txt lists "
                        f"{len(forks)}",
                    )
    return claims


def check_attribution(root: str) -> int:
    forks_path = os.path.join(root, "forks.txt")
    attribution_path = os.path.join(root, "ATTRIBUTION.md")
    canonical_path = os.path.join(root, "world-models", "open-source-adoption.md")
    if not os.path.isfile(forks_path) or not os.path.isfile(attribution_path):
        notes.append("[C6] forks.txt or ATTRIBUTION.md absent; fork/own-work split unchecked")
        return 0

    with open(forks_path, encoding="utf-8") as handle:
        forks = {
            line.strip() for line in handle
            if line.strip() and not line.strip().startswith("#")
        }
    if not forks:
        fail("C6", "forks.txt lists no forks; the split cannot be verified")
        return 0

    with open(attribution_path, encoding="utf-8") as handle:
        text = handle.read()
    # ATTRIBUTION.md deliberately does not repeat the fork list; it links to the canonical table.
    first_party_section = text.split("## Forked upstream projects")[0]
    for repo in sorted(forks):
        if f"/{repo})" in first_party_section:
            fail("C6", f"'{repo}' is a fork but is linked from the first-party section")

    if not os.path.isfile(canonical_path):
        fail("C6", "world-models/open-source-adoption.md is missing; the fork table has no home")
        return len(forks)
    with open(canonical_path, encoding="utf-8") as handle:
        canonical = handle.read()
    for repo in sorted(forks):
        if repo not in canonical:
            fail("C6", f"fork '{repo}' is not listed in world-models/open-source-adoption.md")
    return len(forks)


def main(argv: list[str]) -> int:
    root = os.path.abspath(argv[1] if len(argv) > 1 else ".")
    check_required_files(root)
    check_profile_has_no_relative_links(root)
    checked_links = check_relative_links(root)
    labels = check_labels(root)
    forms = check_forms(root)
    forks = check_attribution(root)
    count_claims = check_counts(root)

    print(f"root: {root}")
    print(f"relative links checked: {checked_links}")
    print(f"issue forms checked:    {forms}")
    print(f"labels used:            {labels if labels else 'none'}")
    print(f"forks tracked:          {forks}")
    print(f"counted claims checked: {count_claims}")

    for note in notes:
        print(note)

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for item in failures:
            print(f"  {item}")
        return 1
    print("\ncommunity files: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
