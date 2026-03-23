import re
import shutil
import subprocess
from pathlib import Path
from rich.console import Console

console = Console()

STDLIB_TEST_LIBS = ["unittest", "doctest", "none"]


def check_uv_installed():
    if shutil.which("uv") is None:
        console.print("\n[bold red]Error:[/bold red] uv is not installed.")
        console.print("[dim]Install it at https://docs.astral.sh/uv/getting-started/installation/[/dim]\n")
        raise SystemExit(1)


def check_project_exists(project_path: Path):
    if project_path.exists():
        console.print(f"\n[bold red]Error:[/bold red] A folder named [bold]{project_path.name}[/bold] already exists.")
        console.print("[dim]Choose a different project name.[/dim]\n")
        raise SystemExit(1)


def check_project_name(project_name: str):
    if not re.match(r'^[a-zA-Z0-9][a-zA-Z0-9_-]*$', project_name):
        console.print(f"\n[bold red]Error:[/bold red] Invalid project name [bold]{project_name}[/bold].")
        console.print("[dim]Use only letters, numbers, hyphens and underscores. Must start with a letter or number.[/dim]\n")
        raise SystemExit(1)


def run(command: list[str], cwd: Path = None):
    result = subprocess.run(
        command,
        shell=False,
        cwd=cwd,
    )

    if result.returncode != 0:
        console.print(f"\n[bold red]Error:[/bold red] Command failed: {' '.join(command)}\n")
        raise SystemExit(1)


def run_command(project_name: str, project_type: str, test_library: str):
    base_dir = Path.cwd()
    project_path = base_dir / project_name

    check_project_name(project_name)
    check_project_exists(project_path)

    console.print(f"\nInitializing project [bold]{project_name}[/bold]...")
    run(["uv", "init", project_name], cwd=base_dir)

    if project_type == "FastAPI":
        console.print("Installing FastAPI and uvicorn...")
        run(["uv", "add", "fastapi", "uvicorn"], cwd=project_path)

    elif project_type == "Flask":
        console.print("Installing Flask...")
        run(["uv", "add", "flask"], cwd=project_path)

    elif project_type == "Django":
        console.print("Installing Django...")
        run(["uv", "add", "django",  "python-dotenv"], cwd=project_path)
        run(["uv", "run", "django-admin", "startproject", "core", "."], cwd=project_path)

    if test_library not in STDLIB_TEST_LIBS:
        console.print(f"Installing {test_library}...")
        run(["uv", "add", "--dev", test_library], cwd=project_path)