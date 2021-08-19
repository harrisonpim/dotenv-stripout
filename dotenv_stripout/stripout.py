import sys

from .git import get_git_top_level_path

patterns = ["*.env", "*.env.*"]


def list_dotenv_file_paths():
    repo_path = get_git_top_level_path()
    return [
        path for pattern in patterns for path in list(repo_path.rglob(pattern))
    ]


def strip_line(line, newline=""):
    line = line.strip()
    if len(line) > 0:
        line = line.split("=")[0] + f"={newline}"
    return line


def strip_lines(lines, newline=""):
    return [strip_line(line, newline=newline) for line in lines]


def strip_file(path):
    with path.open("r") as f:
        lines = f.readlines()
    stripped_lines = strip_lines(lines, newline="\n")
    with path.open("w") as f:
        f.writelines(stripped_lines)


def strip_stdin():
    for line in sys.stdin:
        sys.stdout.write(strip_line(line, newline="\n"))
