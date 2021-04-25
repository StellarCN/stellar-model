from unittest import TestCase

from stellar_model import AssetsResponse
from stellar_model.model.horizon.asset_stat import AssetStat
from tests.response import load_response_file


class TestAssetsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("assets_response.json")
        parsed_data = AssetsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 20)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, AssetStat))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/assets?cursor=&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/assets?cursor=ZYH_GAPBH5XTXAF4QYLIS4BBFXJPUA6WBLGUYCD62LWCPHY2NEGUQTE6QHTF_credit_alphanum4&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/assets?cursor=zzzx_GBIBNMZYLJ5P4B2YKFWWMJYEF4RP77HUGBZWQBRML74ZYEL5FKDQOOQI_credit_alphanum4&limit=20&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
