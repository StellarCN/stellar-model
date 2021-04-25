from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.claimable_balance import ClaimableBalance
from stellar_model.response.page_model import PageModel


__all__ = ["ClaimableBalancesResponse"]


class Embedded(BaseModel):
    records: List[ClaimableBalance]


class ClaimableBalancesResponse(PageModel):
    """
    Represents claimable balances response.

    Can be used for the following endpoint(s):

        - GET /claimable_balances

    See `Claimable Balances <https://developers.stellar.org/api/resources/claimablebalances/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
