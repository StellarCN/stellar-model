import unittest

from decimal import Decimal

from stellar_model.model.horizon.asset_stat import AssetStat
from tests.model.horizon import load_horizon_file


class TestAssetStat(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("asset_stat.json")
        parsed_data = AssetStat.parse_obj(raw_data)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "BTC")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH",
        )
        self.assertEqual(
            parsed_data.paging_token,
            "BTC_GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH_credit_alphanum4",
        )
        self.assertEqual(parsed_data.accounts.authorized, 7377)
        self.assertEqual(parsed_data.accounts.authorized_to_maintain_liabilities, 0)
        self.assertEqual(parsed_data.accounts.unauthorized, 0)
        self.assertEqual(parsed_data.num_claimable_balances, 0)
        self.assertEqual(parsed_data.amount, Decimal("989.9464476"))
        self.assertEqual(parsed_data.balances.authorized, Decimal("989.9464476"))
        self.assertEqual(
            parsed_data.balances.authorized_to_maintain_liabilities, Decimal("0")
        )
        self.assertEqual(parsed_data.balances.unauthorized, Decimal("0"))
        self.assertEqual(parsed_data.claimable_balances_amount, Decimal("0"))
        self.assertEqual(parsed_data.num_accounts, 7377)
        self.assertEqual(parsed_data.flags.auth_required, False)
        self.assertEqual(parsed_data.flags.auth_revocable, False)
        self.assertEqual(parsed_data.flags.auth_immutable, False)
        self.assertEqual(parsed_data.flags.auth_clawback_enabled, False)


if __name__ == "__main__":
    unittest.main()
