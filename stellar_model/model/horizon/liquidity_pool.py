from datetime import datetime
from decimal import Decimal
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link
from stellar_model.model.horizon.liquidity_pool_asset_amount import (
    LiquidityPoolAssetAmount,
)


__all__ = ["LiquidityPool"]


class Links(BaseModel):
    self: Link
    transactions: Link
    operations: Link


class LiquidityPool(BaseModel):
    """
    Represents a liquidity pool.
    """

    id: str = Field(description="A unique identifier for this offer.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    fee_bp: int
    type: str
    total_trustlines: int
    total_shares: Decimal
    reserves: List[LiquidityPoolAssetAmount] = Field(
        description="Only include liquidity pools which have "
        "reserves matching all listed assets."
    )
    last_modified_ledger: int = Field(
        description="The sequence number of the last ledger "
        "in which this offer was modified."
    )
    last_modified_time: Optional[datetime] = Field(
        description="The time of the last ledger " "in which this offer was modified."
    )
    links: Links = Field(alias="_links")
