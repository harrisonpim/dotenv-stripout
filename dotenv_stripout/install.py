import sys

from .git import get_attrfile
from .stripout import patterns
from .utils import run_command

attr_lines = [
    f"{pattern} {attribute}"
    for pattern in patterns
    for attribute in ["filter=dotenv-stripout -y", "diff=env"]
]


def _install(scope="local"):
    python = sys.executable.replace("\\", "/")
    run_command(
        f"git config --{scope} filter.dotenvstripout.clean "
        f"'{python} -m dotenv_stripout'"
    )
    run_command(f"git config --{scope} filter.dotenvstripout.smudge cat")

    attrfile = get_attrfile(scope)
    with attrfile.open("ra") as f:
        if f.tell():
            f.write("\n")

        for line in attr_lines:
            if line not in f.readlines():
                f.write(line)


def _uninstall(scope="local"):
    run_command(f"git config --{scope} --remove-section filter.dotenvstripout")
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
