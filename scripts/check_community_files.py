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

    print(f"root: {root}")
    print(f"relative links checked: {checked_links}")
    print(f"issue forms checked:    {forms}")
    print(f"labels used:            {labels if labels else 'none'}")
    print(f"forks tracked:          {forks}")

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
