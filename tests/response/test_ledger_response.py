from unittest import TestCase

from stellar_model import LedgerResponse
from stellar_model.model.horizon.ledger import Ledger
from tests.response import load_horizon_file


class TestLedgerResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("ledger.json")
        parsed_data = LedgerResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, LedgerResponse))
        self.assertTrue(isinstance(parsed_data, Ledger))
