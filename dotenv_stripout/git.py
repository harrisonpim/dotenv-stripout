import os
from pathlib import Path
from subprocess import CalledProcessError, check_output


def git(command):
    """
    run a git command
    """
    command = ["git"] + command
    try:
        return check_output(command, text=True).strip()
    except CalledProcessError:
        raise OSError(
            "Something went wrong while running:\n" f"{' '.join(command)}"
        )


def get_git_top_level_path():
    return Path(git(["rev-parse", "--show-toplevel"]))


def get_git_dir():
    return Path(git(["rev-parse", "--git-dir"]))


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
