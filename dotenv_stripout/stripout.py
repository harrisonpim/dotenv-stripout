import sys

from .git import get_git_top_level_path

patterns = ["*.env", "*.env.*"]
ignore_file = ".dotenv-stripout-ignore"


def get_ignored_files():
    repo_path = get_git_top_level_path()
    ignore_file_path = repo_path / ignore_file
    if ignore_file_path.exists():
        with ignore_file_path.open("r") as f:
            return {line.strip() for line in f if line.strip()}
    return set()


def list_dotenv_file_paths():
    repo_path = get_git_top_level_path()
    ignored_files = get_ignored_files()
    return [
        path
        for pattern in patterns
        for path in repo_path.rglob(pattern)
        if path.name not in ignored_files
    ]


def strip_line(line, newline=""):
    line = line.strip()
    if len(line) > 0:
        if line.startswith("#"):
            return line + newline
        else:
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
