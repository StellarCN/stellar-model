import unittest

from stellar_model.model.horizon.account_data import AccountData
from tests.model.horizon import load_horizon_file


class TestAccountData(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("account_data.json")
        parsed_data = AccountData.parse_obj(raw_data)
        self.assertEqual(parsed_data.value, "MQ==")
        self.assertEqual(parsed_data.sponsor, None)


if __name__ == "__main__":
    unittest.main()
