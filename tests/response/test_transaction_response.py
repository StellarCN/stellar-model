from unittest import TestCase

from stellar_model import TransactionResponse
from stellar_model.model.horizon.transaction import Transaction
from tests.response import load_horizon_file


class TestTransactionResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("transaction.json")
        parsed_data = TransactionResponse.model_validate(raw_data)
        self.assertTrue(isinstance(parsed_data, TransactionResponse))
        self.assertTrue(isinstance(parsed_data, Transaction))
