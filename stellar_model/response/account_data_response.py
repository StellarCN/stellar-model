from stellar_model.model.horizon.account_data import AccountData


__all__ = ["AccountDataResponse"]


class AccountDataResponse(AccountData):
    """
    Represents single account data response.

    Can be used for the following endpoint(s):

        - GET /accounts/:account_id/data/:key

    See `Retrieve an Account's Data <https://developers.stellar.org/api/resources/accounts/data/>`_ on Stellar API Reference.
    """
