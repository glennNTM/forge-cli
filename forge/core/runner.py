import subprocess
from rich.console import Console

console = Console()

STDLIB_TEST_LIBS = ["unittest", "doctest", "none"]


def run(command: str, cwd: str = None):
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
    )

    if result.returncode != 0:
        console.print(f"\n[red]Command failed:[/red] {command}")
        raise SystemExit(1)


def run_command(project_name: str, project_type: str, test_library: str):
    console.print(f"\nInitializing project [bold]{project_name}[/bold]...")
    run(f"uv init {project_name}")

    if project_type == "FastAPI":
        console.print("Installing FastAPI and uvicorn...")
        run("uv add fastapi uvicorn", cwd=project_name)

    elif project_type == "Flask":
        console.print("Installing Flask...")
        run("uv add flask", cwd=project_name)

    elif project_type == "Django":
        console.print("Installing Django...")
        run("uv add django", cwd=project_name)
        run("uv run django-admin startproject core .", cwd=project_name)

    if test_library not in STDLIB_TEST_LIBS:
        console.print(f"Installing {test_library}...")
        run(f"uv add {test_library} --dev", cwd=project_name)