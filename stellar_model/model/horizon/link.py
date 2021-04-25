from typing import Optional

from pydantic import BaseModel


class Link(BaseModel):
    href: str
    templated: Optional[bool]
