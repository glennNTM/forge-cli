from rich.console import Console
from rich.prompt import Prompt

console = Console()

PROJECT_TYPES = ["From Scratch", "FastAPI", "Flask", "Django"]
TEST_LIBRARIES = ["pytest", "unittest", "doctest", "none"]


def ask_project_type() -> str:
    console.print("\n[bold]What do you want to create?[/bold]\n")

    for i, project_type in enumerate(PROJECT_TYPES, 1):
        console.print(f"  [{i}] {project_type}")

    console.print()

    choice = Prompt.ask(
        "Select a project type",
        choices=["1", "2", "3", "4"],
        default="1"
    )

    return PROJECT_TYPES[int(choice) - 1]


def ask_test_library() -> str:
    console.print("\n[bold]Which test library do you want to use?[/bold]\n")

    for i, lib in enumerate(TEST_LIBRARIES, 1):
        console.print(f"  [{i}] {lib}")

    console.print()

    choice = Prompt.ask(
        "Select a test library",
        choices=["1", "2", "3", "4"],
        default="1"
    )

    return TEST_LIBRARIES[int(choice) - 1]

def ask_docker() -> bool:
    console.print("\n[bold]Do you want to dockerize your app?[/bold]\n")
    console.print("  [1] Yes")
    console.print("  [2] No")
    console.print()

    choice = Prompt.ask(
        "Select an option",
        choices=["1", "2"],
        default="2"
    )

    return choice