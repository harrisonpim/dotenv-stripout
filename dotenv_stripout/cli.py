import typer

from . import __version__
from .install import _install, _uninstall, is_installed
from .stripout import list_dotenv_file_paths, strip_file, strip_stdin

cli = typer.Typer(help="Strip secrets from all .env files in the current repo")


@cli.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    dry_run: bool = typer.Option(
        False, help="Show the effect of the command without running it",
    ),
    stdin: bool = typer.Option(
        False, help="Read lines from stdin and write stripped lines to stdout",
    ),
    version: bool = typer.Option(
        False, "-v", help="Print the package version",
    ),
):
    if ctx.invoked_subcommand is None:
        if version:
            typer.echo(__version__)
            raise typer.Exit(0)
        try:
            if stdin:
                strip_stdin()
            else:
                paths = list_dotenv_file_paths()
                if dry_run:
                    typer.echo("Dry run - Would have stripped secrets from:")
                    for path in paths:
                        typer.echo(path)
                elif typer.confirm(
                    "Are you sure you want to strip secrets from this repo?"
                ):
                    typer.echo("Stripping secrets from:")
                    for path in paths:
                        typer.echo(path)
                        strip_file(path)
                else:
                    raise typer.Abort()

        except OSError as e:
            typer.echo(e)
            raise typer.Exit(1)


@cli.command(help="Check whether the filter has been installed")
def status(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the command will check for the filter in the "
            "global git config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    if is_installed(scope):
        typer.echo(f"Filter is installed {scope}ly")
    else:
        typer.echo(f"Filter is not installed {scope}ly")
        if typer.confirm("Would you like to install it?"):
            _install(scope)
            typer.echo("Done!")
        else:
            raise typer.Abort()


@cli.command(help="Install dotenv-stripout as a git filter")
def install(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the filter will be added to your global git "
            "config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    if is_installed(scope):
        typer.echo(f"Filter is already {scope}ly installed!")
        raise typer.Exit(1)
    else:
        _install(scope)
        typer.echo("Done!")


@cli.command(help="Uninstall the filter")
def uninstall(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the filter will be removed from your global git "
            "config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    if is_installed(scope):
        _uninstall(scope)
        typer.echo("Done!")
    else:
        typer.echo(f"Filter is not yet {scope}ly installed!")
        raise typer.Exit(1)


if __name__ == "__main__":
    cli()
