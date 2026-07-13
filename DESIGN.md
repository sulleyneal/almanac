# Almanac visual overhaul — Phase 0 design plan

Status: **awaiting approval** (this is the one stop-and-ask gate).

---

## 0. Regression contract — feature inventory

Everything below works today and must still work when the overhaul lands.
(Compiled from a full read of `index.html`; numbering is the checklist the
critic verifies each round.)

### Map & terrain
1. Five switchable map **editions** — Antique, Midnight, Hydro, Relief, Topo — via the
   top-center switcher; persisted in `localStorage`, honored from `?theme=`, written back
   to the URL with `history.replaceState`.
2. 3-D terrain from terrarium DEM tiles; on/off toggle; height slider 1.0–4.0×.
3. Hillshade with relief-shading slider (0–100%).
4. Browser-generated contour lines (dense variant on Topo); toggle; labels in feet.
5. Hypsometric color-relief layer (Relief edition only).
6. Water glow + waterway width boost (Hydro edition only).
7. Map brightness slider — dark editions only (row hidden on light editions).
8. Full per-edition OSM basemap styling: landcover, landuse, parks, water(+intermittent),
   waterways, aeroways, buildings, road hierarchy w/ casings, rail + hatching, boundaries
   (state/parish/city), road/ref/water/POI/hood/village/town labels.
9. Per-edition sky/fog.
10. Nav control (zoom + pitch), imperial scale (plus metric on desktop), compact attribution.
11. Camera in URL hash (`hash:true`); a shared link's view wins over auto-locate.

### Weather layers
12. **Radar loop** (RainViewer): past 2 h + 30 min nowcast; play/pause; scrubber; frame
    time; PAST/NOW/FORECAST tag; strength slider; 5-min refresh; toggle; clears instantly
    via layer visibility; layers rebuilt after edition swaps; radar controls hidden when
    radar off or no frames. *(Amended in round 3: the bar is now the Day-Dial ephemeris —
    turning radar off folds away only the controls row, the loop window and the frame
    tick; the day strip, sun arc, needle and moon stay. The dial must not be a hostage
    of the radar toggle.)*
13. **Doppler velocity**: nearest WSR-88D N0U via IEM tiles; station auto-switches as you
    pan (~4° radius cutoff); 5-min refresh; toggle.
14. **Cloud tops 3-D**: GOES-East/West / Himawari Band-13 IR decoded pixel-by-pixel,
    extruded columns (height = colder top); rebuilds 500 ms after moveend; 10-min refresh;
    toggle.
15. **Rain, last 24 h 3-D**: Open-Meteo grid sample, bilinear 3× interpolation,
    logarithmic column height (no cap); tap a column → popup with inches + mm; per-view
    hourly cache; toggle.
16. **Wind flow**: particle trails on an overlay canvas riding a bilinearly interpolated
    Open-Meteo 10 m wind grid; tinted from the live accent token; DPR-aware; pauses when
    tab hidden; clears while the map moves; toggle.
17. **NWS alerts**: warning polygons in conventional colors (fill + dashed outline); tap →
    popup with event, headline, "until"; 4-min cache, 10-min refresh; toggle.
18. **Hurricane tracking** (NHC via ArcGIS): cone, observed + forecast tracks, forecast
    positions colored by Saffir-Simpson wind, stage letters, one name label per storm;
    tap a position → popup (name, stage, time, winds, gusts, pressure); active-storm chips
    in the panel; toggle.

### Panel & forecast
19. Place search (Open-Meteo geocoding): 280 ms debounce, dropdown results with admin/country
    sub-line, click to select, Enter = first result, Escape closes, click-outside closes.
20. Place heading: name auto-shrinks when long; sub-line falls back to coordinates.
21. Point alerts: up to 4 NWS chips beneath the place name, event-colored, "until" time.
22. Current conditions: condition emoji + description, temperature, feels-like, wind
    (compass dir, speed, gusts), humidity, pressure in inHg, precip last hour (only when
    > 0), "as of" timestamp + source note.
23. 48-hour chart: temperature line + rain-chance bars (SVG), hi/lo dots + labels,
    12-hourly time ticks ("Now", "6p", weekday at midnight), colors re-derived from live
    theme tokens on every edition swap.
24. Week ahead: 7 rows — Today/weekday, emoji, description, precip-probability max, hi/lo.
25. Sun & moon: sunrise, sunset, daylight duration, UV max, computed moon phase + name +
    illumination %.
26. WMO weather-code interpretation (emoji + label table).
27. Forecast cached per place for 10 min in `localStorage`.
28. "Use my location": panel button + on-map target control (pulse while locating);
    auto-locate on every fresh launch (sessionStorage heuristic) unless a shared-link hash
    is present; declined/failed → saved place stays.
29. Tap the map → forecast at that point ("On the map" + formatted coordinates); ignored
    while drawing and on double-click; popup priority: alert → hurricane point → rain
    column (rain tap also moves the spot).
30. "Return to the full prospect" → flyTo home view.
31. Mobile ≤ 760 px: panel becomes a bottom sheet; flyTo offset keeps the target visible
    above it; radar bar sits above the sheet; edition buttons compact; cartouche hidden.
32. **Draw**: pencil control toggles crosshair sketch mode (dragPan disabled), strokes
    unprojected to lng/lat so they ride the terrain across pan/zoom/edition swaps; bin
    erases all (toast feedback); stray single-point taps dropped.
33. **JPG export**: composites map canvas + wind canvas over the theme bg; dated filename;
    toast errors when a CORS-tainted layer blocks capture.
34. Toast notifications (`role=status`, `aria-live=polite`).
35. Loading veil ("Consulting the almanac…") with 9-s failsafe.
36. Basemap-unreachable warning (`#warn`) on `openmaptiles` source errors.
37. No-WebGL message.
38. Antique extras today: paper grain, vignette, corner cartouche (see open question Q3).
    *(Resolved with the approved plan: grain and vignette deliberately retired — Q3
    answered "retire" — the cartouche kept and redrawn in the new type. Their absence
    is the intended state, not a regression.)*
39. Persisted prefs: edition, place, all four sliders.
40. Credits block with working links; PWA manifest + icons; OG meta.
41. The spot marker (dot + glow on dark editions + uppercase label) follows the chosen place.

### Environment note (blocking)
The remote sandbox denies egress to every data host above except AWS terrain tiles and
Google Fonts. Needed allowlist:
`tiles.openfreemap.org`, `api.open-meteo.com`, `geocoding-api.open-meteo.com`,
`api.rainviewer.com`, `tilecache.rainviewer.com`, `api.weather.gov`,
`gibs.earthdata.nasa.gov`, `mesonet.agron.iastate.edu`, `services9.arcgis.com`.

---

## 1. Self-critique — what the generic version of this plan looks like

For *any* weather app, the autopilot plan is: a big temperature number over a condition
gradient, glassmorphic cards, Inter/Space Grotesk, cyan accent on near-black (or Fraunces
on cream with terracotta), pill toggles, 24-radius everything. The app's current chrome is
*both* of those templates at once: Antique is AI-default (a) — cream + old-style serif +
brick-red accent + fake grain; Midnight/Hydro is AI-default (b) — near-black glass + acid
cyan/green gradient text. So the overhaul deliberately moves off both, and the plan below
was revised against that check:

- **Dropped**: parchment cosplay (grain/vignette overlays), gradient headline text,
  glassmorphism, emoji as primary iconography, two rival chrome personalities.
- **Kept and argued for**: one dark chrome (see palette rationale — it is *not* template
  (b): no acid accent, a two-hue data-ink system, visible structure instead of glass).
- **Changed**: the boldness budget moved from "textures and gradients everywhere" to a
  single signature instrument (the Day-Dial, §4).

## 2. Design direction — "the instrument, not the parchment"

A real almanac is not distressed paper; it is *dense, disciplined reference typography* —
ephemeris tables, ruled columns, numbered sections, figures set in condensed grotesques,
one flash of cover color. The app becomes a bound annual: **one binding (the chrome),
five plates (the map editions)**. The five map palettes stay — they are the product's
best feature — but the UI chrome stops changing personality per edition and becomes the
consistent, recognizable object.

## 3. Palette (chrome; map plates keep their own palettes)

| Name | Hex | Role |
|---|---|---|
| **Iron Gall** | `#212B3A` | chrome ground — blue-black writing ink, not neutral black |
| **Chart Paper** | `#EFECE2` | primary text on ink; table figures |
| **Moon Grey** | `#93A1B4` | secondary text, captions, leader dots |
| **Almanac Gold** | `#E3B341` | the signature: sun arc, NOW needle, focus rings, key figures |
| **Rain Blue** | `#7FB4D9` | precipitation ink — bars, rain figures, moisture data |
| **Hairline** | `#3A4658` | rules, table borders on ink |

Rationale: the chrome must sit legibly over five very different map plates (two dark,
three light) — a single dark binding does that; gold + rain-blue is the classic
almanac/ephemeris pairing (sun and water), not template (b)'s single acid accent.
Alert colors stay NWS-conventional (they are a standard, not a style choice).

## 4. Type

| Slot | Face | Why |
|---|---|---|
| Display | **Besley** (Clarendon revival) | The farmer's-almanac/woodtype vernacular is Clarendons and slabs, not Garamonds. Used with restraint: masthead, place name, section numerals, big figures. |
| Data / tables | **Archivo Narrow** | Almanac tables are condensed grotesques; tabular figures, tight columns, chips, axis labels. |
| Body / UI | **Archivo** | Same family as the data face — one quiet voice for prose and controls, no third personality. |

Pairing rationale: one slab with character + one condensed workhorse from a single
superfamily = "reference annual", and neither is the AI-default serif/geometric pairing.
(Google Fonts, already the app's font channel.)

## 5. Layout concept

The desktop architecture (map dominant, left panel, bottom time bar) survives — it works
and it is the regression-safe skeleton. What changes is what each region *is*: the panel
becomes a typeset almanac page (masthead → date line → place → numbered sections with
ruled, leader-dotted tables), the edition switcher becomes a plate index, and the radar
bar becomes the signature Day-Dial instrument.

```
┌──────────────────────────────────────────────────────────────────────┐
│ ┌ THE ALMANAC ────────┐      PLATES: I·ANTIQUE II·MIDNIGHT …    [nav]│
│ │ Vol. MMXXVI · 13 Jul│                                         [✎🗑]│
│ │ Day 194 · wk 29     │                                         [⤓] │
│ │ RUSTON              │                                              │
│ │ Louisiana, US       │              THE PLATE                       │
│ │ ▐ TORNADO WARNING   │      (3-D terrain map + weather layers)      │
│ │ §1 OBSERVATIONS     │                                              │
│ │  72,1° thunderstorm │                                              │
│ │  wind ‥‥‥‥ SSW 8    │                                              │
│ │  humidity ‥‥‥ 84 %  │                                              │
│ │ §2 NEXT 48 HOURS    │                                              │
│ │  [temp/rain chart]  │                                              │
│ │ §3 THE WEEK AHEAD   │  ┌ DAY-DIAL ───────────────────────────┐     │
│ │ §4 EPHEMERIS        │  │ 00 ▁▁▂▄ sunrise ═ gold arc ═ sunset │     │
│ │ §5 INSTRUMENTS      │  │ ▶ ‥ [radar 2.5h window + scrubber]  │     │
│ │  toggles · sliders  │  │        ▲NOW needle          ☾ 62%   │     │
│ └─────────────────────┘  └─────────────────────────────────────┘     │
└──────────────────────────────────────────────────────────────────────┘
```

Mobile keeps the bottom-sheet pattern; the Day-Dial compresses to sun-arc + scrubber.

## 6. Signature element — the Day-Dial

The existing radar bar (play/pause, scrubber, time, PAST/NOW/FORECAST) is reborn as a
**24-hour ephemeris strip** under the map: the full day as a ruler, night shaded in ink,
daylight spanned by a thin **gold sun arc** drawn from the *real* sunrise/sunset of the
chosen place, moon phase and illumination at its end, and the radar's ~2.5-hour loop
window inset as the scrubbable segment with a gold NOW needle. Every existing control
keeps working — it just gains the time-of-day context an almanac exists to provide.
This is the one place the design spends boldness; everything else is quiet tables.
Why it embodies "almanac": the ephemeris (sun/moon rise-set arithmetic) *is* the
historical heart of an almanac page — here it is drawn from live data and made the
app's primary instrument.

## 7. Weather-state theming — deliberate restraint

The five map plates already carry the weather drama (radar, cloud columns, alert
polygons), and the plate palette is user-chosen — chrome that *also* repainted itself per
condition would be noise. The chrome responds only with small, ink-like annotations:

- **Alert over the chosen place** → the masthead rule and the place name's underline take
  the NWS event color; chips as today.
- **Night** (after local sunset) → the Day-Dial's needle rides the ink section; a small
  ☾ replaces ☀ beside the clock. No global palette swap — the plates have Midnight for that.
- **Freeze** (≤ 32 °F) → the §1 temperature figure gets a Rain Blue frost tick + "below
  freezing" note; **heat** (≥ 100 °F) → Almanac Gold tick.
- **Storm** → nothing extra in the chrome; the radar window in the Day-Dial and the alert
  rubric already say it.

## 8. Quality floor (built in, verified by the critic)

360 px layout, visible `:focus-visible` rings (Almanac Gold), `prefers-reduced-motion`
(radar loop starts paused, flyTo → jumpTo, wind stays opt-in), AA contrast on every
text/ground pair, no layout shift as data arrives (sections get reserved skeleton heights),
no horizontal scroll.

---

## Open questions (front-loaded)

- **Q1 — blocking:** the sandbox egress policy denies all weather/basemap hosts (list in
  §0). The critic loop is impossible without them. Please allowlist those domains in this
  environment's network policy (Claude Code → environment → network), or tell me to
  proceed blind (I'd argue against — it violates the "real data" rule).
- **Q2:** Approve the core call: five map plates keep their palettes, but the *chrome*
  unifies into the single Iron-Gall binding above (today the chrome swaps between a serif
  parchment UI and a glass cyan UI per edition)?
- **Q3:** Antique's paper-grain + vignette overlays: retire (my recommendation — they are
  template-(a) cosplay and cost GPU), or keep as an Antique-only plate effect? The corner
  cartouche I'd keep, redrawn in the new type.
- **Q4:** Emoji as weather icons (☀️/🌧 etc.) — replace with a drawn, single-weight glyph
  set matching the chrome (recommendation), or keep emoji?
