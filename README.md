# The Almanac

A living weather chart — forecast and animated radar drawn over 3-D terrain, in five
switchable editions: **Antique**, **Midnight**, **Hydro**, **Relief** and **Topo**.
The foundation (theme system, conditions card, vendored MapLibre setup) is ported from
[sulleyneal/Maps](https://github.com/sulleyneal/Maps).

## What it does

- **Radar loop** — the last two hours plus a 30-minute nowcast from
  [RainViewer](https://www.rainviewer.com/), draped over the terrain. Play/pause and
  scrub with the bar beneath the map. (RainViewer's public cache serves one fixed
  palette up to z7; the chart shares those tiles across all editions and overzooms
  past z7.)
- **Cloud tops in 3-D** — the latest GOES-East/West or Himawari "clean infrared"
  imagery from [NASA GIBS](https://www.earthdata.nasa.gov/) (no key), decoded
  pixel-by-pixel in the browser and lofted into an extruded cloud deck — the colder
  the top, the taller the column (flat decks ~2 km, overshooting storm tops ~15 km).
  Rebuilds as you pan; refreshes every ten minutes.
- **Rain, last 24 h in 3-D** — a grid of points across the view is sampled from
  Open-Meteo's hourly precipitation (past day), and each wet cell raises a column
  from the ground — height and color deepen with accumulation (~1 km for a trace,
  ~15 km for 75 mm+). Hairline gaps between columns; rebuilds as you pan.
- **Forecast** — current conditions, a 48-hour temperature/rain-chance chart, the week
  ahead, and sun & moon, all from [Open-Meteo](https://open-meteo.com/) (no key).
- **Anywhere** — search any place on Earth, use your location, or tap the map for the
  forecast at that point. The last place and edition are remembered.
- **Terrain** — 3-D relief, hillshade and browser-generated contours from USGS/SRTM
  elevation tiles, with height/shading sliders.

Open with `?theme=antique|midnight|hydro|relief|topo`, or switch live in the chart.

## Viewing

Open `index.html` in any modern browser — an internet connection is required for the
map and weather data, but there is no build step, no API keys, and no accounts.

```sh
# or serve it locally:
python3 -m http.server 8000   # then visit http://localhost:8000
```

## How it's made

| Ingredient | Source |
|---|---|
| Streets, water, rail, names | [OpenStreetMap](https://www.openstreetmap.org/copyright) vector tiles served by [OpenFreeMap](https://openfreemap.org) (no key, no limits) |
| Elevation (3-D terrain, hillshade) | [Terrain Tiles on AWS](https://registry.opendata.aws/terrain-tiles/) — USGS 3DEP / SRTM, Mapzen terrarium encoding |
| Contour lines | Generated in the browser from the same DEM by [maplibre-contour](https://github.com/onthegomap/maplibre-contour) |
| Radar | [RainViewer public API](https://www.rainviewer.com/api.html) (past 2 h + nowcast, no key) |
| Cloud tops | GOES-East/West & Himawari Band 13 infrared via [NASA GIBS](https://www.earthdata.nasa.gov/) WMTS (no key) |
| Forecast, geocoding | [Open-Meteo](https://open-meteo.com/) (no key) |
| Rendering | [MapLibre GL JS](https://maplibre.org) with hand-written styles (vendored in `vendor/`) |
| Typefaces | EB Garamond, IM Fell English, Inter & Space Grotesk via Google Fonts |

Map data © OpenStreetMap contributors (ODbL). Elevation data courtesy USGS and NASA.
Radar data © RainViewer. Forecast data © Open-Meteo (CC BY 4.0).
