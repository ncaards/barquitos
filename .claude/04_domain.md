# Domain Knowledge — LNG Vessels

## What we're tracking
LNG (Liquefied Natural Gas) carriers — specialized tankers that transport natural
gas cooled to -162°C. ~700 active vessels globally. Finite, well-documented fleet.

## AIS vessel type codes for LNG
AIS type 135 = LNG Tanker (primary filter)
Some carriers also appear under type 138 (LPG) or 137 — include in filter.
MMSI follows standard 9-digit format. Known LNG fleet lists are publicly available
(e.g., from Clarksons, IHS Markit — exportable as CSV for bootstrapping).

## Why vessels go dark (AIS off)
- **Sanctions evasion**: Russian Yamal/Arctic LNG, Iranian LNG — vessels disable
  AIS before entering or departing sanctioned terminals.
- **Ship-to-ship (STS) transfers**: Two vessels meet at sea to transfer cargo,
  often in international waters away from port. Both commonly go dark.
- **Simple equipment failure**: Less interesting but common.

Dark = AIS gap >6 hours for a vessel that was underway.

## Key LNG terminals to monitor

| Terminal | Country | Lat | Lon | Notes |
|----------|---------|-----|-----|-------|
| Ras Laffan | Qatar | 25.897 | 51.551 | World's largest LNG export hub |
| Sabine Pass | USA | 29.731 | -93.874 | Cheniere — major US export |
| Corpus Christi | USA | 27.772 | -97.390 | Cheniere |
| Yamal LNG | Russia | 71.009 | 68.842 | Sanctions-sensitive |
| Arctic LNG 2 | Russia | 71.500 | 68.900 | Sanctioned, high dark-vessel activity |
| Bintulu | Malaysia | 3.160 | 113.044 | MLNG — major Asian exporter |
| Curtis Island | Australia | -23.863 | 151.256 | APLNG, QCLNG, GLNG |
| Gladstone | Australia | -23.863 | 151.256 | Same precinct as Curtis Island |
| Hammerfest | Norway | 70.671 | 23.686 | Snøhvit LNG |
| Idku | Egypt | 31.311 | 30.289 | Egyptian LNG |
| Bonny | Nigeria | 4.440 | 7.152 | NLNG |
| Tangguh | Indonesia | -2.785 | 132.895 | BP-operated |

## Sentinel-1 SAR for vessel detection
- **Product**: GRD (Ground Range Detected), IW (Interferometric Wide) mode
- **Resolution**: 10m × 10m — large vessels (LNG carriers: 280-345m length) are
  clearly detectable as bright point targets
- **Revisit**: ~6 days at equatorial latitudes, better at higher latitudes
- **Access**: Free via ESA Copernicus / Alaska Satellite Facility (ASF)
- **Processing**: Sentinel Hub API (free tier: 60 processing units/month)
- **Vessel detection model**: SAR-Ship dataset + CFAR (Constant False Alarm Rate)
  detector is the standard open-source approach

## Typical LNG voyage patterns
- Qatar → Japan/Korea/China: 18-22 days transit
- US Gulf → Europe: 8-12 days
- US Gulf → Asia: 18-25 days (via Panama Canal)
- Australia → Japan: 8-12 days
- Russia Yamal → Europe (via Northern Sea Route): 10-18 days, seasonal

Vessels typically idle at anchorages outside major ports waiting for berths.
Idle = speed < 0.5 knots, not at a known terminal.
