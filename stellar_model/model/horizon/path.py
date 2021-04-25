from decimal import Decimal
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.asset import Asset


__all__ = ["Path"]


class Path(BaseModel):
    """
    Represents a single payment path.
    """

    source_asset_type: str = Field(
        description="The type for the source asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    source_asset_code: Optional[str] = Field(
        description="The code for the source asset."
    )
    source_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the source asset's issuer."
    )
    source_amount: Decimal = Field(
        description="An estimated cost for making a payment of destination_amount on "
        "this path. Suitable for use in the **sendMax** "
        "field of a path payment operations."
    )
    destination_asset_type: str = Field(
        description="The type for the destination asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    destination_asset_code: Optional[str] = Field(
        description="The code for the destination asset."
    )
    destination_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the destination asset's issuer."
    )
    destination_amount: Decimal = Field(
        description="The destination amount specified in the s"
        "earch that found this path."
    )
    path: List[Asset] = Field(
        description="The intermediary assets that this path hops through."
    )
