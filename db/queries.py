from config import VesselPosition
from db.schema import connection


def upsert_vessel(pos: VesselPosition) -> None:
    with connection() as conn:
        conn.execute(
            "INSERT INTO vessels (mmsi, name, updated_at) VALUES (?, ?, ?)"
            " ON CONFLICT(mmsi) DO UPDATE SET name=excluded.name, updated_at=excluded.updated_at",
            (pos.mmsi, pos.name, pos.timestamp.isoformat()),
        )
        conn.execute(
            "INSERT INTO positions (mmsi, lat, lon, speed, heading, destination, timestamp)"
            " VALUES (?, ?, ?, ?, ?, ?, ?)",
            (pos.mmsi, pos.lat, pos.lon, pos.speed, pos.heading, pos.destination, pos.timestamp.isoformat()),
        )


def latest_positions() -> list[dict]:
    with connection() as conn:
        rows = conn.execute("""
            SELECT p.mmsi, v.name, p.lat, p.lon, p.speed, p.heading, p.destination, p.timestamp
            FROM positions p
            JOIN vessels v USING (mmsi)
            WHERE p.id IN (
                SELECT MAX(id) FROM positions GROUP BY mmsi
            )
            ORDER BY v.name
        """).fetchall()
    return [dict(row) for row in rows]


def position_history(mmsi: str, limit: int = 100) -> list[dict]:
    with connection() as conn:
        rows = conn.execute(
            "SELECT lat, lon, timestamp FROM positions WHERE mmsi = ?"
            " ORDER BY timestamp DESC LIMIT ?",
            (mmsi, limit),
        ).fetchall()
    return [dict(row) for row in rows]
