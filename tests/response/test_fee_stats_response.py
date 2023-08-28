from unittest import TestCase

from stellar_model import FeeStatsResponse
from stellar_model.model.horizon.fee_stats import FeeStats
from tests.response import load_horizon_file


class TestFeeStatsResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("fee_stats.json")
        parsed_data = FeeStatsResponse.model_validate(raw_data)
        self.assertTrue(isinstance(parsed_data, FeeStatsResponse))
        self.assertTrue(isinstance(parsed_data, FeeStats))
