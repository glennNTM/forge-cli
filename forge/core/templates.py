from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


FASTAPI_MAIN = """\
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from Forge CLI"}
"""

FLASK_APP = """\
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {"message": "Hello from Forge CLI"}


if __name__ == "__main__":
    app.run(debug=True)
"""

SCRATCH_MAIN = """\
def main():
    print("Hello from Forge CLI")


if __name__ == "__main__":
    main()
"""

ENV_SCRATCH = """\
APP_ENV=development
DEBUG=true
"""

ENV_FASTAPI = """\
APP_ENV=development
DEBUG=true
HOST=127.0.0.1
PORT=8000
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
"""

ENV_FLASK = """\
APP_ENV=development
FLASK_APP=app.py
FLASK_ENV=development
DEBUG=true
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
"""

ENV_DJANGO = """\
APP_ENV=development
DEBUG=true
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
"""



def write_file(path: Path, content: str):
    path.write_text(content, encoding="utf-8")
    console.print(f"  Created [bold]{path}[/bold]")


def create_template(project_name: str, project_type: str, test_library: str):
    project_path = Path.cwd() / project_name

    console.print("\nGenerating project files...")

    if project_type == "From Scratch":
        write_file(project_path / "main.py", SCRATCH_MAIN)

    elif project_type == "FastAPI":
        write_file(project_path / "main.py", FASTAPI_MAIN)

    elif project_type == "Flask":
        write_file(project_path / "app.py", FLASK_APP)

    elif project_type == "Django":
        pass

    if test_library != "none":
        tests_dir = project_path / "tests"
        tests_dir.mkdir(exist_ok=True)
        write_file(tests_dir / "__init__.py", "")
        write_file(tests_dir / "test_main.py", f"# {test_library} tests\n")

    env_templates = {
        "From Scratch": ENV_SCRATCH,
        "FastAPI": ENV_FASTAPI,
        "Flask": ENV_FLASK,
        "Django": ENV_DJANGO,
    }

    write_file(project_path / ".env.example", env_templates[project_type])

    _print_next_steps(project_name, project_type)


def _print_next_steps(project_name: str, project_type: str):
    if project_type == "FastAPI":
        run_cmd = "uv run uvicorn main:app --reload"
    elif project_type == "Flask":
        run_cmd = "uv run python app.py"
    elif project_type == "Django":
        run_cmd = "uv run python manage.py runserver"
    else:
        run_cmd = "uv run python main.py"

    content = Text()
    content.append("Project created successfully.\n\n", style="bold green")
    content.append("Next steps:\n\n", style="bold white")
    content.append(f"  cd {project_name}\n", style="bright_cyan")
    content.append(f"  {run_cmd}\n", style="bright_cyan")

    console.print(Panel(
        content,
        border_style="green",
        padding=(1, 4),
    ))