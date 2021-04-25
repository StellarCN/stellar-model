from unittest import TestCase

from stellar_model import TransactionsResponse
from stellar_model.model.horizon.transaction import Transaction
from tests.response import load_response_file


class TestTransactionsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("transactions_response.json")
        parsed_data = TransactionsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 100)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Transaction))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/transactions?cursor=&include_failed=true&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/transactions?cursor=150723639505981440&include_failed=true&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/transactions?cursor=150723643801051136&include_failed=true&limit=100&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
