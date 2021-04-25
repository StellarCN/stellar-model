from stellar_model.model.horizon.offer import Offer


__all__ = ["OfferResponse"]


class OfferResponse(Offer):
    """
    Represents single offer response.

    Can be used for the following endpoint(s):

        - GET /offer/:offer_id


    See `Retrieve an Offer <https://developers.stellar.org/api/resources/offers/single/>`_ on Stellar API Reference.
    """
