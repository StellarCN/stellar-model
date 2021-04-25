from unittest import TestCase

from stellar_model import AccountsResponse
from stellar_model.model.horizon.account import Account
from tests.response import load_response_file


class TestAccountsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("accounts_response.json")
        parsed_data = AccountsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 10)
        for record in parsed_data.embedded.records:
            self.assertTrue(isinstance(record, Account))
        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/accounts/?asset=BTC%3AGATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&cursor=&limit=10&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/accounts/?asset=BTC%3AGATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&cursor=GDZVWAFA4RN2YPFHPPF4BNL2OHONAPJLYMSEIHJBNJFMYOAGFRTFM2J4&limit=10&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/accounts/?asset=BTC%3AGATEMHCCKCY67ZUCKTROYN24ZYT5GK4EQZ65JJLDHKHRUZI3EUEKMTCH&cursor=GDZZN7FHZUJ356OAGDPXAF5NYY7N3NCQG65NCMNVOX2PSW4AD4VISEBY&limit=10&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
