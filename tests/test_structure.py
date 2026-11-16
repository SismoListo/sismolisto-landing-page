"""Structural checks for a single deployable web root under public/."""
from pathlib import Path
from html.parser import HTMLParser
import re
ROOT=Path(__file__).resolve().parents[1]
WEB=ROOT/'public'
html=(WEB/'index.html').read_text(encoding='utf-8')
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.scripts=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and a.get('rel')=='stylesheet':self.links.append(a['href'])
        if tag=='script' and a.get('src'):self.scripts.append(a['src'])
s=Links();s.feed(html)
assert not (ROOT/'index.html').exists(), 'Duplicado de index.html en raíz'
assert not any((ROOT/d).exists() for d in ['assets','css','js']), 'Carpeta antigua duplicada'
assert (WEB/'favicon.ico').is_file()
assert 'assets/styles/styles.css' in s.links
assert s.scripts==['assets/scripts/main.js'], s.scripts
for rel in s.links+s.scripts:
    if rel.startswith('https:'):continue
    assert (WEB/rel).is_file(),rel
styles=(WEB/'assets/styles/styles.css').read_text(encoding='utf-8')
mods=re.findall(r'@import url\("\./([^"\n]+\.css)"\)',styles)
assert len(mods)==20,(len(mods),mods)
assert len(set(mods))==len(mods)
assert mods[-2:]==['base/responsive.css','features/acceptance.css'],mods[-2:]
assert all((WEB/'assets/styles'/p).is_file() for p in mods)
main=(WEB/'assets/scripts/main.js').read_text(encoding='utf-8')
assert re.findall(r'import "\./([^"\n]+\.js)"',main)==['app.js','acceptance.js']
assert all((WEB/'assets/scripts'/p).is_file() for p in ['app.js','acceptance.js'])
assert (WEB/'assets/images/brand/README.md').is_file()
print('OK: public/index.html único, favicon, 20 CSS, 2 JS, imágenes y módulos enlazados.')
