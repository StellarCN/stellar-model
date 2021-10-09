from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.liquidity_pool import LiquidityPool
from stellar_model.response.page_model import PageModel


__all__ = ["LiquidityPoolsResponse"]


class Embedded(BaseModel):
    records: List[LiquidityPool]


class LiquidityPoolsResponse(PageModel):
    """
    Represents liquidity pools response.

    Can be used for the following endpoint(s):

        - GET /liquidity_pools


    See `Liquidity Pools <https://developers.stellar.org/api/resources/liquiditypools/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
