# Japan planner rendered image-usage audit

Audit date: 2026-08-23 · deployed commit: `c936a8c` · URL: https://keeve101.github.io/japan-trip-planner/

## Method
- Opened all 20 destination tabs with Playwright at 1280×900.
- Scrolled each active tab to force lazy images to request, then returned to the top.
- Counted content `<img>` elements only; CARTO, Leaflet and map tiles were excluded.
- `loaded` means `complete && naturalWidth > 0` after the forced scroll. A non-loaded item is not automatically treated as absent: it is recorded as a check failure/missing load.
- Card and gallery source links were collected from the rendered DOM.

## Focus findings
- The previously reported `old_street.jpg` count was 18; the final deployed version is **13** after replacing several Karuizawa-specific uses.
- `usui_pass.jpg` is now **8 uses**, but the material attraction-card reuse was reduced: observation platform, Nakasendo, Kumano shrine, chapel, bridges and station no longer use it as their representative image.
- `sengataki_falls.jpg` remains **5 uses** for exact waterfall/forest-area context; stream and viewpoint cards now use distinct forest imagery.
- The new exact/area-specific assets `kumano_kotai.jpg`, `old_karuizawa_ginza.jpg`, `shiraito_alt.jpg`, `karuizawa_forest.jpg`, `harunire_tombo.jpg`, `footbath_hoshino.jpg` and `forest_official_hoshino.jpg` load in the deployed audit.
- Hoshino now includes Sengataki Falls, Harunire Terrace, Tombo-no-Yu, Picchio / Karuizawa Wild Bird Sanctuary, Karuizawa Kogen Church, Stone Church, Seseragi stream walk and Naka-Karuizawa fallback.
- The Hoshino tab contains the current bear warning: sightings were reported between Hoshino and Sengataki in June 2026; visitors should check current notices before forest walks.
- `kfc-net.com` is absent from the final live page; Karuizawa links now use the Tourist Association, official Hoshino Area and attraction-specific sources.

## Asset inventory
| Asset | Rendered uses | Loaded | Failed/not loaded | Destination tabs | Classification / reuse basis |
|---|---:|---:|---:|---|---|
| `mitake.jpg` | 19 | 19 | 0 | Mitake | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `old_street.jpg` | 13 | 13 | 0 | Agatsumakyo / Iwashima; Atami; Hayama; Kamakura; Mitake; Odawara; Shimoda; Shiraito / North Karuizawa; Zushi | Review / representative only: generic street image used for multiple town/food fallback cards; reduced from 18 to 13. Acceptable only where caption marks it representative; avoid as exact attraction imagery. |
| `karuizawa_forest.jpg` | 9 | 9 | 0 | Old Usui Pass / Kyu-Karuizawa; Sengataki / Hoshino; Shiraito / North Karuizawa | Representative forest/route image, explicitly labelled as such; used for stream/viewpoint/pass-side mood where no exact image is verified. |
| `zushi_beach.jpg` | 6 | 6 | 0 | Hayama; Zushi | Exact Zushi Beach hero/card reuse; other Zushi shoreline cards remain representative area-mood uses. |
| `forest.jpg` | 5 | 5 | 0 | Hakone; Mitake; Odawara | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hayama_coast.jpg` | 5 | 5 | 0 | Hayama | Exact/area-mood Hayama coast reuse; not presented as a specific museum or shrine photograph. |
| `agatsuma_gorge.jpg` | 5 | 5 | 0 | Agatsumakyo / Iwashima | Exact Agatsuma Gorge hero/card reuse; bridge/partial-walk cards are labelled area imagery. |
| `old_karuizawa_ginza.jpg` | 5 | 5 | 0 | Old Usui Pass / Kyu-Karuizawa; Sengataki / Hoshino | Exact/area-specific Old Karuizawa Ginza image for old-town cards; not used as a pass or shrine photograph. |
| `lantern_alley.jpg` | 3 | 3 | 0 | Mitake; Zushi | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `okutama_lake.jpg` | 3 | 3 | 0 | Okutama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `temple_sunset.jpg` | 3 | 3 | 0 | Atami; Hayama; Okutama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `atami.jpg` | 3 | 3 | 0 | Atami | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `yokohama.jpg` | 3 | 3 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `odawara.jpg` | 3 | 3 | 0 | Odawara | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `shimoda.jpg` | 3 | 3 | 0 | Shimoda | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kamogawa.jpg` | 3 | 3 | 0 | Shimoda | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `misaki_harbor.jpg` | 3 | 3 | 0 | Misaki | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `misaki_harbor2.jpg` | 3 | 3 | 0 | Misaki | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kusatsu_yubatake.jpg` | 3 | 3 | 0 | Kusatsu Onsen | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kusatsu_town.jpg` | 3 | 3 | 0 | Kusatsu Onsen | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hakone_lake.jpg` | 3 | 3 | 0 | Hakone | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `asakusa_sensoji.jpg` | 3 | 3 | 0 | East Tokyo | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `shiraito_falls.jpg` | 3 | 3 | 0 | Shiraito / North Karuizawa | Exact hero/card reuse for Shiraito Falls; forest/card alternatives use shiraito_alt.jpg or representative forest imagery. |
| `sengataki_falls.jpg` | 3 | 3 | 0 | Sengataki / Hoshino | Exact hero/card reuse for Sengataki Falls; distinct forest/stream cards now use forest assets. |
| `harunire_tombo.jpg` | 3 | 3 | 0 | Sengataki / Hoshino | Official Hoshino Area cluster image for Harunire/Tombo; not presented as Sengataki Falls. |
| `usui_pass.jpg` | 3 | 3 | 0 | Old Usui Pass / Kyu-Karuizawa | Exact hero / exact Old Usui Pass card / gallery reuse; no longer used for observation platform, Nakasendo, shrine, chapel or station cards. |
| `cherry_river.jpg` | 2 | 2 | 0 | Okutama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kamakura_buddha.jpg` | 2 | 2 | 0 | Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kyoto_street.jpg` | 2 | 2 | 0 | Hayama; Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `yuigahama.jpg` | 2 | 2 | 0 | Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `enoshima_harbor.jpg` | 2 | 2 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `enoshima_sunset.jpg` | 2 | 2 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `enoshima_harbor2.jpg` | 2 | 2 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `tokyo_night.jpg` | 2 | 2 | 0 | Atami; East Tokyo | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `yokohama_harbour.jpg` | 2 | 2 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `fuji_temple.jpg` | 2 | 2 | 0 | Odawara | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `jogashima_lighthouse.jpg` | 2 | 2 | 0 | Misaki | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kusatsu_sainokawara.jpg` | 2 | 2 | 0 | Kusatsu Onsen | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hakone_open_air.jpg` | 2 | 2 | 0 | Hakone | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hakone_owakudani.jpg` | 2 | 2 | 0 | Hakone | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `ryogoku_kokugikan.jpg` | 2 | 2 | 0 | East Tokyo | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `tokyo_skytree.jpg` | 2 | 2 | 0 | East Tokyo | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `iwashima_station.jpg` | 2 | 2 | 0 | Agatsumakyo / Iwashima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `yamba_dam.jpg` | 2 | 2 | 0 | Agatsumakyo / Iwashima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kawarayu_oyu.jpg` | 2 | 2 | 0 | Agatsumakyo / Iwashima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `naganohara_station.jpg` | 2 | 2 | 0 | Agatsumakyo / Iwashima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `shiraito_alt.jpg` | 2 | 2 | 0 | Shiraito / North Karuizawa | Alternate exact Shiraito waterfall/forest view; prevents all Shiraito-area cards from using the hero frame. |
| `hoshino_onsen.jpg` | 2 | 0 | 2 | Sengataki / Hoshino | Exact Hoshino Onsen environment image. |
| `forest_official_hoshino.jpg` | 2 | 2 | 0 | Sengataki / Hoshino | Official Hoshino Area forest image; area-mood use only. |
| `kumano_kotai.jpg` | 2 | 2 | 0 | Old Usui Pass / Kyu-Karuizawa | Exact attraction image for Kumano Kotai Shrine; source link is the Karuizawa Tourist Association page. |
| `mitake_station.jpg` | 1 | 0 | 1 | Mitake | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `mitake_shrine.jpg` | 1 | 1 | 0 | Mitake | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `ogouchi_shrine.jpg` | 1 | 1 | 0 | Okutama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `nippara_cave.jpg` | 1 | 1 | 0 | Okutama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kamakura.jpg` | 1 | 1 | 0 | Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hasedera.jpg` | 1 | 1 | 0 | Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hokokuji.jpg` | 1 | 1 | 0 | Kamakura | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `enoshima_shrine.jpg` | 1 | 1 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `enoshima_iwaya.jpg` | 1 | 1 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `katase_beach.jpg` | 1 | 1 | 0 | Enoshima | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `zushi_coast.jpg` | 1 | 1 | 0 | Zushi | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `atami_sun_beach.jpg` | 1 | 1 | 0 | Atami | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kinomiya.jpg` | 1 | 1 | 0 | Atami | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `moa.jpg` | 1 | 1 | 0 | Atami | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `shibuya_night.jpg` | 1 | 1 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `yokohama_chinatown.jpg` | 1 | 1 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `sankeien.jpg` | 1 | 1 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `cup_noodles.jpg` | 1 | 1 | 0 | Yokohama | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `seafood_shop.jpg` | 1 | 1 | 0 | Odawara | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `shimoda_onsen.jpg` | 1 | 1 | 0 | Shimoda | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `hakone_ropeway.jpg` | 1 | 1 | 0 | Hakone | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `kappabashi.jpg` | 1 | 1 | 0 | East Tokyo | Reviewed rendered asset; inspect card/gallery source links for exact versus representative caption. |
| `footbath_hoshino.jpg` | 1 | 1 | 0 | Sengataki / Hoshino | Official Hoshino Area image for Hoshino relaxation context. |

## Source pages captured from rendered cards

- **`mitake.jpg`** — [1](https://www.mountainproject.com/area/106672476/mitake)
- **`old_street.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hayama%20caf%C3%A9s%20and%20seafood); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Heiwa-dori%20%2F%20Atami%20Ginza); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Historic-street%20atmosphere); [4](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Karuizawa%20Station%20%2F%20onward%20rail); [5](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Karuizawa%20relaxation%20fallback); [6](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Karuizawa%20station%20%2F%20old-town%20food); [7](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Karuizawa%20town%20fallback); [8](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Komachi-dori%20%2B%20Tsurugaoka%20Hachimangu); [9](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Naganohara%20%2F%20Iwashima%20local%20food%20stop); [10](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Odawara%20station%20streets); [11](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Ome%20food%20and%20supplies); [12](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Perry%20Road); [13](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Zushi%20station%20food%20streets)
- **`karuizawa_forest.jpg`** — [1](https://www.karuizawa-kankokyokai.jp/en/)
- **`zushi_beach.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Miura%20Peninsula%20beach%20atmosphere); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Nagisa%20Bridge%20%2F%20marina%20edge); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Zushi%20Beach); [4](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Zushi%20Marina%20%2F%20Sagami%20Bay%20view)
- **`forest.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Forest%20atmosphere%20for%20the%20Okutama%20side%20trip); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hakone-Yumoto%20onsen%20town); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Odawara-area%20landscape%20atmosphere%E2%80%94not%20a%20specific%20attraction); [4](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Soga%20Plum%20Grove%20%2F%20west%20Odawara); [5](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Tama%20River%20%2F%20rock%20condition%20check)
- **`hayama_coast.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hayama%20Museum%20of%20Modern%20Art); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hayama%20coast); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Isshiki%20Beach); [4](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Nagasawa%20%2F%20coastal%20viewpoints)
- **`agatsuma_gorge.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Agatsuma_Gorge_Aerial_photograph.jpg)
- **`old_karuizawa_ginza.jpg`** — [1](https://www.karuizawa-kankokyokai.jp/en/spot/old-karuizawa-ginza/)
- **`lantern_alley.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Caf%C3%A9s%20%2B%20Kamakura%20fallback); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Evening%20caf%C3%A9-street%20atmosphere); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Tokyo-region%20evening%20atmosphere)
- **`okutama_lake.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Lake%20Okutama); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Lake%20Okutama%20%2F%20Ogouchi%20Dam)
- **`temple_sunset.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Japanese%20evening%20atmosphere); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Morito%20Shrine%20%2B%20coast); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Temple%20and%20mountain%20atmosphere)
- **`atami.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Atami%20Castle%20viewpoint); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Atami%20port)
- **`yokohama.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Minato%20Mirai%20waterfront); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Yokohama%20Minato%20Mirai)
- **`odawara.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Odawara%20Castle); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Odawara%20Castle%20Park)
- **`shimoda.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Shirahama%20Beach)
- **`kamogawa.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Pacific%20coast%20atmosphere); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Port%20seafood%20and%20Kinmedai); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Ryugu%20Sea%20Cave)
- **`misaki_harbor.jpg`** — [1](https://commons.wikimedia.org/wiki/File:250429_Misaki_Harbor_01.jpg)
- **`misaki_harbor2.jpg`** — [1](https://commons.wikimedia.org/wiki/File:250429_Misaki_Harbor_04.jpg)
- **`kusatsu_yubatake.jpg`** — [1](https://commons.wikimedia.org/wiki/File:2023.04.26_Yubatake_(Kusatsu_Onsen).jpg)
- **`kusatsu_town.jpg`** — [1](https://commons.wikimedia.org/wiki/File:251128_Onsen_Town_in_Kusatsu_12.jpg)
- **`hakone_lake.jpg`** — [1](https://commons.wikimedia.org/wiki/File:A_view_of_Lake_Ashi_with_Peace_Torii_gate,_Hakone,_Japan1.jpg)
- **`asakusa_sensoji.jpg`** — [1](https://commons.wikimedia.org/wiki/File:20100725_Tokyo_Five-storied_Pagoda_Sensoji_5379.jpg)
- **`shiraito_falls.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Karuizawa_shiraito-no-taki03s3200.jpg)
- **`sengataki_falls.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Sengataki_Falls_(Nagano)_01.jpg)
- **`harunire_tombo.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Harunire%20Terrace); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hoshino%20forest%20area); [3](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Tombo-no-Yu)
- **`usui_pass.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Old_Usui_Pass.JPG)
- **`cherry_river.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hikawa%20Gorge%20%2F%20river%20walk); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=River-side%20evening%20atmosphere)
- **`kamakura_buddha.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Kamakura_Daibutsu.jpg)
- **`kyoto_street.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Small-street%20atmosphere); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Temple-street%20atmosphere)
- **`yuigahama.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Yuigahama_beach_05.jpg)
- **`enoshima_harbor.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Enoshima_harbor.jpg)
- **`enoshima_sunset.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Enoshima%20Sea%20Candle); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Sunset%20viewed%20from%20Enoshima)
- **`enoshima_harbor2.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Enoshima%20harbour); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Island%20seafood%20lanes)
- **`tokyo_night.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Asakusa%20evening%20food%20and%20river%20walk); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Night-city%20atmosphere)
- **`yokohama_harbour.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Yamashita%20Park%20%2B%20Osanbashi); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Yokohama%20harbour%20waterfront)
- **`fuji_temple.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Castle%20museum%20%2F%20indoor%20backup); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Historic%20Japanese%20landscape%20atmosphere)
- **`jogashima_lighthouse.jpg`** — [1](https://commons.wikimedia.org/wiki/File:250429_Jogashima_Lighthouse_03.jpg)
- **`kusatsu_sainokawara.jpg`** — [1](https://commons.wikimedia.org/wiki/File:251128_Sainokawara_Park_10.jpg)
- **`hakone_open_air.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Hakone_Open-air_Museum_20211202-5.jpg)
- **`hakone_owakudani.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Owakudani_Valley_near_Owakudani_Station.JPG)
- **`ryogoku_kokugikan.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Ryogoku_Great_Sumo_Hall.jpg)
- **`tokyo_skytree.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Skytree_20220708182810_(52279108935).jpg)
- **`iwashima_station.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Iwashima%20Station%20%2F%20village%20approach); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Iwashima%20Station%20building)
- **`yamba_dam.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Yamba%20Dam%20%2F%20Agatsuma%20Lake)
- **`kawarayu_oyu.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Kawarayu%20Onsen%20Oyu); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Kawarayu-Onsen%20Station%20%2F%20Kawarayu%20Onsen)
- **`naganohara_station.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Naganohara-Kusatsuguchi%20Station)
- **`shiraito_alt.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Karuizawa_shiraito-no-taki03s3200.jpg)
- **`hoshino_onsen.jpg`** — [1](https://commons.wikimedia.org/wiki/File:160730_Hoshino_Onsen_Karuizawa_Nagano_pref_Japan01bs3.jpg)
- **`forest_official_hoshino.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hoshino%20forest%20area); [2](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hoshino%20forest%20atmosphere)
- **`kumano_kotai.jpg`** — [1](https://www.karuizawa-kankokyokai.jp/en/spot/kumano-kotai-shrine/)
- **`mitake_station.jpg`** — [1](https://commons.wikimedia.org/wiki/File:JREast-Ome-line-Mitake-station-entrance.jpg)
- **`mitake_shrine.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Miyamasu_Mitake_Shrine_(53086177055).jpg)
- **`ogouchi_shrine.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Ogouchi_Shrine_@_Lake_Okutama_(11206233905).jpg)
- **`nippara_cave.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Nippara_Limestone_Cave_(15504098295).jpg)
- **`kamakura.jpg`** — No card source link captured (hero/gallery source is in the image caption/source registry).
- **`hasedera.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Hase-dera.jpg)
- **`hokokuji.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Hokokuji_in_Kamakura_(2582072655).jpg)
- **`enoshima_shrine.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Enoshima_Shrine_(13897760842).jpg)
- **`enoshima_iwaya.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Iwaya_Caves_-_Enoshima,_Japan_-_DSC07917.jpg)
- **`katase_beach.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Sunny_December_2023,_Katase_Nishihama_beach_13.jpg)
- **`zushi_coast.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Zushi%20coast)
- **`atami_sun_beach.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Atami_Sun_Beach_-_Aug_29,_2013_(1).jpg)
- **`kinomiya.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Kinomiya_Jinja_(Kinomiya_Shrine)_20100612.jpg)
- **`moa.jpg`** — [1](https://commons.wikimedia.org/wiki/File:230127_MOA_Museum_of_Art_Atami_Japan14s3.jpg)
- **`shibuya_night.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Japanese%20city%20night%20atmosphere)
- **`yokohama_chinatown.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Yokohama%20Chinatown)
- **`sankeien.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Sankei-en_20221127-1.jpg)
- **`cup_noodles.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Cup_Noodles_Museum_@_Yokohama_(9052323677).jpg)
- **`seafood_shop.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Odawara%20Fish%20Market)
- **`shimoda_onsen.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Shimoda%20onsen%20stays)
- **`hakone_ropeway.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hakone%20Ropeway%20%2F%20Tozan%20scenic%20transport)
- **`kappabashi.jpg`** — [1](https://commons.wikimedia.org/wiki/File:Cream_and_red_coffee_cup-shaped_balconies,_Niimi_Tableware,_Kappabashi_Dougu_Street,_Tokyo,_Japan.jpg)
- **`footbath_hoshino.jpg`** — [1](https://commons.wikimedia.org/wiki/Special:MediaSearch?type=image&search=Hoshino%20forest%20footbath)

## Intentional image-free cards
- Picchio / Karuizawa Wild Bird Sanctuary
- Karuizawa Kogen Church
- Stone Church
- Ryugaeshi Falls
- Historic Karuizawa architecture / Manpei Hotel area
- Megane Bridge / railway-history branch

These cards explicitly say no reusable exact image was verified; they do not fall back to a misleading generic photograph.
