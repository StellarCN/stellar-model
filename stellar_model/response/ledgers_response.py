from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.ledger import Ledger
from stellar_model.response.page_model import PageModel


__all__ = ["LedgersResponse"]


class Embedded(BaseModel):
    records: List[Ledger]


class LedgersResponse(PageModel):
    """
    Represents ledgers response.

    Can be used for the following endpoint(s):

        - GET /ledgers


    See `Ledgers <https://developers.stellar.org/api/resources/ledgers/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
