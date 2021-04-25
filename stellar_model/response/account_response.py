from stellar_model.model.horizon.account import Account


__all__ = ["AccountResponse"]


class AccountResponse(Account):
    """
    Represents single account response.

    Can be used for the following endpoint(s):

        - GET /accounts/:account_id


    See `Retrieve an Account <https://developers.stellar.org/api/resources/accounts/single/>`_ on Stellar API Reference.
    """
