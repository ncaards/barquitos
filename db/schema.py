import sqlite3
from pathlib import Path

DB_PATH = Path("barquitos.db")


def connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init() -> None:
    with connection() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS vessels (
                mmsi        TEXT PRIMARY KEY,
                name        TEXT,
                updated_at  TEXT
            );

            CREATE TABLE IF NOT EXISTS positions (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                mmsi        TEXT NOT NULL,
                lat         REAL NOT NULL,
                lon         REAL NOT NULL,
                speed       REAL,
                heading     REAL,
                destination TEXT,
                timestamp   TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_positions_mmsi
                ON positions (mmsi, timestamp DESC);
        """)
