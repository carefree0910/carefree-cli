from typing import List
from pydantic import BaseModel


class Template(BaseModel):
    cmd: str
    is_plain: bool


class TemplatePack(BaseModel):
    cmd: Template
    hierarchy: List[str]
