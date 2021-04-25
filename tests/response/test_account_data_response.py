from unittest import TestCase

from stellar_model import AccountDataResponse
from stellar_model.model.horizon.account_data import AccountData
from tests.response import load_horizon_file


class TestAccountDataResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("account_data.json")
        parsed_data = AccountDataResponse.parse_obj(raw_data)
        self.assertTrue(isinstance(parsed_data, AccountDataResponse))
        self.assertTrue(isinstance(parsed_data, AccountData))
