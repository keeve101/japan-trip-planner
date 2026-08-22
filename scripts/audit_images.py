from playwright.sync_api import sync_playwright
from collections import defaultdict
import json, re
URL='https://keeve101.github.io/japan-trip-planner/index.html?audit=rendered'
with sync_playwright() as p:
    b=p.chromium.launch(headless=True)
    page=b.new_page(viewport={'width':1280,'height':900})
    page.goto(URL,wait_until='networkidle',timeout=60000)
    # Use visible destination buttons; clicking triggers the app's tab renderer.
    labels=page.locator('.nav button').all_inner_texts()
    records=[]
    for label in labels:
        if 'Overview' in label or 'Itinerary' in label: continue
        try:
            page.get_by_role('button',name=label,exact=True).click()
            page.wait_for_timeout(250)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(500)
            page.evaluate("window.scrollTo(0, 0)")
            page.wait_for_timeout(150)
        except Exception:
            continue
        data=page.evaluate("""(label)=>({label,imgs:[...document.querySelectorAll('.tab.active img')].map((im,i)=>({src:im.currentSrc||im.src,alt:im.alt,loaded:im.complete&&im.naturalWidth>0,card:im.closest('.rec-card')?.querySelector('h3')?.innerText||null,source:im.closest('.rec-card')?.querySelector('a.source')?.href||im.closest('figure')?.querySelector('a.source')?.href||null,hero:!!im.closest('.hero-photo,.dest-head'),loading:im.loading}),)} )""",label)
        records.append(data)
    out=defaultdict(lambda:{'uses':0,'tabs':set(),'cards':[],'loaded':0,'missing':0,'urls':set(),'sources':set()})
    for tab in records:
        for im in tab['imgs']:
            src=im['src']
            if not src or 'carto' in src.lower() or 'tile' in src.lower() or 'leaflet' in src.lower(): continue
            name=src.rsplit('/',1)[-1].split('?',1)[0]
            x=out[name];x['uses']+=1;x['tabs'].add(tab['label']);x['urls'].add(src)
            if im.get('source'): x['sources'].add(im['source'])
            if im['card']: x['cards'].append(im['card'])
            if im['loaded']: x['loaded']+=1
            else: x['missing']+=1
    result={k:{'uses':v['uses'],'tabs':sorted(v['tabs']),'cards':v['cards'],'loaded':v['loaded'],'missing':v['missing'],'urls':sorted(v['urls']),'sources':sorted(v['sources'])} for k,v in sorted(out.items(),key=lambda kv:-kv[1]['uses'])}
    print(json.dumps({'labels':labels,'records':records,'assets':result},ensure_ascii=False,indent=2))
    b.close()
