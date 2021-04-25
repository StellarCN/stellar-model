from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


class Links(BaseModel):
    self: Link
    next: Link
    prev: Link


class PageModel(BaseModel):
    """
    Represents pageable response.
    """

    links: Links = Field(alias="_links")
