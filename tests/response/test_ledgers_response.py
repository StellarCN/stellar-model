from unittest import TestCase

from stellar_model import LedgersResponse
from stellar_model.model.horizon.ledger import Ledger
from tests.response import load_response_file


class TestLedgersResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("ledgers_response.json")
        parsed_data = LedgersResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 20)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Ledger))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/ledgers?cursor=&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/ledgers?cursor=150721238619127808&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/ledgers?cursor=150721320223506432&limit=20&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
