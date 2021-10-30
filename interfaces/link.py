import pydantic
from typing import Optional


class LinkInterface(pydantic.BaseModel):
    id: Optional[int]
    source: str
    target: str
    value: int
