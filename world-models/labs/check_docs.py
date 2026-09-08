"""Check repository-relative Markdown links and accidental private content."""
import re
from pathlib import Path

root = Path(__file__).resolve().parents[2]
failures = []
links = 0
for path in root.rglob('*.md'):
    if '.git' in path.parts:
        continue
    text = path.read_text(encoding='utf-8')
    if '\ufffd' in text:
        failures.append(f'{path.relative_to(root)}: replacement character')
    if re.search(r'(?:[A-Za-z]:[\\/](?:Users|Windows)|gh[pousr]_[A-Za-z0-9]{20,}|-----BEGIN .*PRIVATE KEY-----)', text):
        failures.append(f'{path.relative_to(root)}: possible private path or credential')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        links += 1
        local = target.split('#')[0]
        if local and not (path.parent / local).is_file():
            failures.append(f'{path.relative_to(root)}: missing {local}')
if failures:
    raise SystemExit('\n'.join(failures))
print(f'PASS: {links} relative document links; basic encoding/private-content checks.')
