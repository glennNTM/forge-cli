# 🔥 Forge CLI

> Modern Python project scaffolding — inspired by Laravel Artisan & create-next-app.

Forge CLI lets you spin up Python projects in seconds with an interactive, guided experience.

## ✨ Features

- Interactive project type selection
- Built-in support for **FastAPI**, **Flask**, **Django** and bare Python
- Powered by [`uv`](https://github.com/astral-sh/uv) for fast dependency management
- Beautiful terminal UI with [`Rich`](https://github.com/Textualize/rich)

## 🚀 Installation

> Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/getting-started/installation/)
```bash
uv tool install forge-cli
```

## 📦 Usage
```bash
forge new my_project
```

## 🛠️ Dev setup
```bash
git clone https://github.com/<username>/forge-cli
cd forge-cli
uv sync
uv pip install -e .
```

## 📋 Roadmap

- [ ] `From Scratch` template
- [ ] `FastAPI` template
- [ ] `Flask` template
- [ ] `Django` template
- [ ] Docker support
- [ ] Auth boilerplate
- [ ] Plugin system

## 📄 License

MIT