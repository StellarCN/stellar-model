from unittest import TestCase

from stellar_model import OffersResponse
from stellar_model.model.horizon.offer import Offer
from tests.response import load_response_file


class TestOffersResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("offers_response.json")
        parsed_data = OffersResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 20)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Offer))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/offers?cursor=&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/offers?cursor=546459297&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/offers?cursor=546459316&limit=20&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
