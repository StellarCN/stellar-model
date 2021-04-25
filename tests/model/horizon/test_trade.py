import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.trade import Trade
from tests.model.horizon import load_horizon_file


class TestTrade(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("trade.json")
        parsed_data = Trade.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "150615114272284677-0")
        self.assertEqual(parsed_data.paging_token, "150615114272284677-0")
        self.assertEqual(
            parsed_data.ledger_close_time,
            datetime.datetime(2021, 4, 23, 13, 55, 52, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.offer_id, "544656471")
        self.assertEqual(parsed_data.base_offer_id, "4762301132699672581")
        self.assertEqual(
            parsed_data.base_account,
            "GAREHPOLONP4N5WJPF6EG676FAH3IEDUF5AXMZXGSVU3262XJETXOTLW",
        )
        self.assertEqual(parsed_data.base_amount, Decimal("0.4355160"))
        self.assertEqual(parsed_data.base_asset_type, "native")
        self.assertEqual(parsed_data.base_asset_code, None)
        self.assertEqual(parsed_data.base_asset_issuer, None)
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


if __name__ == "__main__":
    unittest.main()
