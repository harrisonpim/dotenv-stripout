import subprocess
from pathlib import Path
from typing import Union


def strip_line(line: str):
    return line.split("=")[0] + "=\n"


def strip_file(path: Union[Path, str]):
    with open(str(path), "r") as f:
        lines = f.readlines()

    stripped_lines = [strip_line(line) for line in lines]

    with open(str(path), "w") as f:
        f.writelines(stripped_lines)


def get_git_top_level_path():
    try:
        git_top_level_path = subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"], universal_newlines=True
        ).strip()
        return Path(git_top_level_path)
    except subprocess.CalledProcessError:
        raise OSError("Looks like this isn't a git repository!")


def list_dotenv_file_paths():
    git_top_level_path = get_git_top_level_path()
    dotenv_file_paths = map(str, (
        list(git_top_level_path.rglob("*.env")) +
        list(git_top_level_path.rglob("*.env.*"))
    ))
    return dotenv_file_paths
