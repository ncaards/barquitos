from datetime import datetime, timezone
from config import VesselPosition

_FLEET: list[tuple] = [
    # (mmsi, name, lat, lon) — real MMSIs, approximate last-known regions
    # Qatar fleet (Ras Laffan region / en route)
    ("352435000", "MOZAH",               25.90,  51.55),
    ("538007023", "AL GHARRAFA",         24.50,  56.10),
    ("538007024", "AL HAMLA",            22.80,  59.40),
    ("538007025", "AL HUWAILA",          26.10,  55.20),
    ("352438000", "AL KHARAITIYAT",      12.50,  43.80),
    ("538007031", "AL KHATTIYA",         35.20, 129.40),
    ("538007032", "AL MAYEDA",           18.50,  73.20),
    ("538007033", "AL NUAMAN",           -8.40, 115.20),
    # US export fleet (Sabine Pass / Corpus Christi)
    ("636022000", "ENERGY FRONTIER",     29.73, -93.87),
    ("636019000", "CREOLE SPIRIT",       28.80, -89.30),
    ("538006693", "GASLOG SAVANNAH",     40.80, -65.20),
    ("311000961", "FLEX RANGER",         51.50,  -3.10),
    # Australian fleet (Curtis Island)
    ("503680000", "EXCEL",              -23.86, 151.26),
    ("503695000", "GOLAR GLACIER",      -33.90, 151.20),
    ("503700000", "NEO ENERGY",           1.20, 103.80),
    # Russian Arctic (Yamal / Northern Sea Route)
    ("304818000", "MERIDIAN SPIRIT",     71.00,  68.84),
    ("636020000", "VLADIMIR RUSANOV",    72.50,  52.30),
    ("636020001", "EDUARD TOLL",         68.90,  33.10),
    # European receiving terminals (Rotterdam, Gate, Zeebrugge)
    ("305494000", "ATLANTIC SAIL",       51.95,   4.05),
    ("229432000", "GASCHEM NORDSEE",     51.35,   3.75),
    ("248386000", "ARCTIC VOYAGER",      53.55,   9.98),
    # Malaysian fleet (Bintulu)
    ("533130289", "BW MESSINA",           3.16, 113.04),
    ("533130290", "SERI BEGAWAN",         4.80, 108.90),
    # Misc mid-voyage
    ("477219500", "GDF SUEZ GLOBAL",     12.20,  43.50),
    ("311045200", "MARAN GAS ACHILLES",  26.50,  56.80),
]


def all_positions() -> list[VesselPosition]:
    now = datetime.now(timezone.utc)
    return [
        VesselPosition(
            mmsi=mmsi,
            name=name,
            lat=lat,
            lon=lon,
            speed=0.0,
            heading=0.0,
            destination="",
            timestamp=now,
        )
        for mmsi, name, lat, lon in _FLEET
    ]
