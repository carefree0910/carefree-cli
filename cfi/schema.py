from pathlib import Path
from pydantic import BaseModel


class TemplatePack(BaseModel):
    cmd: str
    hierarchy: Path
