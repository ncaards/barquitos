# Code Standards

## Core principles
- Code is read more than written. Optimize for the reader.
- If a name needs a comment to explain it, rename it.
- A function that needs a docstring to explain what it does is too complex.

## Functions and modules
- Max 40 lines per function. No exceptions.
- One responsibility per function. If you're using "and" to describe it, split it.
- Prefer returning values over mutating state.
- No commented-out code. Use git to recover old code.

## Python specifics
- Type hints on all function signatures.
- Use dataclasses or Pydantic models for structured data — no raw dicts across module boundaries.
- Prefer `pathlib.Path` over `os.path`.
- Use `match` for multi-branch dispatch (Python 3.10+).
- Generator expressions over list comprehensions when the result isn't needed immediately.
- Never use mutable default arguments.

## Comments
- Zero comments by default.
- Only add a comment when the WHY is genuinely non-obvious: a hidden constraint, an API quirk, a workaround for a known bug.
- Never comment WHAT the code does — well-named code already does that.

## Naming
- Variables and functions: `snake_case`, descriptive nouns/verbs.
- No abbreviations unless domain-standard (e.g., `mmsi`, `ais`, `sar`).
- Boolean variables and functions: prefix with `is_`, `has_`, `can_`.
- Collections: plural (`vessels`, `positions`, `terminals`).

## Error handling
- Only handle errors at system boundaries (WebSocket, HTTP, file I/O, DB).
- Let internal errors propagate — don't swallow exceptions with bare `except`.
- Use specific exception types, never `except Exception`.

## Git
- Conventional commits: `feat:`, `fix:`, `chore:`, `refactor:`, `docs:`.
- Commit at logical checkpoints — a working unit, not a file save.
- Branch names: `feat/phase-1-live-map`, `fix/ais-reconnect`, etc.
- Never commit `.env`, credentials, or `.venv/`.

## Packages
- uv only. Never pip, pipenv, or poetry.
- `uv add <package>` to add dependencies.
- `uv sync` to reproduce the environment from `uv.lock`.
- `uv run python app.py` to run without activating the venv manually.
