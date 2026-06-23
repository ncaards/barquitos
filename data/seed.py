import math
from datetime import datetime, timezone, timedelta

from config import VesselPosition

_FLEET: list[tuple] = [
    # (mmsi, name, lat, lon, heading, speed_kn, destination)
    ("352435000", "MOZAH",              25.90,  51.55,  95, 15.8, "YOKOHAMA"),
    ("538007023", "AL GHARRAFA",        24.50,  56.10,  72, 14.1, "INCHEON"),
    ("538007024", "AL HAMLA",           22.80,  59.40, 110,  0.2, "WAITING"),
    ("538007025", "AL HUWAILA",         26.10,  55.20, 278,  0.3, "RAS LAFFAN"),
    ("352438000", "AL KHARAITIYAT",     12.50,  43.80, 340, 16.5, "BARCELONA"),
    ("538007031", "AL KHATTIYA",        35.20, 129.40, 215,  9.1, "OSAKA"),
    ("538007032", "AL MAYEDA",          18.50,  73.20,  85, 17.2, "DAHEJ"),
    ("538007033", "AL NUAMAN",          -8.40, 115.20, 340, 13.8, "TOKYO"),
    ("636022000", "ENERGY FRONTIER",    29.73, -93.87, 155,  0.4, "LOADING"),
    ("636019000", "CREOLE SPIRIT",      28.80, -89.30,  80, 18.1, "ROTTERDAM"),
    ("538006693", "GASLOG SAVANNAH",    40.80, -65.20,  45, 16.4, "GATE TERMINAL"),
    ("311000961", "FLEX RANGER",        51.50,  -3.10, 175,  0.2, "MILFORD HAVEN"),
    ("503680000", "EXCEL",             -23.86, 151.26,   5,  0.3, "UNLOADING"),
    ("503695000", "GOLAR GLACIER",     -33.90, 151.20, 310, 14.9, "INCHEON"),
    ("503700000", "NEO ENERGY",          1.20, 103.80, 270, 11.3, "DAHEJ"),
    ("304818000", "MERIDIAN SPIRIT",    71.00,  68.84, 245, 14.6, "ZEEBRUGGE"),
    ("636020000", "VLADIMIR RUSANOV",   72.50,  52.30, 290, 16.1, "ROTTERDAM"),
    ("636020001", "EDUARD TOLL",        68.90,  33.10, 270,  0.2, "MURMANSK"),
    ("305494000", "ATLANTIC SAIL",      51.95,   4.05,  90,  0.3, "GATE TERMINAL"),
    ("229432000", "GASCHEM NORDSEE",    51.35,   3.75, 200, 10.4, "MONTOIR"),
    ("248386000", "ARCTIC VOYAGER",     53.55,   9.98, 265, 12.8, "SABINE PASS"),
    ("533130289", "BW MESSINA",          3.16, 113.04,  75, 15.7, "TOKYO"),
    ("533130290", "SERI BEGAWAN",        4.80, 108.90,  40,  0.4, "BINTULU"),
    ("477219500", "GDF SUEZ GLOBAL",    12.20,  43.50, 330, 17.3, "BARCELONA"),
    ("311045200", "MARAN GAS ACHILLES", 26.50,  56.80,  95, 16.0, "OSAKA"),
]

_STEP_HOURS = 3
_TRAIL_POINTS = 10


def _step_backward(lat: float, lon: float, heading_deg: float, knots: float) -> tuple[float, float]:
    distance_km = knots * 1.852 * _STEP_HOURS
    bearing_rad = math.radians((heading_deg + 180) % 360)
    delta_lat = (distance_km / 111.0) * math.cos(bearing_rad)
    delta_lon = (distance_km / (111.0 * math.cos(math.radians(lat)))) * math.sin(bearing_rad)
    return lat + delta_lat, lon + delta_lon


def _trail(mmsi: str, name: str, lat: float, lon: float,
           heading: int, speed: float, destination: str) -> list[VesselPosition]:
    positions = []
    now = datetime.now(timezone.utc)
    curr_lat, curr_lon = lat, lon
    effective_speed = max(speed, 12.0)

    for i in range(_TRAIL_POINTS):
        positions.append(VesselPosition(
            mmsi=mmsi, name=name,
            lat=curr_lat, lon=curr_lon,
            speed=speed if i == 0 else effective_speed,
            heading=float(heading),
            destination=destination,
            timestamp=now - timedelta(hours=i * _STEP_HOURS),
        ))
        curr_lat, curr_lon = _step_backward(curr_lat, curr_lon, heading, effective_speed)

    return positions


def all_positions() -> list[VesselPosition]:
    return [
        VesselPosition(
            mmsi=mmsi, name=name,
            lat=lat, lon=lon,
            speed=float(speed), heading=float(heading),
            destination=destination,
            timestamp=datetime.now(timezone.utc),
        )
        for mmsi, name, lat, lon, heading, speed, destination in _FLEET
    ]


def all_trails() -> list[VesselPosition]:
    positions = []
    for row in _FLEET:
        positions.extend(_trail(*row))
    return positions
