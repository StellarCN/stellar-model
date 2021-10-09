from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link
from stellar_model.model.horizon.price import Price


__all__ = ["Trade"]


class Links(BaseModel):
    self: Link
    base: Link
    counter: Link
    operation: Link


class Trade(BaseModel):
    """
    Represents a single Trade.
    """

    id: str = Field(description="A unique identifier for this trade.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    ledger_close_time: datetime = Field(
        description="The datetime of when the ledger with this trade was closed."
    )
    offer_id: Optional[str] = Field(description="The sell offer ID. **DECPRECATED**")
    trade_type: str = Field(
        default="Can be set to **all**, **orderbook**, "
        "or **liquidity_pools** to filter only "
        "trades executed across a given mechanism."
    )
    liquidity_pool_fee_bp: Optional[int]
    base_liquidity_pool_id: Optional[str] = Field(
        description="The base liquidity pool ID. If this trade "
        "was executed against a liquidity pool."
    )
    base_offer_id: Optional[str] = Field(
        description="The base offer ID. If this offer was immediately and "
        "fully consumed, this will be a synethic ID."
    )
    base_account: Optional[str] = Field(
        description="The account ID of the base party for this trade."
    )
    base_amount: Decimal = Field(
        description="The amount of the base asset that was moved "
        "from **base_account** to **counter_account**."
    )
    base_asset_type: str = Field(
        description="The type for the base asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    base_asset_code: Optional[str] = Field(description="The code for the base asset.")
    base_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the base asset's issuer."
    )
    counter_liquidity_pool_id: Optional[str] = Field(
        description="The counter liquidity pool ID. "
        "If this trade was executed against a liquidity pool."
    )
    counter_offer_id: Optional[str] = Field(
        description="The counter offer ID. If this offer was "
        "immediately and fully consumed, this will "
        "be a synethic ID."
    )
    counter_account: Optional[str] = Field(
        description="The account ID of the counter party for this trade."
    )
    counter_amount: Decimal = Field(
        description="The amount of the counter asset that was "
        "moved from **counter_account** to **base_account**."
    )
    counter_asset_type: str = Field(
        description="The type for the counter asset. "
        "Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    counter_asset_code: Optional[str] = Field(
        description="The code for the counter asset."
    )
    counter_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the counter asset's issuer."
    )
    base_is_seller: bool = Field(description="Indicates with party is the seller.")
    price: Optional[Price] = Field(
        description="An object of a number numerator and number denominator that represents "
        "the original offer price. To derive the price, "
        "divide **n** by **d**."
    )
    links: Links = Field(alias="_links")
