from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.transaction import Transaction
from stellar_model.response.page_model import PageModel


__all__ = ["TransactionsResponse"]


class Embedded(BaseModel):
    records: List[Transaction]


class TransactionsResponse(PageModel):
    """
    Represents transactions response.

    Can be used for the following endpoint(s):

        - GET /transactions

    See `Transactions <https://developers.stellar.org/api/resources/transactions/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
