from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.offer import Offer
from stellar_model.response.page_model import PageModel


__all__ = ["OffersResponse"]


class Embedded(BaseModel):
    records: List[Offer]


class OffersResponse(PageModel):
    """
    Represents offers response.

    Can be used for the following endpoint(s):

        - GET /offers


    See `Offers <https://developers.stellar.org/api/resources/offers/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
