import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.account import Account
from tests.model.horizon import load_horizon_file


class TestAccount(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("account.json")
        parsed_data = Account.model_validate(raw_data)
        self.assertEqual(
            parsed_data.id, "GDI73WJ4SX7LOG3XZDJC3KCK6ED6E5NBYK2JUBQSPBCNNWEG3ZN7T75U"
        )
        self.assertEqual(
            parsed_data.account_id,
            "GDI73WJ4SX7LOG3XZDJC3KCK6ED6E5NBYK2JUBQSPBCNNWEG3ZN7T75U",
        )
        self.assertEqual(parsed_data.sequence, 24739097524306471)
        self.assertEqual(parsed_data.subentry_count, 3)
        self.assertEqual(
            parsed_data.inflation_destination,
            "GDI73WJ4SX7LOG3XZDJC3KCK6ED6E5NBYK2JUBQSPBCNNWEG3ZN7T75U",
        )
        self.assertEqual(parsed_data.sequence_ledger, 774)
        self.assertEqual(
            parsed_data.sequence_time,
            datetime.datetime(2022, 5, 6, 5, 29, 20, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.home_domain, "tempo.eu.com")
        self.assertEqual(parsed_data.last_modified_ledger, 34720451)
        self.assertEqual(
            parsed_data.last_modified_time,
            datetime.datetime(2021, 4, 1, 18, 25, 17, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.thresholds.low_threshold, 5)
        self.assertEqual(parsed_data.thresholds.med_threshold, 0)
        self.assertEqual(parsed_data.thresholds.high_threshold, 0)
        self.assertEqual(parsed_data.flags.auth_required, False)
        self.assertEqual(parsed_data.flags.auth_revocable, True)
        self.assertEqual(parsed_data.flags.auth_immutable, False)
        self.assertEqual(parsed_data.flags.auth_clawback_enabled, False)
        self.assertEqual(len(parsed_data.signers), 1)
        self.assertEqual(parsed_data.signers[0].type, "ed25519_public_key")
        self.assertEqual(
            parsed_data.signers[0].key,
            "GDI73WJ4SX7LOG3XZDJC3KCK6ED6E5NBYK2JUBQSPBCNNWEG3ZN7T75U",
        )
        self.assertEqual(parsed_data.signers[0].weight, 10)
        self.assertEqual(len(parsed_data.data), 2)
        self.assertEqual(parsed_data.data["mock1"], "hello")
        self.assertEqual(parsed_data.data["mock2"], "world")
        self.assertEqual(parsed_data.num_sponsoring, 0)
        self.assertEqual(parsed_data.num_sponsored, 0)
        self.assertEqual(
            parsed_data.paging_token,
            "GDI73WJ4SX7LOG3XZDJC3KCK6ED6E5NBYK2JUBQSPBCNNWEG3ZN7T75U",
        )
        self.assertEqual(len(parsed_data.balances), 3)
        self.assertEqual(parsed_data.balances[0].balance, Decimal("400.0000000"))
        self.assertEqual(
            parsed_data.balances[0].liquidity_pool_id,
            "2c0bfa623845dd101cbf074a1ca1ae4b2458cc8d0104ad65939ebe2cd9054355",
        )
        self.assertEqual(parsed_data.balances[0].limit, Decimal("922337203685.4775807"))
        self.assertEqual(parsed_data.balances[0].last_modified_ledger, 367662)
        self.assertEqual(parsed_data.balances[0].is_authorized, False)
        self.assertEqual(
            parsed_data.balances[0].is_authorized_to_maintain_liabilities, False
        )
        self.assertEqual(parsed_data.balances[0].asset_type, "liquidity_pool_shares")
        self.assertEqual(parsed_data.balances[1].balance, Decimal("426.3895513"))
        self.assertEqual(parsed_data.balances[1].limit, Decimal("922337203685.4775807"))
        self.assertEqual(
            parsed_data.balances[1].buying_liabilities, Decimal("0.0000000")
        )
        self.assertEqual(
            parsed_data.balances[1].selling_liabilities, Decimal("0.0000000")
        )
        self.assertEqual(parsed_data.balances[1].last_modified_ledger, 34781475)
        self.assertEqual(parsed_data.balances[1].is_authorized, True)
        self.assertEqual(
            parsed_data.balances[1].is_authorized_to_maintain_liabilities, True
        )
        self.assertEqual(parsed_data.balances[1].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.balances[1].asset_code, "EURT")
        self.assertEqual(
            parsed_data.balances[1].asset_issuer,
            "GAP5LETOV6YIE62YAM56STDANPRDO7ZFDBGSNHJQIYGGKSMOZAHOOS2S",
        )
        self.assertEqual(parsed_data.balances[2].balance, Decimal("98.8944793"))
        self.assertEqual(parsed_data.balances[2].limit, None)
        self.assertEqual(
            parsed_data.balances[2].buying_liabilities, Decimal("0.0000000")
        )
        self.assertEqual(
            parsed_data.balances[2].selling_liabilities, Decimal("0.0000000")
        )
        self.assertEqual(parsed_data.balances[2].last_modified_ledger, None)
        self.assertEqual(parsed_data.balances[2].is_authorized, None)
        self.assertEqual(
            parsed_data.balances[2].is_authorized_to_maintain_liabilities, None
        )
        self.assertEqual(parsed_data.balances[2].asset_type, "native")
        self.assertEqual(parsed_data.balances[2].asset_code, None)
        self.assertEqual(parsed_data.balances[2].asset_issuer, None)


if __name__ == "__main__":
    unittest.main()
