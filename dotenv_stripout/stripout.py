from pathlib import Path
from typing import Union

from .git import get_git_top_level_path

patterns = ["*.env", "*.env.*"]


def strip_line(line: str):
    return line.split("=")[0] + "=\n"


def strip_file(path: Union[Path, str]):
    with open(str(path), "r") as f:
        lines = f.readlines()

    stripped_lines = [strip_line(line) for line in lines]

    with open(str(path), "w") as f:
        f.writelines(stripped_lines)


def list_dotenv_file_paths():
    repo_path = get_git_top_level_path()
    return [
        str(path)
        for pattern in patterns
        for path in list(repo_path.rglob(pattern))
    ]
