from pathlib import Path
from html.parser import HTMLParser
import json,re
root=Path(__file__).parent/'dist';errors=[]
class Parser(HTMLParser):
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for name in ['href','src']:
   v=d.get(name,'')
   if v.startswith('/') and not v.startswith('//'):
    f=root/v.split('?')[0].split('#')[0].lstrip('/')
    if not (f.is_file() or (f/'index.html').is_file()):errors.append((str(self.file),v))
  if tag=='img' and 'alt' not in d:errors.append((str(self.file),'missing alt'))
for file in root.rglob('*.html'):
 p=Parser();p.file=file;p.feed(file.read_text())
c=json.loads((root/'catalog.js').read_text().removeprefix('window.JUICE_CATALOG=').removesuffix(';'))
assert len(c['products'])==21 and len(c['collections'])==6
for p in c['products']:
 assert (root/'products'/p['handle']/'index.html').exists()
 assert all((root/i.lstrip('/')).exists() for i in p['images'])
assert not errors,errors
print(json.dumps({'pages':len(list(root.rglob('index.html'))),'products':21,'collections':6,'broken_local_references':0,'images':len(list((root/'assets').iterdir()))}))
