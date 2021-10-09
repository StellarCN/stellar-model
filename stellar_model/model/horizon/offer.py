from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.asset import Asset
from stellar_model.model.horizon.link import Link
from stellar_model.model.horizon.price import Price


__all__ = ["Offer"]


class Links(BaseModel):
    self: Link
    offer_maker: Link


class Offer(BaseModel):
    """
    Represents the display form of an offer to trade currency.
    """

    id: str = Field(description="A unique identifier for this offer.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    seller: str = Field(description="The account ID of the account making this offer.")
    selling: Asset = Field(description="The asset this offer wants to sell.")
    buying: Asset = Field(description="The asset this offer wants to buy.")
    amount: Decimal = Field(
        description="The amount of **selling** that the account making this offer "
        "is willing to sell."
    )
    price_r: Price = Field(
        description="A precise representation of the buy and sell price of the assets on offer."
    )
    price: Decimal = Field(
        description="How many units of **buying** it takes to get 1 unit of **selling**. "
        "A number representing the decimal form of **price_r**."
    )
    last_modified_ledger: int = Field(
        description="The sequence number of the last ledger "
        "in which this offer was modified."
    )
    last_modified_time: Optional[datetime] = Field(
        description="The time of the last ledger " "in which this offer was modified."
    )
    sponsor: Optional[str] = Field(
        description="The account id of the sponsor "
        "who is paying the reserves for this offer."
    )
    links: Links = Field(alias="_links")
