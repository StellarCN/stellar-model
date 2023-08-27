import unittest

from decimal import Decimal

from stellar_model.model.horizon.asset_stat import AssetStat
from tests.model.horizon import load_horizon_file


class TestAssetStat(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("asset_stat.json")
        parsed_data = AssetStat.model_validate(raw_data)
        self.assertEqual(parsed_data.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.asset_code, "ZX2")
        self.assertEqual(
            parsed_data.asset_issuer,
            "GDBSQA2GDRBRZVWOMRLZ6V4ZN2UESRQAEIHGKCZDR3YO4QIMC3CLHPR3",
        )
        self.assertEqual(
            parsed_data.paging_token,
            "ZX2_GDBSQA2GDRBRZVWOMRLZ6V4ZN2UESRQAEIHGKCZDR3YO4QIMC3CLHPR3_credit_alphanum4",
        )
        self.assertEqual(parsed_data.num_accounts, 1)
        self.assertEqual(parsed_data.num_claimable_balances, 0)
        self.assertEqual(parsed_data.num_liquidity_pools, 0)
        self.assertEqual(parsed_data.amount, Decimal("1001"))
        self.assertEqual(parsed_data.accounts.authorized, 1)
        self.assertEqual(parsed_data.accounts.authorized_to_maintain_liabilities, 0)
        self.assertEqual(parsed_data.accounts.unauthorized, 0)
        self.assertEqual(parsed_data.claimable_balances_amount, Decimal("0"))
        self.assertEqual(parsed_data.liquidity_pools_amount, Decimal("0"))
        self.assertEqual(parsed_data.balances.authorized, Decimal("1001"))
        self.assertEqual(
            parsed_data.balances.authorized_to_maintain_liabilities, Decimal("0")
        )
        self.assertEqual(parsed_data.balances.unauthorized, Decimal("0"))
        self.assertEqual(parsed_data.flags.auth_required, False)
        self.assertEqual(parsed_data.flags.auth_revocable, False)
        self.assertEqual(parsed_data.flags.auth_immutable, False)
        self.assertEqual(parsed_data.flags.auth_clawback_enabled, False)


if __name__ == "__main__":
    unittest.main()
