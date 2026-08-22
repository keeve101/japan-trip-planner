from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
from urllib.parse import urlparse
import json,time
URL='https://keeve101.github.io/japan-trip-planner/index.html?links=latest'
with sync_playwright() as p:
  b=p.chromium.launch(headless=True);page=b.new_page(viewport={'width':1440,'height':1000});page.goto(URL,wait_until='domcontentloaded',timeout=60000)
  labels=[x.inner_text().strip() for x in page.locator('.nav button').all()]
  seen={}
  for label in labels:
    try:
      page.get_by_role('button',name=label,exact=True).click();page.wait_for_timeout(150);page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    except Exception: continue
    for a in page.locator('.tab.active a[href]').all():
      href=a.get_attribute('href') or ''; text=a.inner_text().strip()
      if not href.startswith(('http://','https://')) or 'google.com/maps' in href or 'openstreetmap' in href or 'carto' in href: continue
      seen.setdefault(href,{'url':href,'text':text,'tabs':set()})['tabs'].add(label)
  out=[]
  for href,v in sorted(seen.items()):
    q={'url':href,'text':v['text'],'tabs':sorted(v['tabs'])}
    c=b.new_context();pg=c.new_page();
    try:
      r=pg.goto(href,wait_until='domcontentloaded',timeout=30000)
      q.update(status=r.status if r else None,final=pg.url,title=pg.title()[:120],result='working' if r and r.status<400 else 'http-error')
    except PWTimeout:q.update(result='browser-timeout',final=pg.url)
    except Exception as e:q.update(result='browser-error',error=str(e)[:160],final=pg.url)
    c.close();out.append(q)
  print(json.dumps({'checked_at':'2026-08-23','count':len(out),'links':out},indent=2,ensure_ascii=False))
  b.close()
