import os
from pathlib import Path
from subprocess import CalledProcessError, check_output
from enum import Enum


class Scope(Enum):
    """
    The scope of the git filter. Options are "global" and "local"

    Local refers to the current git repository, while global refers to the user's
    global git config. See https://git-scm.com/docs/git-config#SCOPES for more info
    """

    GLOBAL = "global"
    LOCAL = "local"


def git(command: list[str]) -> str:
    """
    Run a git command and return the output as a string

    :param list[str] command: Git command to run, eg. ["rev-parse", "--show-toplevel"]
    :raises OSError: If the command fails, an OSError is raised
    :return str: The output of the command
    """
    command = ["git"] + command
    try:
        return check_output(command, text=True).strip()
    except CalledProcessError:
        raise OSError("Something went wrong while running:\n" f"{' '.join(command)}")


def get_git_top_level_path() -> Path:
    """
    Get the top level path of the current git repository

    :return Path: The top level path of the current git repository
    """
    return Path(git(["rev-parse", "--show-toplevel"]))


def get_git_dir() -> Path:
    """
    Get the path to the .git directory of the current git repository

    :return Path: The path to the .git directory of the current git repository
    """
    return Path(git(["rev-parse", "--git-dir"]))


def get_attrfile(scope: Scope) -> Path:
    """
    Get the path to the git attributes file

    :param Scope scope: The scope of the git filter
    :return Path: The path to the git attributes file
    """
    if scope == Scope.GLOBAL:
        config_dir = Path("~/.config").expanduser()
        xdg_config_dir = Path(os.environ.get("XDG_CONFIG_DIR", config_dir))
        if xdg_config_dir.exists():
            attrfile = xdg_config_dir / "git" / "attributes"
        else:
            attrfile = Path("~/.gitconfig")
    else:
        attrfile = get_git_dir() / "info" / "attributes"

    return attrfile.expanduser()
