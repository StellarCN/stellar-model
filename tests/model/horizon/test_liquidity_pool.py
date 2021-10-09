import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.liquidity_pool import LiquidityPool
from tests.model.horizon import load_horizon_file


class TestLiquidityPool(unittest.TestCase):
    def test_valid_native(self):
        raw_data = load_horizon_file("liquidity_pool_native.json")
        parsed_data = LiquidityPool.parse_obj(raw_data)
        self.assertEqual(
            parsed_data.id,
            "2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab",
        )
        self.assertEqual(
            parsed_data.paging_token,
            "2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab",
        )
        self.assertEqual(parsed_data.fee_bp, 30)
        self.assertEqual(parsed_data.type, "constant_product")
        self.assertEqual(parsed_data.total_trustlines, 1)
        self.assertEqual(parsed_data.total_shares, Decimal("25612.4969497"))
        self.assertEqual(len(parsed_data.reserves), 2)
        self.assertEqual(parsed_data.reserves[0].asset.asset_type, "native")
        self.assertEqual(parsed_data.reserves[0].asset.asset_code, None)
        self.assertEqual(parsed_data.reserves[0].asset.asset_issuer, None)
        self.assertEqual(parsed_data.reserves[0].amount, Decimal("1120.0000000"))
        self.assertEqual(parsed_data.reserves[1].asset.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.reserves[1].asset.asset_code, "BTCLN")
        self.assertEqual(
            parsed_data.reserves[1].asset.asset_issuer,
            "GD4UTLD46SWG5KCUVBRWFSFCUDISYNEJ2AF5FNB67ORAE6K7ZSAXH5O7",
        )
        self.assertEqual(parsed_data.reserves[1].amount, Decimal("585905.8506615"))
        self.assertEqual(parsed_data.last_modified_ledger, 366227)
        self.assertEqual(
            parsed_data.last_modified_time,
            datetime.datetime(2021, 10, 7, 16, 1, 59, tzinfo=datetime.timezone.utc),
        )

    def test_valid_alphanum(self):
        raw_data = load_horizon_file("liquidity_pool_alphanum.json")
        parsed_data = LiquidityPool.parse_obj(raw_data)
        self.assertEqual(
            parsed_data.id,
            "2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab",
        )
        self.assertEqual(
            parsed_data.paging_token,
            "2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab",
        )
        self.assertEqual(parsed_data.fee_bp, 30)
        self.assertEqual(parsed_data.type, "constant_product")
        self.assertEqual(parsed_data.total_trustlines, 1)
        self.assertEqual(parsed_data.total_shares, Decimal("25612.4969497"))
        self.assertEqual(len(parsed_data.reserves), 2)
        self.assertEqual(parsed_data.reserves[0].asset.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.reserves[0].asset.asset_code, "COOL")
        self.assertEqual(
            parsed_data.reserves[0].asset.asset_issuer,
            "GAZKB7OEYRUVL6TSBXI74D2IZS4JRCPBXJZ37MDDYAEYBOMHXUYIX5YL",
        )
        self.assertEqual(parsed_data.reserves[0].amount, Decimal("1120.0000000"))
        self.assertEqual(parsed_data.reserves[1].asset.asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.reserves[1].asset.asset_code, "BTCLN")
        self.assertEqual(
            parsed_data.reserves[1].asset.asset_issuer,
            "GD4UTLD46SWG5KCUVBRWFSFCUDISYNEJ2AF5FNB67ORAE6K7ZSAXH5O7",
        )
        self.assertEqual(parsed_data.reserves[1].amount, Decimal("585905.8506615"))
        self.assertEqual(parsed_data.last_modified_ledger, 366227)
        self.assertEqual(
            parsed_data.last_modified_time,
            datetime.datetime(2021, 10, 7, 16, 1, 59, tzinfo=datetime.timezone.utc),
        )


if __name__ == "__main__":
    unittest.main()
