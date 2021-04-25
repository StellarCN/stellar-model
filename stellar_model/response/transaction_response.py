from stellar_model.model.horizon.transaction import Transaction


__all__ = ["TransactionResponse"]


class TransactionResponse(Transaction):
    """
    Represents single transaction response.

    Can be used for the following endpoint(s):

        - GET /transactions/:transaction_id
        - POST /transactions

    See `Transactions <https://developers.stellar.org/api/resources/transactions/>`_ on Stellar API Reference.
    """
