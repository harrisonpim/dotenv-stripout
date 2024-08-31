import sys
from typing import Union
from pathlib import Path
from .git import get_git_top_level_path

patterns = ["*.env", "*.env.*"]
ignore_file = ".dotenv-stripout-ignore"


def list_ignored_files() -> set:
    """
    Get the set of local .env files to leave unstripped

    Files to be left unstripped are listed in .dotenv-stripout-ignore files,
    which can be present in any directory.

    :return set: A set of paths to the .env files which dotenv-stripout should ignore
    """
    ignored_files = set()
    repo_path = get_git_top_level_path()
    dotenv_stripout_ignore_file_paths = repo_path.rglob(ignore_file)
    ignore_patterns = []
    for file_path in dotenv_stripout_ignore_file_paths:
        with file_path.open("r") as f:
            for line in f:
                if line.strip():
                    ignore_patterns.append(line.strip())

    for pattern in ignore_patterns:
        ignored_files.update(
            [
                path
                for path in repo_path.rglob(pattern)
                if path.name not in ignored_files
            ]
        )

    return ignored_files


def list_dotenv_file_paths() -> list:
    """
    List all dotenv files in the repo, excluding those in .dotenv-stripout-ignore

    :return list: A list of paths to dotenv files to strip
    """
    repo_path = get_git_top_level_path()
    return [
        path
        for pattern in patterns
        for path in repo_path.rglob(pattern)
        if path not in list_ignored_files()
    ]


def strip_line(line: str, newline: str = "") -> str:
    """
    Strip the value from a line of a dotenv file

    :param str line: The line to strip
    :param str newline: The newline character to use, defaults to ""
    :return str: The stripped line
    """
    line = line.strip()
    if len(line) > 0:
        if line.startswith("#"):
            return line + newline
        else:
            line = line.split("=")[0] + f"={newline}"
    return line


def strip_lines(lines: list[str], newline: str = "") -> list[str]:
    """
    Strip the values from a list of lines of a dotenv file

    :param list[str] lines: The lines to strip
    :param str newline: The newline character to use, defaults to ""
    :return list[str]: The stripped lines
    """
    return [strip_line(line, newline=newline) for line in lines]


def strip_file(path: Union[Path, str]):
    """
    Strip the values from a dotenv file

    :param Union[Path, str] path: The path to the dotenv file
    """
    with path.open("r") as f:
        lines = f.readlines()
    stripped_lines = strip_lines(lines, newline="\n")
    with path.open("w") as f:
        f.writelines(stripped_lines)


def strip_stdin():
    """Strip the values a dotenv file provided via stdin"""
    for line in sys.stdin:
        sys.stdout.write(strip_line(line, newline="\n"))
