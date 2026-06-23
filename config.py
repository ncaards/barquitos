from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

AISSTREAM_API_KEY = os.getenv("AISSTREAM_API_KEY", "")
AISSTREAM_WS_URL = "wss://stream.aisstream.io/v0/stream"

SENTINEL_HUB_CLIENT_ID = os.getenv("SENTINEL_HUB_CLIENT_ID", "")
SENTINEL_HUB_CLIENT_SECRET = os.getenv("SENTINEL_HUB_CLIENT_SECRET", "")

LNG_VESSEL_TYPE_CODES = {135, 137, 138}

DARK_VESSEL_GAP_HOURS = 6


@dataclass
class Terminal:
    name: str
    country: str
    lat: float
    lon: float
    radius_km: float = 10.0


LNG_TERMINALS: list[Terminal] = [
    Terminal("Ras Laffan",      "Qatar",       25.897,   51.551),
    Terminal("Sabine Pass",     "USA",         29.731,  -93.874),
    Terminal("Corpus Christi",  "USA",         27.772,  -97.390),
    Terminal("Yamal LNG",       "Russia",      71.009,   68.842),
    Terminal("Arctic LNG 2",    "Russia",      71.500,   68.900),
    Terminal("Bintulu",         "Malaysia",     3.160,  113.044),
    Terminal("Curtis Island",   "Australia",  -23.863,  151.256),
    Terminal("Hammerfest",      "Norway",      70.671,   23.686),
    Terminal("Idku",            "Egypt",       31.311,   30.289),
    Terminal("Bonny",           "Nigeria",      4.440,    7.152),
    Terminal("Tangguh",         "Indonesia",   -2.785,  132.895),
]


@dataclass
class VesselPosition:
    mmsi: str
    name: str
    lat: float
    lon: float
    speed: float
    heading: float
    destination: str
    timestamp: datetime


@dataclass
class PortCall:
    mmsi: str
    terminal: str
    arrived_at: datetime
    departed_at: datetime | None
