# Visual overhaul — progress

**Round:** 0 (Phase 0 — design plan)
**State:** ⏸ Awaiting (1) plan approval and (2) a network-policy fix — see below.

## Done
- Full codebase read; regression contract compiled (41 items — `DESIGN.md` §0).
- Design plan drafted, self-critiqued against the generic-weather-app template
  and the three AI-design defaults (`DESIGN.md`).

## Blocked
The remote environment's egress policy denies every data host the app uses, so the app
cannot render real data here — which the house rules and the critic loop require.
Reachable: AWS terrain tiles, Google Fonts. **Denied:** `tiles.openfreemap.org`,
`api.open-meteo.com`, `geocoding-api.open-meteo.com`, `api.rainviewer.com`,
`tilecache.rainviewer.com`, `api.weather.gov`, `gibs.earthdata.nasa.gov`,
`mesonet.agron.iastate.edu`, `services9.arcgis.com`.
Fix: allowlist these in the Claude Code environment's network policy, then re-prompt.

## Next (on approval)
Round 1 build: font swap (Besley/Archivo/Archivo Narrow), Iron-Gall chrome tokens,
panel-as-page typography, Day-Dial instrument, quality floor. Then first critic pass.

## Critic findings
None yet — no build rounds run.
