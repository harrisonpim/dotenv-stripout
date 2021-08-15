import os
from pathlib import Path
from subprocess import CalledProcessError

from .utils import run_command


def get_git_top_level_path():
    try:
        return Path(run_command("git rev-parse --show-toplevel"))
    except CalledProcessError:
        raise OSError("Looks like this isn't a git repository!")


def get_git_dir():
    try:
        return Path(run_command("git rev-parse --git-dir"))
    except CalledProcessError:
        raise OSError("Looks like this isn't a git repository!")


def get_attrfile(scope):
    if scope == "global":
        config_dir = Path("~/.config").expanduser()
        xdg_config_dir = Path(os.environ.get("XDG_CONFIG_DIR", config_dir))
        if xdg_config_dir.exists():
            attrfile = xdg_config_dir / "git" / "attributes"
        else:
            attrfile = Path("~/.gitconfig")
    else:
        attrfile = get_git_dir() / "info" / "attributes"

    return attrfile.expanduser()
