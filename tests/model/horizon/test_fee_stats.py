import unittest

from decimal import Decimal

from stellar_model.model.horizon.fee_stats import FeeStats
from tests.model.horizon import load_horizon_file


class TestFeeStats(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("fee_stats.json")
        parsed_data = FeeStats.parse_obj(raw_data)
        self.assertEqual(parsed_data.last_ledger, 35068310)
        self.assertEqual(parsed_data.last_ledger_base_fee, 100)
        self.assertEqual(parsed_data.ledger_capacity_usage, Decimal("0.16"))

        self.assertEqual(parsed_data.fee_charged.max, 500)
        self.assertEqual(parsed_data.fee_charged.min, 100)
        self.assertEqual(parsed_data.fee_charged.mode, 100)
        self.assertEqual(parsed_data.fee_charged.p10, 100)
        self.assertEqual(parsed_data.fee_charged.p20, 100)
        self.assertEqual(parsed_data.fee_charged.p30, 100)
        self.assertEqual(parsed_data.fee_charged.p40, 100)
        self.assertEqual(parsed_data.fee_charged.p50, 100)
        self.assertEqual(parsed_data.fee_charged.p60, 100)
        self.assertEqual(parsed_data.fee_charged.p70, 100)
        self.assertEqual(parsed_data.fee_charged.p80, 100)
        self.assertEqual(parsed_data.fee_charged.p90, 100)
        self.assertEqual(parsed_data.fee_charged.p95, 100)
        self.assertEqual(parsed_data.fee_charged.p99, 100)

        self.assertEqual(parsed_data.max_fee.max, 15000)
        self.assertEqual(parsed_data.max_fee.min, 100)
        self.assertEqual(parsed_data.max_fee.mode, 1000)
        self.assertEqual(parsed_data.max_fee.p10, 100)
        self.assertEqual(parsed_data.max_fee.p20, 100)
        self.assertEqual(parsed_data.max_fee.p30, 120)
        self.assertEqual(parsed_data.max_fee.p40, 300)
        self.assertEqual(parsed_data.max_fee.p50, 1000)
        self.assertEqual(parsed_data.max_fee.p60, 1000)
        self.assertEqual(parsed_data.max_fee.p70, 1000)
        self.assertEqual(parsed_data.max_fee.p80, 1000)
        self.assertEqual(parsed_data.max_fee.p90, 1000)
        self.assertEqual(parsed_data.max_fee.p95, 3000)
        self.assertEqual(parsed_data.max_fee.p99, 15000)


if __name__ == "__main__":
    unittest.main()
