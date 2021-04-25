from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.asset_stat import AssetStat
from stellar_model.response.page_model import PageModel


__all__ = ["AssetsResponse"]


class Embedded(BaseModel):
    records: List[AssetStat]


class AssetsResponse(PageModel):
    """
    Represents assets response.

    Can be used for the following endpoint(s):

        - GET /accounts


    See `Assets <https://developers.stellar.org/api/resources/assets/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
