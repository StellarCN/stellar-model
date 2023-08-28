from unittest import TestCase

from stellar_model import AssetsResponse
from stellar_model.model.horizon.asset_stat import AssetStat
from tests.response import load_response_file


class TestAssetsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("assets_response.json")
        parsed_data = AssetsResponse.model_validate(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 100)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, AssetStat))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon-testnet.stellar.org/assets?cursor=&limit=100&order=asc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon-testnet.stellar.org/assets?cursor=00300076FD_GAFIQIKCKZFVB263EF2NUZDX6WLGNTVKNTQP6EYMZEBCASDOPFVBVHAA_credit_alphanum12&limit=100&order=asc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon-testnet.stellar.org/assets?cursor=0000158EEB_GA26RGSABBCQDHNGBS7X6OJPEN7F3WSJBQOCWUODMSLZCXRKPTTVBGI6_credit_alphanum12&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
