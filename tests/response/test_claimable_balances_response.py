from unittest import TestCase

from stellar_model import ClaimableBalancesResponse
from stellar_model.model.horizon.claimable_balance import ClaimableBalance
from tests.response import load_response_file


class TestClaimableBalancesResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("claimable_balances_response.json")
        parsed_data = ClaimableBalancesResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 20)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, ClaimableBalance))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/claimable_balances/?cursor=&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/claimable_balances/?cursor=35007005-000000002ea6748769c932ef4bb286886cdb07c60a83a1cd5457d4ae9ec13515d590b878&limit=20&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/claimable_balances/?cursor=35084005-0000000048a70acdec712be9547d19f7e58adc22e35e0f5bcf3897a0353ab5dd4c5d61f4&limit=20&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
