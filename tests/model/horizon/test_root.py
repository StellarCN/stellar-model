import datetime
import unittest

from stellar_model.model.horizon.root import Root
from tests.model.horizon import load_horizon_file


class TestRoot(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("root.json")
        parsed_data = Root.parse_obj(raw_data)
        self.assertEqual(
            parsed_data.horizon_version,
            "2.2.0-7d7e58007af55e7697223009fd24daf76aa908e2",
        )
        self.assertEqual(
            parsed_data.core_version,
            "stellar-core 16.0.0 (0e35ac6ef382391096dbe4443197051452a3ce50)",
        )
        self.assertEqual(parsed_data.ingest_latest_ledger, 35075520)
        self.assertEqual(parsed_data.history_latest_ledger, 35075520)
        self.assertEqual(
            parsed_data.history_latest_ledger_closed_at,
            datetime.datetime(2021, 4, 24, 1, 31, 8, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.history_elder_ledger, 2)
        self.assertEqual(parsed_data.core_latest_ledger, 35075520)
        self.assertEqual(
            parsed_data.network_passphrase,
            "Public Global Stellar Network ; September 2015",
        )
        self.assertEqual(parsed_data.current_protocol_version, 16)
        self.assertEqual(parsed_data.core_supported_protocol_version, 16)
        self.assertEqual(parsed_data.links.self.href, "https://horizon.stellar.org/")
        self.assertEqual(parsed_data.links.self.templated, None)


if __name__ == "__main__":
    unittest.main()
