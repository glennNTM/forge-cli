import os
from rich.console import Console

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


def write_file(path: str, content: str):
    with open(path, "w") as f:
        f.write(content)
    console.print(f"  Created [bold]{path}[/bold]")


def create_template(project_name: str, project_type: str, test_library: str):
    console.print("\nGenerating project files...")

    if project_type == "From Scratch":
        write_file(f"{project_name}/main.py", SCRATCH_MAIN)

    elif project_type == "FastAPI":
        write_file(f"{project_name}/main.py", FASTAPI_MAIN)

    elif project_type == "Flask":
        write_file(f"{project_name}/app.py", FLASK_APP)

    elif project_type == "Django":
        # Django genere ses fichiers via django-admin, rien a ajouter
        pass

    if test_library not in ["none"]:
        tests_dir = f"{project_name}/tests"
        os.makedirs(tests_dir, exist_ok=True)
        write_file(f"{tests_dir}/__init__.py", "")
        write_file(f"{tests_dir}/test_main.py", f"# {test_library} tests\n")

    console.print("\n[bold green]Project created successfully.[/bold green]")
    _print_next_steps(project_name, project_type)


def _print_next_steps(project_name: str, project_type: str):
    console.print("\nNext steps:\n")
    console.print(f"  cd {project_name}")

    if project_type == "FastAPI":
        console.print("  uv run uvicorn main:app --reload")

    elif project_type == "Flask":
        console.print("  uv run python app.py")

    elif project_type == "Django":
        console.print("  uv run python manage.py runserver")

    elif project_type == "From Scratch":
        console.print("  uv run python main.py")

    console.print()