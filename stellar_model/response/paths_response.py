from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.path import Path


__all__ = ["PathsResponse"]


class Embedded(BaseModel):
    records: List[Path]


class PathsResponse(BaseModel):
    """
    Represents paths response.

    Can be used for the following endpoint(s):

        - GET /paths/strict-receive
        - GET /paths/strict-send

    See `Paths <https://developers.stellar.org/api/aggregations/paths/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
