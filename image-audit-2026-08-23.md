# Image audit — 2026-08-23

## Result

The first audit reported approximately 124 non-loading rendered image instances. A deduplicated browser DOM pass found **55 distinct URLs represented by 108 currently non-naturalWidth instances** in the deployed page after the image fallback change. The earlier 124 count included additional lazy-loaded/remote instances during the full-page pass; it was not a count of distinct assets.

`naturalWidth === 0` is not, by itself, proof of a network failure: lazy images in unvisited tabs may not have attempted a request. Therefore this list is an affected/needs-verification list, not a claim that every entry is a separately confirmed HTTP 404.

The repeated-instance effect is substantial: `old_street.jpg` appears 18 times, `forest.jpg` 5 times, and several others appear 2–3 times.

## Deduplicated affected URLs/files

Counts are rendered DOM instances in the audit pass.

```text
forest.jpg 5
lantern_alley.jpg 3
mitake_station.jpg 1
mitake_shrine.jpg 1
old_street.jpg 18
cherry_river.jpg 2
temple_sunset.jpg 3
ogouchi_shrine.jpg 1
nippara_cave.jpg 1
kamakura_buddha.jpg 2
kyoto_street.jpg 2
yuigahama.jpg 2
hasedera.jpg 1
hokokuji.jpg 1
enoshima_sunset.jpg 2
enoshima_harbor2.jpg 2
enoshima_shrine.jpg 1
enoshima_iwaya.jpg 1
katase_beach.jpg 1
zushi_coast.jpg 1
tokyo_night.jpg 2
atami_sun_beach.jpg 1
kinomiya.jpg 1
moa.jpg 1
yokohama_harbour.jpg 2
shibuya_night.jpg 1
yokohama_chinatown.jpg 1
sankeien.jpg 1
cup_noodles.jpg 1
fuji_temple.jpg 2
seafood_shop.jpg 1
kamogawa.jpg 3
shimoda_onsen.jpg 1
jogashima_lighthouse.jpg 2
misaki_harbor2.jpg 3
kusatsu_sainokawara.jpg 2
kusatsu_town.jpg 3
hakone_open_air.jpg 2
hakone_owakudani.jpg 2
hakone_ropeway.jpg 1
ryogoku_kokugikan.jpg 2
tokyo_skytree.jpg 2
kappabashi.jpg 1
iwashima_station.jpg 2
yamba_dam.jpg 2
kawarayu_oyu.jpg 2
naganohara_station.jpg 2
shiraito_alt.jpg 1
karuizawa_forest.jpg 1
hoshino_onsen.jpg 2
harunire_tombo.jpg 2
footbath_hoshino.jpg 1
forest_official_hoshino.jpg 2
kumano_kotai.jpg 1
old_karuizawa_ginza.jpg 1
```

## Classification

- **Local asset paths:** all entries above use the deployed `japan-trip-assets/` path. They are genuine site asset candidates to verify against the repository and should not be replaced with downloaded images without provenance/licence records.
- **Remote Mountain Project images:** the problem-card implementation no longer depends on them for rendering. It uses the locally hosted Mitake area image and keeps the Mountain Project page as the research/source link; no topo is reproduced.
- **Browser/network distinction:** this DOM list combines images that failed/are absent with lazy images that may not yet have attempted loading. The browser console had no JavaScript errors. A future asset repair pass should use HTTP status/stat checks plus a forced lazy-image traversal before declaring a file a confirmed 404.
- **Preservation rule:** functioning images were not replaced. Failed image containers are intentionally removed at runtime to avoid broken-image icons while the source asset list remains available for a proper provenance-based replacement pass.
