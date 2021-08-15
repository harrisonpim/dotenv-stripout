from .git import get_git_top_level_path

patterns = ["*.env", "*.env.*"]


def list_dotenv_file_paths():
    repo_path = get_git_top_level_path()
    return [
        path for pattern in patterns for path in list(repo_path.rglob(pattern))
    ]


def strip_line(line):
    line = line.strip()
    if len(line) > 0:
        line = line.split("=")[0] + "=\n"
    return line


def strip_file(path, text_output):
    with path.open("r") as f:
        lines = f.readlines()
    stripped_lines = [strip_line(line) for line in lines]
    if text_output:
        for line in stripped_lines:
            print(line)
    else:
        with path.open("w") as f:
            f.writelines(stripped_lines)
