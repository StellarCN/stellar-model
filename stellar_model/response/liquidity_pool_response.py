from stellar_model.model.horizon.liquidity_pool import LiquidityPool


__all__ = ["LiquidityPoolResponse"]


class LiquidityPoolResponse(LiquidityPool):
    """
    Represents single liquidity pool response.

    Can be used for the following endpoint(s):

        - GET /liquidity_pools/:liquidity_pool_id

    See `Retrieve a Liquidity Pool <https://developers.stellar.org/api/resources/liquiditypools/single/>`_ on Stellar API Reference.
    """
