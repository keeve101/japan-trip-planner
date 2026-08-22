# External link audit — 2026-08-23

Rendered all destination tabs and checked 202 non-map external links in an ordinary headless browser. Google Maps, OpenStreetMap and CARTO links were excluded from HTTP classification. Final deployment at time of audit: `645ecac`.

## Result

- 192 links returned a normal working browser result.
- The following are exceptions and are not all broken:

| URL | Browser result | Classification / action |
|---|---|---|
| `https://www.jreast.co.jp/e/` | 403 | JR East returned 403 Access Denied to automation; official HTTPS URL retained; not classified as broken. |
| `https://www.kkkg.co.jp/bus/timetable/kusakaru_sen.pdf?v=20260401` | browser-error | PDF download started; valid timetable resource, not a broken HTML page. |
| `https://www.kusatsu-onsen.ne.jp/` | browser-timeout | Browser timeout; official domain retained, status incomplete rather than negative. |
| `https://www.mountainproject.com/route/202832824/rinshankaiho` | 429 | Mountain Project returned 429 rate limit; browser-visible page is rate-limited, not proven dead. |
| `https://www.mountainproject.com/route/203457796/in-praise-of-shadows` | 429 | Mountain Project returned 429 rate limit; browser-visible page is rate-limited, not proven dead. |
| `https://www.ukclimbing.com/logbook/crags/mitake-18512/` | 403 | Cloudflare/403 challenge; not classified as broken solely from automation. |
| `https://www.ukclimbing.com/logbook/crags/mitake-3693` | 403 | Cloudflare/403 challenge; not classified as broken solely from automation. |
| `https://www.yokohama.travel/en/` | browser-error | Certificate mismatch in browser; replaced in planner with `https://www.yokohamajapan.com/`. |

## Definite broken links repaired

- `https://commons.wikimedia.org/wiki/File:Enoshima_harbor.jpg` → `https://commons.wikimedia.org/wiki/File:Enoshima_Yacht_Harbor_2022.jpg`
- `https://commons.wikimedia.org/wiki/File:Kamakura_Daibutsu.jpg` → `https://commons.wikimedia.org/wiki/File:The_Great_Buddha_of_K%C5%8Dtoku-in_(Kamakura_Daibutsu).jpg`
- `https://picchio.co.jp/en/` → `https://picchio.co.jp/`
- `https://www.mitakevc.org/` → `https://www.mitaketozan.co.jp/`
- `https://www.seibu-bus.co.jp/sp/karuizawa/` → `https://www.jrbuskanto.co.jp/`
- `http://time.jrbuskanto.co.jp/bk03010.html` removed from the planner in favour of the verified HTTPS JR Bus Kanto homepage.

The audit does not label Google Maps search links or browser-blocked pages as broken merely because automated navigation cannot retrieve them.
