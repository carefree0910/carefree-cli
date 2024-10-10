import json

from typing import List
from pathlib import Path
from pydantic import BaseModel

from . import console
from .constants import CFI_SUFFIX
from .constants import CFI_SETTINGS_PATH


class Settings(BaseModel):
    data_dir: Path


def load_settings_or_error() -> Settings:
    if not CFI_SETTINGS_PATH.is_file():
        msg = f"Cannot find '{CFI_SETTINGS_PATH}', please run `cfi init` first."
        console.error(msg)
        raise SystemExit(1)
    with CFI_SETTINGS_PATH.open("r") as f:
        return Settings(**json.load(f))


def ask_with_warn(question: str) -> bool:
    return console.ask(f"[yellow]{question}", ["y", "n"], default="n") == "y"


def parse_hierarchy_parent(hierarchy: List[str]) -> Path:
    settings = load_settings_or_error()
    return settings.data_dir.joinpath(*hierarchy[:-1])


def parse_hierarchy_path(hierarchy: List[str]) -> Path:
    parent = parse_hierarchy_parent(hierarchy)
    return parent / f"{hierarchy[-1]}{CFI_SUFFIX}"


def beautify_cmd(cmd: str) -> str:
    return f"[green]{cmd}[/green]"
