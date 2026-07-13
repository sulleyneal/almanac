# Visual overhaul — progress

**Round:** 2 — round-1 findings fixed, critic round 2 in flight
**State:** ▶ Critic round 1 returned 6 major + 8 minor findings; all 14 fixed
and smoke-verified. Done = two consecutive critic rounds with zero majors.

## Round 1 critic findings → fixes (all landed)
Majors:
1. **Wind canvas was 600×300 in a corner** (and forced hscroll at 360 on every
   plate) → canvas now stretched (`width/height:100%`); JPG export composites
   correctly.
2. **Day-Dial collided with panel/cartouche/attribution** → dial now centers on
   the plate (not the viewport) with width capped to clear both corners; the
   antique cartouche steps above the dial band; the compact attribution starts
   folded to its ⓘ mark.
3. **Scale bars hidden behind the panel** → bottom-left controls moved onto the
   plate (392 px), and lifted above the dial at 761–1020 px and on mobile.
4. **No focus ring on map controls** → explicit gold `:focus-visible` outline on
   all MapLibre controls; Day-Dial got `role=img` + a narrated ephemeris label.
5. **Two clocks in one UI** → every printed time (radar clock, "as of", alert
   chips, masthead date/day-number) now uses the place's own timezone; map-tap
   alert popups print the alert's own wall clock, matching NWS headlines.
6. **Uncaught MapLibre exceptions on plate swaps** → root-caused to the terrain
   depth pass running mid-`setStyle`; terrain is parked during the swap and
   re-hung on `styledata`. 12 consecutive swaps: zero exceptions.

Minors: chart low-label no longer mashes into the tick row; long single-word
place names shrink-to-fit instead of breaking mid-word; dial hour labels 9 px;
cloud-tops lose the checkerboard seams (no vertical gradient + cell overlap);
alert fills readable over radar (0.22); radar loop holds a frame until the next
one's tiles arrive (no blank flashes); Relief gets lowland color stops; the
restored place lands above the mobile sheet.

Plus one excavated during the fix: **the spot marker was invisible on any
terrain at low zoom** — 3-D terrain depth-culls circle layers, so the dot is
now a terrain-tracking DOM marker (solid via `opacityWhenCovered:1`), drawn
into the JPG export by hand, with the label still a style layer.

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
- **Round 1** (full matrix, live data): 6 majors / 8 minors — listed above, all
  fixed. Contract: 31 OK, 4 partial, rest environmental (no active hurricanes
  on Earth to render; sky/fog and no-WebGL unverifiable headless).
- **Round 2**: in flight.
