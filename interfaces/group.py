import pydantic
from typing import Optional


class GroupInterface(pydantic.BaseModel):
    id: Optional[int]
    name: str
    is_active: bool = True
