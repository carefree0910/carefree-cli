import json
import subprocess

import regex as re

from typing import List
from typing import NamedTuple

from .. import console
from ..utils import beautify_cmd
from ..utils import parse_hierarchy_path
from ..common import hierarchy_argument
from ..schema import Template


class Parsed(NamedTuple):
    cmd: str
    to_fill: List[str]


def parse(template: Template) -> Parsed:
    """
    parse a given `template`. each `template` should have three formats:
    * plain command, i.e. the direct command to run. no '{}'s.
    * placeholder template, which is a string with some '{}'s, each '{}' can either
      have a name included not not.
    > if no name, should use '__i' as the name, where `__i` is the index of the '{}'.
    """

    cmd = template.cmd
    if template.is_plain:
        return Parsed(cmd, to_fill=[])
    to_fill = []
    no_names = []
    for i, m in enumerate(re.finditer(r"\{([^}]*)\}", cmd)):
        i_name = m.group(1)
        if i_name:
            if i_name not in to_fill:
                to_fill.append(i_name)
        else:
            no_names.append(i)
            to_fill.append(f"__{i}")
            cmd = cmd[: m.start()] + f"__{{{i}}}" + cmd[m.end() :]
    return Parsed(cmd, to_fill)


def load(hierarchy: hierarchy_argument) -> None:
    template_path = parse_hierarchy_path(hierarchy)
    if not template_path.exists():
        console.error(f"Cannot find template at '{template_path}'.")
        return None
    template = json.loads(template_path.read_text())
    parsed = parse(Template(**template))
    if not parsed.to_fill:
        cmd = parsed.cmd
    else:
        kwargs = {}
        console.log(f"filling command {beautify_cmd(parsed.cmd)}")
        for to_fill in parsed.to_fill:
            value = console.ask(f"[bold][cyan]`{to_fill}`")
            kwargs[to_fill] = value
        cmd = parsed.cmd.format(**kwargs)

    import pyperclip

    pyperclip.copy(cmd)
    console.log("command loaded as below, it is already copied to clipboard!")
    console.log(beautify_cmd(cmd))
