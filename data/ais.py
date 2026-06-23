import asyncio
import json
import logging
from collections.abc import Callable
from datetime import datetime, timezone

import websockets

from config import AISSTREAM_API_KEY, AISSTREAM_WS_URL, LNG_VESSEL_TYPE_CODES, VesselPosition

logger = logging.getLogger(__name__)


def _build_subscription(bounding_boxes: list[list[list[float]]]) -> dict:
    return {
        "APIKey": AISSTREAM_API_KEY,
        "BoundingBoxes": bounding_boxes,
        "FilterMessageTypes": ["PositionReport"],
    }


def _parse_position(message: dict) -> VesselPosition | None:
    meta = message.get("MetaData", {})
    position = message.get("Message", {}).get("PositionReport", {})

    ship_type = meta.get("ShipType", 0)
    if ship_type not in LNG_VESSEL_TYPE_CODES:
        return None

    return VesselPosition(
        mmsi=str(meta.get("MMSI", "")),
        name=meta.get("ShipName", "").strip(),
        lat=meta.get("latitude", 0.0),
        lon=meta.get("longitude", 0.0),
        speed=position.get("Sog", 0.0),
        heading=position.get("Cog", 0.0),
        destination=meta.get("Destination", "").strip(),
        timestamp=datetime.now(timezone.utc),
    )


async def _stream(on_position: Callable[[VesselPosition], None]) -> None:
    bounding_boxes = [[[-90, -180], [90, 180]]]
    subscription = _build_subscription(bounding_boxes)

    async with websockets.connect(AISSTREAM_WS_URL) as ws:
        await ws.send(json.dumps(subscription))
        logger.info("AIS stream connected")

        async for raw in ws:
            message = json.loads(raw)
            position = _parse_position(message)
            if position:
                on_position(position)


async def stream_with_reconnect(on_position: Callable[[VesselPosition], None]) -> None:
    backoff = 5
    while True:
        try:
            await _stream(on_position)
        except Exception as e:
            logger.warning("AIS stream disconnected: %s — reconnecting in %ds", e, backoff)
            await asyncio.sleep(backoff)
            backoff = min(backoff * 2, 60)
        else:
            backoff = 5
