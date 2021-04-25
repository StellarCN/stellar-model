from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Asset(BaseModel):
    """
    Represents a single asset.
    """

    asset_type: str = Field(
        description="The type for this asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(description="The code for this asset.")
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of this asset's issuer."
    )
