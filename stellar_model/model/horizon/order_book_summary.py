from decimal import Decimal
from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.asset import Asset
from stellar_model.model.horizon.price import Price


__all__ = ["OrderBookSummary"]


class PriceLevel(BaseModel):
    """
    Represents an aggregation of offers that share a given price.
    """

    price: Decimal = Field(
        description="The bid price of the base asset denominated in the counter asset. "
        "A number representing the decimal form of **price_r**."
    )
    price_r: Price = Field(
        description="A precise representation of the bid price of the asset pair."
    )
    amount: Decimal = Field(
        description="The amount of counter asset that the account making "
        "this offer is willing to buy at this price."
    )


class OrderBookSummary(BaseModel):
    """
    Represents a snapshot summary of a given order book.
    """

    bids: List[PriceLevel] = Field(
        description="The prices and amounts for the buyside of the asset pair."
    )
    asks: List[PriceLevel] = Field(
        description="The prices and amounts for the sellside of the asset pair."
    )
    base: Asset = Field(description="Details about the base asset.")
    counter: Asset = Field(description="Details about the counter asset.")
