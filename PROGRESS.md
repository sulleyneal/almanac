# Visual overhaul — progress

**Round:** 1 (build) done — critic loop started with live data
**State:** ▶ Network policy fixed (all nine data hosts allowlisted and verified).
Critic round 1 in flight.

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

## Unblocked (2026-07-13)
The environment's network policy now allowlists all nine data hosts; each was
verified with a real request (radar tile download, NWS point alerts, geocoding).
One sandbox quirk documented for future sessions: the egress gateway resets
*Chromium's* TLS handshake even for allowlisted hosts, so the screenshot harness
routes every external request through Playwright's Node-side fetch
(`context.route` → `request.newContext({proxy})` → `route.fulfill`), which uses
the same TLS stack as curl. All requests still traverse the policy proxy.
Live smoke shot confirmed: tiles, forecast, Day-Dial sun arc, radar loop all real.

## Critic findings
Round 1 in flight (fresh-context critic; live data; 41-item contract + state
matrix + lineup + extremes + a11y).
