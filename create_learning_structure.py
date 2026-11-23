
from pathlib import Path
import argparse

PHASES = {
    "phase-01-python-foundations": {
        "name": "Python Foundations",
        "days": [
            "introduction-to-python",
            "variables-and-data-types",
            "strings-and-string-methods",
            "numbers-and-operators",
            "user-input-and-type-conversion",
            "conditional-statements",
            "logical-and-comparison-operators",
            "loops",
            "functions",
            "function-arguments-and-return-values",
        ],
    },
    "phase-02-core-python": {
        "name": "Core Python",
        "days": [
            "lists-and-tuples",
            "dictionaries-and-sets",
            "list-comprehensions",
            "file-handling",
            "exception-handling",
            "modules-and-packages",
            "working-with-json",
            "debugging-and-logging",
            "object-oriented-programming",
            "classes-and-inheritance",
        ],
    },
    "phase-03-developer-skills": {
        "name": "Developer Skills",
        "days": [
            "git-and-github",
            "virtual-environments-and-pip",
            "unit-testing-with-pytest",
            "clean-code-and-refactoring",
            "algorithms-and-complexity",
            "searching-and-sorting",
            "recursion",
            "data-structures",
            "working-with-apis",
            "mini-project",
        ],
    },
    "phase-04-practical-python": {
        "name": "Practical Python",
        "days": [
            "http-and-rest-apis",
            "requests-and-api-integration",
            "sql-and-databases",
            "sqlite-with-python",
            "automation-basics",
            "web-scraping-concepts",
            "application-architecture",
            "configuration-and-environment-variables",
            "security-fundamentals",
            "integration-project",
        ],
    },
    "phase-05-capstone": {
        "name": "Capstone and Review",
        "days": [
            "project-planning",
            "requirements-and-design",
            "implementation-part-one",
            "implementation-part-two",
            "testing-and-debugging",
        ],
    },
}

FILES = {
    "README.md": "# Python 45-Day Learning Journey\n\nMy structured journey to becoming a capable software engineer.\n",
    ".gitignore": ".venv/\n__pycache__/\n*.py[cod]\n.pytest_cache/\n.ruff_cache/\n.env\n.DS_Store\n",
    "requirements.txt": "pytest\nruff\n",
    "resources/books.md": "# Books and Reading Notes\n",
    "resources/courses.md": "# Courses and Tutorials\n",
    "resources/useful-links.md": "# Useful Development Resources\n",
    "journal/learning-journal.md": "# Learning Journal\n",
    "projects/README.md": "# Projects\n",
    "tests/README.md": "# Test Suite\n",
    "capstone/README.md": "# Capstone Project\n",
}


def create_file(path: Path, content: str, force: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and not force:
        print(f"Preserved existing file: {path}")
        return

    path.write_text(content, encoding="utf-8")
    print(f"Created: {path}")


def create_structure(root: Path, force: bool) -> None:
    root.mkdir(parents=True, exist_ok=True)

    for relative_path, content in FILES.items():
        create_file(root / relative_path, content, force)

    for phase_folder, phase in PHASES.items():
        phase_path = root / phase_folder
        phase_path.mkdir(parents=True, exist_ok=True)

        for index, topic in enumerate(phase["days"], start=1):
            day_number = sum(
                len(p["days"])
                for name, p in PHASES.items()
                if list(PHASES).index(name) < list(PHASES).index(phase_folder)
            ) + index

            day_folder = (
                phase_path
                / f"day-{day_number:02d}-{topic}"
            )

            create_file(
                day_folder / "README.md",
                f"# Day {day_number}: {topic.replace('-', ' ').title()}\n\n"
                "## Learning objectives\n\n"
                "## Concepts\n\n"
                "## Exercises\n\n"
                "## Completion checklist\n",
                force,
            )

            create_file(
                day_folder / "main.py",
                '"""Main practice file for this lesson."""\n\n'
                'print("Day lesson started!")\n',
                force,
            )

            create_file(
                day_folder / "exercises.py",
                '"""Exercises for this lesson."""\n',
                force,
            )

            create_file(
                day_folder / "notes.md",
                f"# Day {day_number} Notes\n",
                force,
            )

            create_file(
                day_folder / "test_main.py",
                '"""Tests for this lesson."""\n',
                force,
            )

    print("\nLearning workspace created successfully!")
    print(f"Location: {root.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Create the Python 45-day learning workspace."
    )
    parser.add_argument(
        "--path",
        default="python-45-days",
        help="Destination folder",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing generated starter files",
    )

    args = parser.parse_args()
    create_structure(Path(args.path), args.force)


if __name__ == "__main__":
    main()
