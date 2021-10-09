from unittest import TestCase

from stellar_model import LiquidityPoolsResponse
from stellar_model.model.horizon.liquidity_pool import LiquidityPool
from tests.response import load_response_file


class TestLiquidityPoolsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("liquidity_pools_response.json")
        parsed_data = LiquidityPoolsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 10)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, LiquidityPool))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon-testnet.stellar.org/liquidity_pools?cursor=&limit=10&order=asc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon-testnet.stellar.org/liquidity_pools?cursor=82eba905e0403a7a01212d1ae3db7f3dcbabe00ad303800ec8a86e688ffee888&limit=10&order=asc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon-testnet.stellar.org/liquidity_pools?cursor=2389378a6156eedfac66daa000d24c926431c3e667b9f754771964f27a6da6ab&limit=10&order=desc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
