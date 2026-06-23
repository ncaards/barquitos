import random
from datetime import datetime, timezone

from config import VesselPosition

_MOCK_VESSELS = [
    ("352435000", "MOZAH",            25.1,  53.2, 135),
    ("538007023", "AL GHARRAFA",      24.5,  56.1, 135),
    ("636022000", "ENERGY FRONTIER",  29.5, -93.6, 135),
    ("477219500", "EXCEL",            22.8,  59.4, 135),
    ("305494000", "ATLANTIC SAIL",    51.2,  -1.3, 135),
    ("304818000", "MERIDIAN SPIRIT",  70.8,  68.5, 135),
    ("229432000", "GASCHEM NORDSEE",  53.5,   8.6, 137),
    ("311045200", "BW MESSINA",        3.4, 113.2, 135),
]


def _jitter(value: float, delta: float = 0.05) -> float:
    return value + random.uniform(-delta, delta)


def current_positions() -> list[VesselPosition]:
    return [
        VesselPosition(
            mmsi=mmsi,
            name=name,
            lat=_jitter(lat),
            lon=_jitter(lon),
            speed=round(random.uniform(0.0, 18.0), 1),
            heading=round(random.uniform(0, 359), 1),
            destination=random.choice(["RAS LAFFAN", "TOKYO", "ROTTERDAM", "SABINE PASS", ""]),
            timestamp=datetime.now(timezone.utc),
        )
        for mmsi, name, lat, lon, _ in _MOCK_VESSELS
    ]
