from unittest import TestCase

from stellar_model import LiquidityPoolResponse
from stellar_model.model.horizon.liquidity_pool import LiquidityPool
from tests.response import load_horizon_file


class TestLiquidityPoolResponse(TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("liquidity_pool_alphanum.json")
        parsed_data = LiquidityPoolResponse.model_validate(raw_data)
        self.assertTrue(isinstance(parsed_data, LiquidityPoolResponse))
        self.assertTrue(isinstance(parsed_data, LiquidityPool))
