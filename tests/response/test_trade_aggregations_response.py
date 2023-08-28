from unittest import TestCase

from stellar_model import TradeAggregationsResponse
from stellar_model.model.horizon.trade_aggregation import TradeAggregation
from tests.response import load_response_file


class TestTradeAggregationsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("trade_aggregations_response.json")
        parsed_data = TradeAggregationsResponse.model_validate(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 100)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, TradeAggregation))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/trade_aggregations?base_asset_type=credit_alphanum4&base_asset_code=BTC&base_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&counter_asset_type=native&resolution=60000&limit=100",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/trade_aggregations?base_asset_code=BTC&base_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&base_asset_type=credit_alphanum4&counter_asset_type=native&limit=100&resolution=60000&start_time=0",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(parsed_data.links.prev.href, "")
        self.assertEqual(parsed_data.links.prev.templated, None)
