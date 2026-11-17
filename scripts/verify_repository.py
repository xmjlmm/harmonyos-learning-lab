"""Verify migration bytes, integration fixes, module references and new guides."""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MODULES = [
    'apps/farm-manager',
    'samples/state-management/basic',
    'samples/state-management/extended',
    'samples/distributed-billing',
    'prototypes/farm-assistant',
]


def active_text(path):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.S)
    return '\n'.join(line for line in text.splitlines()
                     if not line.lstrip().startswith('//'))


def main():
    failures = []
    manifest = json.loads(
        (ROOT/'docs/migration-manifest.json').read_text(encoding='utf-8')
    )
    records = manifest['records']
    origins = set()
    originals = set()
    for row in records:
        key = (row['branch'], row['source'])
        if key in origins:
            failures.append('Duplicate source record: '+str(key))
        origins.add(key)
        path = ROOT/row['destination']
        try:
            path.resolve().relative_to(ROOT.resolve())
        except ValueError:
            failures.append('Out-of-scope path: '+row['destination'])
            continue
        if row['commit'] != manifest['branches'][row['branch']]:
            failures.append('Inconsistent source commit: '+str(key))
        if not path.is_file():
            failures.append('Missing original file: '+row['destination'])
            continue
        data = path.read_bytes()
        blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        if (len(data) != row['size'] or blob != row['git_blob_sha1']
                or hashlib.sha256(data).hexdigest() != row['sha256']):
            failures.append('Changed original bytes: '+row['destination'])
        originals.add(row['destination'])
    if set(row['branch'] for row in records) != set(manifest['branches']):
        failures.append('Source branch coverage mismatch')
    for change in manifest['adjustments']:
        path = ROOT/change['active']
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != change['sha256']:
            failures.append('Unexpected integration change: '+change['active'])
        if change['original'] not in originals:
            failures.append('Missing pre-change copy: '+change['original'])

    imports = 0
    routes = 0
    known = []
    documented_routes = {
        (row['module'], row['file'], row['target']): row['reason']
        for row in json.loads((ROOT/'docs/known-route-issues.json').read_text(encoding='utf-8'))
    }
    for module in MODULES:
        root = ROOT/module
        ets = root/'entry/src/main/ets'
        pages_file = root/'entry/src/main/resources/base/profile/main_pages.json'
        pages = set(json.loads(pages_file.read_text(encoding='utf-8'))['src'])
        for page in pages:
            if not (ets/(page+'.ets')).is_file():
                failures.append('Registered page missing: '+module+'/'+page)
        for path in ets.rglob('*.ets'):
            text = active_text(path)
            for name in re.findall(r'(?:from\s+|import\s*)[\'\"](\.[^\'\"]+)[\'\"]', text):
                imports += 1
                target = path.parent/name
                if not any(Path(str(target)+ext).is_file()
                           for ext in ('', '.ets', '.ts', '.json', '/index.ets')):
                    failures.append('Missing relative import: '+str(path)+' -> '+name)
            targets = re.findall(r"loadContent\(\s*['\"]([^'\"]+)['\"]", text)
            targets += re.findall(r"url\s*:\s*['\"](pages/[^'\"]+)['\"]", text)
            for page in targets:
                routes += 1
                if page not in pages or not (ets/(page+'.ets')).is_file():
                    key = (module, path.relative_to(root).as_posix(), page)
                    if key in documented_routes:
                        known.append(module+' -> '+page+': '+documented_routes[key])
                    else:
                        failures.append('Unresolved page: '+module+' -> '+page)
        if module == 'prototypes/farm-assistant':
            crop = (ets/'pages/CropManage.ets').read_text(encoding='utf-8')
            if crop.rstrip().endswith('.onClick(() => { this.is'):
                known.append('Farm prototype: CropManage source is truncated')
            all_text = '\n'.join(active_text(p) for p in ets.rglob('*.ets'))
            if not re.search(r'RdbManager\s*\.\s*initRdbStore\s*\(', all_text):
                known.append('Farm prototype: no RdbManager initialization call')

    guides = [p for p in ROOT.rglob('*.md')
              if p.relative_to(ROOT).as_posix() not in originals
              and '.git' not in p.parts]
    links = 0
    for path in guides:
        for url in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            if re.match(r'^[a-zA-Z]+:', url) or url.startswith('#'):
                continue
            links += 1
            target = path.parent/unquote(url.split('#', 1)[0])
            if not target.exists():
                failures.append('Broken guide link: '+str(path)+' -> '+url)

    print('Source branches:', len(manifest['branches']))
    print('Original files verified:', len(records))
    print('Documented integration fixes:', len(manifest['adjustments']))
    print('Relative imports checked:', imports)
    print('Page references checked:', routes)
    print('Generated Markdown documents:', len(guides))
    print('Local guide links checked:', links)
    for issue in known:
        print('KNOWN LEGACY ISSUE:', issue)
    for failure in failures:
        print('FAIL:', failure)
    print('PASS (preservation/integration checks; documented legacy issues remain)' if not failures else 'FAILED')
    return int(bool(failures))


if __name__ == '__main__':
    sys.exit(main())
