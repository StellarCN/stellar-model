import unittest
from decimal import Decimal

from stellar_model.model.horizon.trade_aggregation import TradeAggregation
from tests.model.horizon import load_horizon_file


class TestTradeAggregation(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("trade_aggregation.json")
        parsed_data = TradeAggregation.model_validate(raw_data)
        self.assertEqual(parsed_data.timestamp, 1619081700000)
        self.assertEqual(parsed_data.trade_count, 1)
        self.assertEqual(parsed_data.base_volume, Decimal("3.9000000"))
        self.assertEqual(parsed_data.counter_volume, Decimal("0.0000351"))
        self.assertEqual(parsed_data.avg, Decimal("0.0000090"))
        self.assertEqual(parsed_data.high, Decimal("0.0000090"))
        self.assertEqual(parsed_data.high_r.n, 9)
        self.assertEqual(parsed_data.high_r.d, 1000000)
        self.assertEqual(parsed_data.low, Decimal("0.0000090"))
        self.assertEqual(parsed_data.low_r.n, 9)
        self.assertEqual(parsed_data.low_r.d, 1000000)
        self.assertEqual(parsed_data.open, Decimal("0.0000090"))
        self.assertEqual(parsed_data.open_r.n, 9)
        self.assertEqual(parsed_data.open_r.d, 1000000)
        self.assertEqual(parsed_data.close, Decimal("0.0000090"))
        self.assertEqual(parsed_data.close_r.n, 9)
        self.assertEqual(parsed_data.close_r.d, 1000000)


if __name__ == "__main__":
    unittest.main()
