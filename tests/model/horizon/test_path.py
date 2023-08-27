import unittest

from decimal import Decimal

from stellar_model.model.horizon.path import Path
from tests.model.horizon import load_horizon_file


class TestPath(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("path.json")
        parsed_data = Path.model_validate(raw_data)
        self.assertEqual(parsed_data.source_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.source_asset_code, "CNY")
        self.assertEqual(
            parsed_data.source_asset_issuer,
            "GAREELUB43IRHWEASCFBLKHURCGMHE5IF6XSE7EXDLACYHGRHM43RFOX",
        )
        self.assertEqual(parsed_data.source_amount, Decimal("39.9854243"))
        self.assertEqual(parsed_data.destination_asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.destination_asset_code, "BB1")
        self.assertEqual(
            parsed_data.destination_asset_issuer,
            "GD5J6HLF5666X4AZLTFTXLY46J5SW7EXRKBLEYPJP33S33MXZGV6CWFN",
        )
        self.assertEqual(parsed_data.destination_amount, Decimal("5"))
        self.assertEqual(len(parsed_data.path), 2)
        self.assertEqual(parsed_data.path[0].asset_type, "native")
        self.assertEqual(parsed_data.path[0].asset_code, None)
        self.assertEqual(parsed_data.path[0].asset_issuer, None)
        self.assertEqual(parsed_data.path[1].asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.path[1].asset_code, "USD")
        self.assertEqual(
            parsed_data.path[1].asset_issuer,
            "GDUKMGUGDZQK6YHYA5Z6AY2G4XDSZPSZ3SW5UN3ARVMO6QSRDWP5YLEX",
        )


if __name__ == "__main__":
    unittest.main()
