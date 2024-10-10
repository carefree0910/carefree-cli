from pathlib import Path
from pydantic import BaseModel


class Template(BaseModel):
    cmd: str
    hierarchy: Path
