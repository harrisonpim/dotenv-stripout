import sys

from .git import get_attrfile, git
from .stripout import patterns

attr_lines = [
    f"{pattern} {attribute}\n"
    for attribute in ["filter=dotenvstripout"]
    for pattern in patterns
]


def _install(scope="local"):
    python = sys.executable.replace("\\", "/")
    git(["config", f"--{scope}", "filter.dotenvstripout.smudge", "cat"])
    git(
        [
            "config",
            f"--{scope}",
            "filter.dotenvstripout.clean",
            f'"{python}" -m dotenv_stripout --stdin',
        ]
    )

    attrfile = get_attrfile(scope)

    if not attrfile.exists():
        attrfile.touch(exist_ok=True)

    with attrfile.open("r") as f:
        attrs = f.readlines()

    with attrfile.open("a",) as f:
        if f.tell():
            f.write("\n")
        for line in attr_lines:
            if line not in attrs:
                f.write(line)


def _uninstall(scope="local"):
    git(["config", f"--{scope}", "--remove-section", "filter.dotenvstripout"])
    attrfile = get_attrfile(scope)
    with attrfile.open("r") as f:
        attrs_to_keep = [
            line for line in f.readlines() if line not in attr_lines
        ]
    with attrfile.open("w") as f:
        f.writelines(attrs_to_keep)


def is_installed(scope="local"):
    attrfile = get_attrfile(scope)
    try:
        with attrfile.open("r") as f:
            attrs = f.readlines()
        if all([line in attrs for line in attr_lines]):
            return True
        else:
            return False
    except FileNotFoundError:
        return False
