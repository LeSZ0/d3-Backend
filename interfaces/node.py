import pydantic
from typing import Optional


class NodeInterface(pydantic.BaseModel):
    id: str
    group: int
