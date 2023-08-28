from unittest import TestCase

from stellar_model.model.horizon.account import Account
from stellar_model.response.account_response import AccountResponse
from tests.response import load_horizon_file


class TestAccountResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("account.json")
        parsed_data = AccountResponse.model_validate(raw_data)
        self.assertTrue(isinstance(parsed_data, AccountResponse))
        self.assertTrue(isinstance(parsed_data, Account))
