"""Stage only public files for Cloudflare Pages. Never deploy the repository root."""
from pathlib import Path
import shutil,zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
OUT.mkdir(exist_ok=True)
for name in ['index.html','favicon.svg']:
    shutil.copy2(ROOT/name,OUT/name)
shutil.copytree(ROOT/'deck-toolkit',OUT/'deck-toolkit',dirs_exist_ok=True)
with zipfile.ZipFile(ROOT/'site-upload.zip','w',zipfile.ZIP_DEFLATED) as z:
    for f in sorted(OUT.rglob('*')):
        if f.is_file():z.write(f,f.relative_to(OUT).as_posix())
print(f'Staged {sum(f.is_file() for f in OUT.rglob("*"))} public files in dist/ and site-upload.zip.')
