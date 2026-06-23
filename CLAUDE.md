# barquitos

Python Dash dashboard for LNG vessel tracking.

## Stack
- **Runtime:** Python 3.12
- **Framework:** Dash + dash-leaflet
- **Package manager:** uv — always use `uv add`, `uv run`, `uv sync`. Never pip.

## Code style
- No comments. Code must be self-documenting through naming.
- Functions and methods stay under 40 lines.
- Follow PEP 8 and idiomatic Python.
- Prefer composition over inheritance. Keep modules focused.

## Git
- Commit at logical checkpoints, not after every file.
- Conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`.

## Running
```bash
uv run python app.py
```
