from stellar_model.model.horizon.ledger import Ledger


__all__ = ["LedgerResponse"]


class LedgerResponse(Ledger):
    """
    Represents single ledger response.

    Can be used for the following endpoint(s):

        - GET /ledger/:sequence_id


    See `Retrieve a Ledger <https://developers.stellar.org/api/resources/ledgers/single/>`_ on Stellar API Reference.
    """
