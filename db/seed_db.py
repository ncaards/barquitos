from data.seed import all_trails
from db.schema import init
from db.queries import upsert_vessel


def run() -> None:
    init()
    positions = all_trails()
    for pos in positions:
        upsert_vessel(pos)
    unique = len({p.mmsi for p in positions})
    print(f"Seeded {unique} vessels × {len(positions) // unique} trail points each.")


if __name__ == "__main__":
    run()
