from pathlib import Path
import concurrent.futures, subprocess, json, re, html, urllib.parse, xml.etree.ElementTree as ET

base=Path(__file__).parent; assets=base.parent/'dist/assets'; origin='https://thejuicebarjuicecompany.com'
def get(url,path):
 path.parent.mkdir(parents=True,exist_ok=True)
 r=subprocess.run(['curl','-L','--silent','--fail','--max-time','20',url,'-o',str(path)],capture_output=True)
 return r.returncode==0

sm=ET.parse(base/'sitemap.xml'); ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
sitemaps=[n.text for n in sm.findall('.//s:loc',ns) if 'agentic' not in n.text]
def sitemap(url):
 p=base/urllib.parse.urlsplit(url).path.lstrip('/'); get(url,p)
 try:return [x.text for x in ET.parse(p).findall('.//s:loc',ns)]
 except:return []
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex: urls=sum(ex.map(sitemap,sitemaps),[])
urls=list(dict.fromkeys(urls+[origin+'/cart',origin+'/search',origin+'/collections/all']))
def page(url):
 path=urllib.parse.urlsplit(url).path.strip('/') or 'home'
 get(url,base/'pages'/f'{path.replace("/","__")}.html')
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:list(ex.map(page,urls))
products=json.load(open(base/'products.json'))['products']; jobs=[]; mapping={}
for p in products:
 for i,im in enumerate(p['images']):
  ext=Path(urllib.parse.urlsplit(im['src']).path).suffix
  filename=f'{p["handle"]}-{i}{ext}';jobs.append((im['src'],assets/filename));mapping[im['src']]='/assets/'+filename

s=(base/'home.html').read_text(); image_urls=set()
for v in re.findall(r'''(?:https:)?//thejuicebarjuicecompany.com/cdn/shop/(?:files|products)/[^\s"'<>]+''',s):
 v=html.unescape(v)
 if re.search(r'\.(jpg|png|webp|jpeg)',v,re.I):image_urls.add('https:'+v if v.startswith('//') else v)
for i,url in enumerate(sorted(image_urls)):
 ext=re.search(r'\.(jpg|png|webp|jpeg)',url,re.I)[0];name=f'brand-{i}{ext}';jobs.append((url,assets/name));mapping[url]='/assets/'+name
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex: results=list(ex.map(lambda j:get(*j),jobs))
(base/'asset-map.json').write_text(json.dumps(mapping,indent=2));(base/'page-inventory.json').write_text(json.dumps(urls,indent=2))
collections=['frontpage','juice-cleanse','sea-moss','wellness-shots','gift-cards','1-2-gallon-jugs']
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:list(ex.map(lambda c:get(origin+f'/collections/{c}/products.json?limit=250',base/f'collection-{c}.json'),collections))
print(json.dumps({'pages':len(urls),'products':len(products),'assets':sum(results),'unavailable_assets':len(results)-sum(results)}))
