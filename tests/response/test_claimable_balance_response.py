from unittest import TestCase

from stellar_model import ClaimableBalanceResponse
from stellar_model.model.horizon.claimable_balance import ClaimableBalance
from tests.response import load_horizon_file


class TestClaimableBalanceResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("claimable_balance_conditional.json")
        parsed_data = ClaimableBalanceResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, ClaimableBalanceResponse))
        self.assertTrue(isinstance(parsed_data, ClaimableBalance))
