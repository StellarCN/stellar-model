from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.trade import Trade
from stellar_model.response.page_model import PageModel


__all__ = ["TradesResponse"]


class Embedded(BaseModel):
    records: List[Trade]


class TradesResponse(PageModel):
    """
    Represents trades response.

    Can be used for the following endpoint(s):

        - GET /trades

    See `Trades <https://developers.stellar.org/api/resources/trades/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
