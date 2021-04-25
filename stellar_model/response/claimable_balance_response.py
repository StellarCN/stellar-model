from stellar_model.model.horizon.claimable_balance import ClaimableBalance


__all__ = ["ClaimableBalanceResponse"]


class ClaimableBalanceResponse(ClaimableBalance):
    """
    Represents single claimable balance response.

    Can be used for the following endpoint(s):

        - GET /claimable_balances/:claimable_balance_id

    See `Claimable Balances <https://developers.stellar.org/api/resources/claimablebalances/>`_ on Stellar API Reference.
    """
