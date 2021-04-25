from unittest import TestCase

from stellar_model import OfferResponse
from stellar_model.model.horizon.offer import Offer
from tests.response import load_horizon_file


class TestOfferResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("offer.json")
        parsed_data = OfferResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, OfferResponse))
        self.assertTrue(isinstance(parsed_data, Offer))
