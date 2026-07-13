# Visual overhaul — progress

**Round:** 3 — round-2 findings fixed, critic round 3 in flight
**State:** ▶ Round 2 returned 4 majors + 10 minors (down from 6 + 8). All fixed
and smoke-verified. Done = two consecutive critic rounds with zero majors.

## Round 2 critic findings → fixes (all landed)
Majors:
1. **13 uncaught TypeErrors in 15 plate switches with weather layers on** —
   root-caused to MapLibre's style diff re-binding the fill-extrusion layers'
   data-driven paint against buckets the workers still held. Plate swaps now do
   a full style rebuild (`diff:false`) with the weather sources baked empty and
   refilled from the in-memory caches on `styledata`. 15 switches, all six
   layers on: **zero errors** (was 13).
2. **Sliders had no visible keyboard focus** — the track reset carried
   `outline:none`; all five ranges now take the gold ring.
3. **Antique cartouche covered both scale bars at 768** — the ornament now
   yields below 1120 px (mobile already hid it).
4. **Attribution mark sat on the bottom sheet's live figures at 360** — the
   bottom-right controls ride above the sheet (and above the dial when shown),
   mirroring the scale bars.

Minors: the radar clock re-prints the moment a new place's forecast (and
timezone) lands, and a relocation drops the old place's forecast immediately —
the instruments run on a longitude-estimated clock (±1 h) rather than the old
place's or the browser's; chart hi/lo figures get a ground-colored halo over
full-height rain bars; sub-hundredth precipitation prints "trace", never
"0.00 in"; the basemap-outage notice moved from the footer to under the search
box; polar day/night prints an em-dash instead of "sunrise 12:00 am"; the
abandoned search text clears on dismissal; PAST/NOW/FORECAST tag up to 9.5 px;
the moon glyph steps aside when the needle rides near midnight; Relief's spot
dot is brick (the teal one vanished into the green field); cloud-top columns
skip the faint warm-deck wash and drop to 0.68 opacity.

Design decision (recorded in DESIGN.md §0 item 12): **the Day-Dial is no longer
a hostage of the radar toggle.** Radar off folds away only the controls row,
the loop window and the frame tick — the day strip, sun arc, needle and moon
stay out. The ephemeris is the app's spine, not a radar accessory.

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
- **Round 2** (full matrix, live data): 4 majors / 10 minors — listed above,
  all fixed. Contract: 34 OK, 3 partial, rest environmental. The two rounds
  agree the concept holds; the failures were craft and edge cases.
- **Round 3**: in flight. Needs zero majors here AND in round 4 to finish.
