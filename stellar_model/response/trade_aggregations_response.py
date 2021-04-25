from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.trade_aggregation import TradeAggregation
from stellar_model.response.page_model import PageModel


__all__ = ["TradeAggregationsResponse"]


class Embedded(BaseModel):
    records: List[TradeAggregation]


class TradeAggregationsResponse(PageModel):
    """
    Represents trade aggregations response.

    Can be used for the following endpoint(s):

        - GET /trade_aggregations

    See `Trade Aggregations <https://developers.stellar.org/api/aggregations/trade-aggregations/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
