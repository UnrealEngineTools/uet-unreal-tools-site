"""Validate generated pages, local assets and fragment links without browser dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json, html
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True);self.links=[];self.ids=[];self.h1=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
files=[ROOT/'index.html',*(ROOT/'deck-toolkit').rglob('index.html')]
pages={f:Page(f.read_text(encoding='utf-8')) for f in files}
for f,p in pages.items():
    rendered=html.unescape(f.read_text(encoding='utf-8'))
    assert not any(c in rendered for c in ('\u00c2','\u00c3','\u00e2')),f'Possible UTF-8 mojibake: {f}'
    assert len(p.ids)==len(set(p.ids)),f'Duplicate anchor: {f}'
    assert p.h1==1,f'Expected one main heading: {f}'
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        target=(ROOT/u.path.lstrip('/') if u.path.startswith('/') else f.parent/u.path).resolve() if u.path else f
        assert target.is_relative_to(ROOT),link
        if target.is_dir():target/= 'index.html'
        assert target.exists(),f'Missing target: {f}: {link}'
        if u.fragment:assert unquote(u.fragment) in pages[target].ids,f'Missing anchor: {f}: {link}'
index=json.loads((ROOT/'deck-toolkit/assets/search.json').read_text())
assert len(index)==11 and len({p['url'] for p in index})==11
assert all(p['text'].strip() and p['summary'].strip() for p in index)
print(f'PASS: {len(pages)} pages; all local links, fragments and assets; 11 searchable topics.')
