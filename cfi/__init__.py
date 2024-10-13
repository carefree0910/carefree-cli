import typer

from .meta.init import init
from .meta.list import list
from .meta.import_fn import import_fn
from .meta.export_fn import export_fn
from .crud.create import add
from .crud.read import load
from .crud.update import update
from .crud.delete import delete

ctx_settings = {"help_option_names": ["-h", "--help"]}
cli = typer.Typer(context_settings=ctx_settings)
clil = typer.Typer(context_settings=ctx_settings)

# meta
cli.command("init", help="Initialize your project.")(init)
cli.command("ls", help="List your templates.")(list)
cli.command("export", help="Export templates to a (`cfi`) file.")(export_fn)
cli.command("import", help="Import templates from a (`cfi`) file.")(import_fn)

# crud
cli.command("add", help="Add a new template.")(add)
for c in [cli, clil]:
    c.command("load", help="Load a template.")(load)
cli.command("update", help="Update a template.")(update)
cli.command("delete", help="Delete a template.")(delete)
