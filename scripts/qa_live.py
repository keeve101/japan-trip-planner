from playwright.sync_api import sync_playwright
import json
URL='https://keeve101.github.io/japan-trip-planner/index.html?qa=beb3525'
with sync_playwright() as p:
 b=p.chromium.launch(headless=True);pg=b.new_page(viewport={'width':1440,'height':1000});errs=[];pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None);pg.goto(URL,wait_until='networkidle',timeout=90000)
 buttons=pg.locator('.nav button');labels=[buttons.nth(i).inner_text().strip() for i in range(buttons.count())]
 failures=[];counts={}
 for label in labels:
  try:
   pg.get_by_role('button',name=label,exact=True).click();pg.wait_for_timeout(300);pg.evaluate('window.scrollTo(0,document.body.scrollHeight)');pg.wait_for_timeout(300)
   imgs=pg.locator('.tab.active img');counts[label]=imgs.count()
   for i in range(imgs.count()):
    im=imgs.nth(i);src=im.get_attribute('src')
    if not im.evaluate('(x)=>x.complete && x.naturalWidth>0'): failures.append((label,src))
  except Exception as e: failures.append((label,str(e)))
 mapok=pg.locator('#regional-map .leaflet-marker-icon').count()>=10
 pg.set_viewport_size({'width':390,'height':844});pg.goto(URL,wait_until='networkidle',timeout=90000);overflow=pg.evaluate('document.documentElement.scrollWidth>innerWidth')
 print(json.dumps({'tabs':len(labels),'image_failures':failures,'tab_image_counts':counts,'map_markers':pg.locator('#regional-map .leaflet-marker-icon').count(),'console_errors':errs,'mobile_horizontal_overflow':overflow},indent=2))
 b.close()
