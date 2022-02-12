from unittest import TestCase

from stellar_model import OrderBookResponse
from stellar_model.model.horizon.order_book_summary import OrderBookSummary
from tests.response import load_response_file


class TestLedgerResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("order_book_response.json")
        parsed_data = OrderBookResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, OrderBookResponse))
        self.assertTrue(isinstance(parsed_data, OrderBookSummary))
