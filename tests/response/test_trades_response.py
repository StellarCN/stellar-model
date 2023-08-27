from unittest import TestCase

from stellar_model import TradesResponse
from stellar_model.model.horizon.trade import Trade
from tests.response import load_response_file


class TestTradesResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("trades_response.json")
        parsed_data = TradesResponse.model_validate(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 100)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Trade))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/trades?base_asset_type=native&counter_asset_code=BTC&counter_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&counter_asset_type=credit_alphanum4&cursor=&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/trades?base_asset_type=native&counter_asset_code=BTC&counter_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&counter_asset_type=credit_alphanum4&cursor=148329556015616001-3&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/trades?base_asset_type=native&counter_asset_code=BTC&counter_asset_issuer=GATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&counter_asset_type=credit_alphanum4&cursor=150716462615965697-0&limit=100&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
