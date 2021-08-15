import typer

from .install import _install, _uninstall, is_installed
from .stripout import list_dotenv_file_paths, strip_file

cli = typer.Typer(help="Strip secrets from all .env files in the current repo")


@cli.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    dry_run: bool = typer.Option(
        False, help="Show the effect of the command without running it",
    ),
):
    if ctx.invoked_subcommand is None:
        try:
            paths = list_dotenv_file_paths()
            if dry_run:
                typer.echo("Dry run - Would have stripped secrets from:")
                for path in paths:
                    typer.echo(path)
            else:
                if typer.confirm(
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


@cli.command(help="Check whether the pre-commit hook has been installed")
def status(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the command will check for the pre-commit hook in the "
            "global git config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    if is_installed(scope):
        typer.echo(f"Hook is installed {scope}ly")
        if typer.confirm("Would you like to uninstall it?"):
            _uninstall(scope)
            typer.echo("Done!")
        else:
            raise typer.Abort()
    else:
        typer.echo(f"Hook is not installed {scope}ly")
        if typer.confirm("Would you like to install it?"):
            _install(scope)
            typer.echo("Done!")
        else:
            raise typer.Abort()


@cli.command(help="Install dotenv-stripout as a git pre-commit hook")
def install(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the pre-commit hook will be added to your global git "
            "config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    _install(scope)


@cli.command(help="Uninstall the pre-commit hook")
def uninstall(
    _global: bool = typer.Option(
        False,
        "--global",
        help=(
            "If set, the pre-commit hook will be removed from your global git "
            "config instead of the current repo"
        ),
    ),
):
    scope = "global" if _global else "local"
    _uninstall(scope)


if __name__ == "__main__":
    cli()
