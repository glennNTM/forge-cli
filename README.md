# Forge CLI

A command-line tool for scaffolding Python projects.

## Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Dev setup
```bash
git clone https://github.com/<username>/forge-cli
cd forge-cli
uv sync
uv pip install -e .
```

## Usage
```bash
forge new my_project
```

Follow the interactive prompts to select:
- Project type: From Scratch, FastAPI, Flask or Django
- Test library: pytest, unittest, doctest or none

## License

MIT