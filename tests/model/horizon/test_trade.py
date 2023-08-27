import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.trade import Trade
from tests.model.horizon import load_horizon_file


class TestTrade(unittest.TestCase):
    def test_valid_orderbook(self):
        raw_data = load_horizon_file("trade_orderbook.json")
        parsed_data = Trade.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "150615114272284677-0")
        self.assertEqual(parsed_data.paging_token, "150615114272284677-0")
        self.assertEqual(
            parsed_data.ledger_close_time,
            datetime.datetime(2021, 4, 23, 13, 55, 52, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.offer_id, "544656471")
        self.assertEqual(parsed_data.trade_type, "orderbook")
        self.assertEqual(parsed_data.liquidity_pool_fee_bp, None)
        self.assertEqual(parsed_data.base_offer_id, "4762301132699672581")
        self.assertEqual(
            parsed_data.base_account,
            "GAREHPOLONP4N5WJPF6EG676FAH3IEDUF5AXMZXGSVU3262XJETXOTLW",
        )
        self.assertEqual(parsed_data.base_amount, Decimal("0.4355160"))
        self.assertEqual(parsed_data.base_asset_type, "native")
        self.assertEqual(parsed_data.base_asset_code, None)
        self.assertEqual(parsed_data.base_asset_issuer, None)
        self.assertEqual(parsed_data.counter_liquidity_pool_id, None)
        self.assertEqual(parsed_data.counter_offer_id, "544656471")
        self.assertEqual(
            parsed_data.counter_account,
            "GB4FWDMQZEMDNAYUHOUOOXCG4TOWCNDUUEAI7ZUHNNPAK2236444OXHD",
        )
        self.assertEqual(parsed_data.counter_amount, Decimal("0.1841505"))
        self.assertEqual(parsed_data.counter_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.counter_asset_code, "USD")
        self.assertEqual(
            parsed_data.counter_asset_issuer,
            "GDUKMGUGDZQK6YHYA5Z6AY2G4XDSZPSZ3SW5UN3ARVMO6QSRDWP5YLEX",
        )
        self.assertEqual(parsed_data.base_is_seller, False)
        self.assertEqual(parsed_data.price.n, 200)
        self.assertEqual(parsed_data.price.d, 473)

    def test_valid_liquidity_pool(self):
        raw_data = load_horizon_file("trade_liquidity_pool.json")
        parsed_data = Trade.model_validate(raw_data)
        self.assertEqual(parsed_data.id, "1567602933510145-0")
        self.assertEqual(parsed_data.paging_token, "1567602933510145-0")
        self.assertEqual(
            parsed_data.ledger_close_time,
            datetime.datetime(2021, 10, 7, 14, 13, 20, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.offer_id, None)
        self.assertEqual(parsed_data.trade_type, "liquidity_pool")
        self.assertEqual(parsed_data.liquidity_pool_fee_bp, 30)
        self.assertEqual(parsed_data.base_offer_id, "4613253621360898049")
        self.assertEqual(
            parsed_data.base_account,
            "GCUGVB6HXX56LMAYLTD2OJRJYGRGQRHQ4H5WFZRCWG4WOPCJSLFCWUZA",
        )
        self.assertEqual(parsed_data.base_amount, Decimal("10.0000000"))
        self.assertEqual(parsed_data.base_asset_type, "native")
        self.assertEqual(parsed_data.base_asset_code, None)
        self.assertEqual(parsed_data.base_asset_issuer, None)
        self.assertEqual(
            parsed_data.counter_liquidity_pool_id,
            "2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab",
        )
        self.assertEqual(parsed_data.counter_offer_id, None)
        self.assertEqual(
            parsed_data.counter_account,
            None,
        )
        self.assertEqual(parsed_data.counter_amount, Decimal("6475.7567056"))
        self.assertEqual(parsed_data.counter_asset_type, "credit_alphanum12")
        self.assertEqual(parsed_data.counter_asset_code, "BTCLN")
        self.assertEqual(
            parsed_data.counter_asset_issuer,
            "GD4UTLD46SWG5KCUVBRWFSFCUDISYNEJ2AF5FNB67ORAE6K7ZSAXH5O7",
        )
        self.assertEqual(parsed_data.base_is_seller, False)
        self.assertEqual(parsed_data.price.n, 64757567056)
        self.assertEqual(parsed_data.price.d, 100000000)


if __name__ == "__main__":
    unittest.main()
