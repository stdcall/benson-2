"""Install the GAP packages that the Sage checks need into the user GAP root
(~/.gap/pkg): the character table library and the packages it requires.
The SageMath container of CI has no character table library; a local
SageMath installation usually has it already. Pinned versions, verified by
SHA-256; nothing else is changed.

usage: sage -python scripts/install_gap_packages.py
"""
import hashlib
import io
from pathlib import Path
import tarfile
import urllib.request

PACKAGES = (
    ('https://github.com/gap-packages/utils/releases/download/v0.92/'
     'utils-0.92.tar.gz',
     'f2dad4d922eaa1aa535f3e76fa5e858f97ce829cc4fd7a4dc1a314d814b9a53b'),
    ('https://www.math.rwth-aachen.de/~Thomas.Breuer/atlasrep/'
     'atlasrep-2.1.9.tar.gz',
     '4d1bb336c44985d982411d9113430b50e846d4192cfe9e9c15126328225c5e79'),
    ('https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/'
     'ctbllib-1.3.9.tar.gz',
     '0e676abee52f460f6e4cc24d2d42aa6e75839ce69596f1786e4eece33fb9187f'),
)

target = Path.home() / '.gap' / 'pkg'
target.mkdir(parents=True, exist_ok=True)
for url, digest in PACKAGES:
    with urllib.request.urlopen(url, timeout=300) as response:
        data = response.read()
    actual = hashlib.sha256(data).hexdigest()
    if actual != digest:
        raise SystemExit(f'{url}: SHA-256 {actual}, expected {digest}')
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        archive.extractall(target, filter='data')
    print('installed', url.rsplit('/', 1)[1], 'in', target)
