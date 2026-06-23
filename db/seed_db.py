from data.seed import all_positions
from db.schema import init
from db.queries import upsert_vessel


def run() -> None:
    init()
    positions = all_positions()
    for pos in positions:
        upsert_vessel(pos)
    print(f"Seeded {len(positions)} LNG vessels.")


if __name__ == "__main__":
    run()
