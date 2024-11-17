from stellar_model.model.horizon.async_transaction import AsyncTransaction

__all__ = ["AsyncTransactionResponse"]


class AsyncTransactionResponse(AsyncTransaction):
    """Represents async transaction response.

    Can be used for the following endpoint(s):

        - POST /transactions_async

    See `Submit a Transaction Asynchronously <https://developers.stellar.org/docs/data/horizon/api-reference/submit-async-transaction>`_ on Stellar API Reference.
    """
