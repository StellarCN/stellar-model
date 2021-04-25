from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.account import Account
from stellar_model.response.page_model import PageModel


__all__ = ["AccountsResponse"]


class Embedded(BaseModel):
    records: List[Account]


class AccountsResponse(PageModel):
    """
    Represents accounts response.

    Can be used for the following endpoint(s):

        - GET /accounts


    See `Accounts <https://developers.stellar.org/api/resources/accounts/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
