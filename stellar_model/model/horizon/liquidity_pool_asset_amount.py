from decimal import Decimal

from pydantic import BaseModel

from stellar_model.model.horizon.asset import Asset


__all__ = ["LiquidityPoolAssetAmount"]


class LiquidityPoolAssetAmount(BaseModel):
    """
    Represents a liquidity pool asset reserve.
    """

    asset: Asset
    amount: Decimal

    def __init__(self, **data):
        asset = data.get("asset")
        if asset is not None:
            if asset == "native":
                data["asset"] = Asset(asset_type="native")
            else:
                asset_code, asset_issuer = asset.split(":")
                asset_type = (
                    "credit_alphanum4" if len(asset_code) <= 4 else "credit_alphanum12"
                )
                data["asset"] = Asset(
                    asset_type=asset_type,
                    asset_code=asset_code,
                    asset_issuer=asset_issuer,
                )

        super().__init__(**data)
