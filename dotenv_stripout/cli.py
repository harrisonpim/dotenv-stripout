import typer

from .stripout import list_dotenv_file_paths, strip_file

cli = typer.Typer()


@cli.command()
def status():
    typer.echo("Hello")


@cli.command()
def install(name, blah: bool = False):
    if blah:
        typer.echo(f"Hello {name}")
    else:
        typer.echo(f"Bye {name}")


@cli.command()
def uninstall():
    typer.echo(f"Bye")


@cli.command()
def strip(dry_run: bool = False):
    try:
        paths = list_dotenv_file_paths()
        if dry_run:
            typer.echo(
                "Dry run - Would have stripped secrets from:"
            )
            for path in paths:
                typer.echo(path)
        else:
            typer.confirm(
                "Are you sure you want to strip all secrets from this repo?"
            )
            typer.echo("Stripping secrets from:")
            for path in paths:
                typer.echo(path)
                strip_file(path)
    except OSError as e:
        typer.echo(e)
        typer.Exit()


if __name__ == "__main__":
    cli()
