# Visual overhaul — progress

**Round:** 5 — **DONE. Rounds 4 and 5 both returned zero major findings —
two consecutive clean rounds, the loop's termination condition.**
**State:** ✅ Complete. The build the critics cleared is the build on this
branch — no code changed after round 5's review.

## Terminal state (round 5 verdict, fresh-eyes critic)
- 2× full plate cycling with all nine layers on: **0 pageerrors, 0 console
  errors**.
- Alert chip / map popup / NWS headline agree verbatim against the live feed.
- Clock coherence verified numerically in Honolulu, Ruston, Riyadh, Vostok —
  masthead, "as of", radar clock and dial needle all on the place's own time;
  the transient after a far search correctly shows the marked "≈" estimate.
- Full keyboard ring, reduced-motion pause, honest degradation in all four
  simulated outages, no horizontal scroll anywhere.
- Contract: **40 of 41 OK** (item 18, hurricane rendering, remains honestly
  unverifiable — zero tropical cyclones existed on Earth during all five
  rounds; the feed queries fire and the empty state is truthful).
- Critic's own words: "This reads as one product across all five plates …
  I would ship it."

## Noted follow-ups (round-5 minors, deliberately NOT applied post-loop —
the shipped build is exactly what two clean rounds reviewed)
1. Wind-flow trails have low salience on light plates in light wind (the
   critic's first fix-next pick).
2. No extreme-cold badge tier: −85 °F is captioned "below freezing" (the
   critic's second pick — add a blue "extreme cold" mark ≤ −30 °F).
3. OSM labels can pass under the right-edge tool column at 360.
4. The 48-h rain bars carry no % scale cue.
5. Tapping the rain layer where no rain fell gives no "nothing here" feedback.

## Round 4 (first clean round) — minors triaged
Fixed:
- Slow layer builds now say so: the cloud-tops and rain toggles show
  "inking…" beside their labels while a build is in flight, and the §5 prose
  explains what the tag means.
- The search input (first tab stop) takes the full gold focus ring.
- The estimated clock is marked: with no forecast aboard, the radar clock
  prints "≈ 1:30 AM" instead of asserting the longitude guess as fact.
- A relocation now empties the previous place's drawn sections outright —
  no stale chart under a new heading, even in the DOM.
Attempted and reverted:
- A light-plate filter to drop the faintest cloud cells erased a real overcast
  (midnight control showed a full deck where filtered antique showed clear
  sky). Data fidelity wins: the filter is reverted; the light-plate deck keeps
  the sheer grey-blue material from round 4.
Accepted with rationale:
- Cloud-tops tile seams: inherent to the per-cell IR sampling; softening
  requires a resampling architecture, out of scope for a visual overhaul.
- 9 px dial labels / 9.5 px radar tag: at the floor, not below it; crisp at
  2× DPR; enlarging breaks the strip's proportions.
- All-layers-on "pixel soup": user-chosen composition; the product does not
  override an explicit choice.

## Round 3 critic findings → fixes (all landed)
Majors:
1. **Alert chip printed the wrong "until" time** (2 h off — the longitude
   estimate formatting a stamp that carries its own zone) → chips now print the
   alert's own wall clock via the same helper the popup uses; chip, popup and
   NWS headline agree verbatim. Verified against a live Cochise-County FFW.
2. **Dial and radar clock kept different fallback clocks** (browser tz vs
   longitude estimate) when the forecast was absent → `ddOffset` now delegates
   to the single `placeOffsetSec` chain. One clock, one fallback, everywhere.
3. **Cloud tops on light plates read as masonry** → the r2 cell-overlap (which
   drew a pale lattice) is gone; light plates get a cool grey-blue deck at 0.52
   opacity that reads as vapor over the paper; dark plates keep their material.

Minors: Flash Flood Warning now wears its conventional dark red (green was the
river-flood color — a hazard-class misread); relocating puts the old place's
observations into the pending state instead of leaving them under the new
heading; the mobile dial draws at its real 40 px height (it was scaling to 87%
and floating inside its bar with sub-9 px labels); the radar tag admits
"INKING…" while the visible frame's tiles are still arriving; an alerts-feed
outage shows a muted "warnings unreachable" chip instead of nothing; wind
trails ride a reading ink on light plates (gold-on-cream was ~invisible);
Enter pressed before search results arrive selects the first hit when it
lands; map labels for very long place names truncate with an ellipsis (the
full name stays in the heading); DESIGN.md §0 item 38 records that grain and
vignette are retired by approved design, not regression.

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
- **Round 3** (full matrix, live data): 3 majors / 9 minors, all new — every
  round-1/2 major stayed fixed. Contract: 36 OK, 2 partial, 1 broken (the chip
  clock, fixed), hurricanes still unverifiable (zero storms on Earth).
- **Round 4** (full matrix, live data): **ZERO MAJORS** — 10 all-layer plate
  swaps clean, clocks agree across 7 timezones, alert chip/popup/headline
  agree verbatim, contract 40/41 OK (hurricanes: zero storms on Earth to
  render). 7 minors: 5 fixed, 2 accepted (above).
- **Round 5** (full matrix, live data): **ZERO MAJORS** — second consecutive
  clean round. Loop complete. 5 minors recorded above as follow-ups.
