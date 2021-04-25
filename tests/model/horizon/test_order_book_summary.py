import unittest

from decimal import Decimal

from stellar_model.model.horizon.order_book_summary import OrderBookSummary
from tests.model.horizon import load_horizon_file


class TestOrderBookSummary(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("order_book_summary.json")
        parsed_data = OrderBookSummary.parse_obj(raw_data)
        self.assertEqual(parsed_data.base.asset_type, "native")
        self.assertEqual(parsed_data.base.asset_code, None)
        self.assertEqual(parsed_data.base.asset_issuer, None)
        self.assertEqual(parsed_data.counter.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.counter.asset_code, "BTC")
        self.assertEqual(
            parsed_data.counter.asset_issuer,
            "GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH",
        )
        self.assertEqual(len(parsed_data.bids), 20)
        self.assertEqual(parsed_data.bids[0].amount, Decimal("0.0010503"))
        self.assertEqual(parsed_data.bids[0].price, Decimal("0.0000070"))
        self.assertEqual(parsed_data.bids[0].price_r.n, 7)
        self.assertEqual(parsed_data.bids[0].price_r.d, 1000000)
        self.assertEqual(len(parsed_data.asks), 20)
        self.assertEqual(parsed_data.asks[0].amount, Decimal("485.0714286"))
        self.assertEqual(parsed_data.asks[0].price, Decimal("0.0000084"))
        self.assertEqual(parsed_data.asks[0].price_r.n, 21)
        self.assertEqual(parsed_data.asks[0].price_r.d, 2500000)


if __name__ == "__main__":
    unittest.main()
