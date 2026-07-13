# Visual overhaul — progress

**Round:** 1 (build) — plan approved (unified chrome; grain/vignette retired; drawn glyphs)
**State:** ⏳ Built and smoke-tested offline; full critic loop still gated on the
network-policy fix (see Blocked).

## Round 1 — what changed
- **One binding:** the per-edition chrome split (parchment serif UI vs. glass cyan UI)
  is gone. All five map plates now share the Iron-Gall chrome: `#212B3A` ground,
  Chart Paper text, Almanac Gold + Rain Blue data inks, hairline rules.
- **Type:** Besley (display) + Archivo (body) + Archivo Narrow (tables/figures)
  replace EB Garamond / IM Fell / Inter / Space Grotesk.
- **Panel is a page:** masthead (THE ALMANAC · Vol. MMXXVI · date · day-of-year),
  numbered sections §1–§7, leader-dotted observation rows, ruled tables.
- **Day-Dial:** the radar bar is now a 24-hour ephemeris strip — night in ink, gold
  sun arc from the real sunrise/sunset, radar loop window in rain-blue, gold NOW
  needle, moon phase in the corner. All previous controls kept.
- **Drawn glyph set** replaces emoji (13 single-weight SVG glyphs + computed moon face).
- **Plate index:** edition switcher restyled with roman numerals, centered over the map.
- Grain/vignette overlays removed; cartouche kept (redrawn). Gradient headline gone.
- **Quality floor:** gold `:focus-visible` rings; `prefers-reduced-motion` starts the
  radar paused, zeroes camera flights, kills animations; sections reserve height while
  loading (no CLS); considered API-failure state with quiet auto-retry.
- Layout verified by measurement at 360/768/900/1120/1440 — no overlaps, no
  horizontal scroll.

## Blocked (unchanged)
Egress policy still denies the data hosts, so everything above was verified only in
offline states (chrome, typography, failure state, layout metrics). The critic loop —
real forecast/radar/alert states, lineup test, regression contract — starts the moment
these are allowlisted: `tiles.openfreemap.org`, `api.open-meteo.com`,
`geocoding-api.open-meteo.com`, `api.rainviewer.com`, `tilecache.rainviewer.com`,
`api.weather.gov`, `gibs.earthdata.nasa.gov`, `mesonet.agron.iastate.edu`,
`services9.arcgis.com`. This session re-checks reachability on a timer.

## Critic findings
None yet — critic rounds require live data.
