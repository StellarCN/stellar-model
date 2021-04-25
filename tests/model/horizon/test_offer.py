import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.offer import Offer
from tests.model.horizon import load_horizon_file


class TestOffer(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("offer.json")
        parsed_data = Offer.parse_obj(raw_data)
        self.assertEqual(parsed_data.id, "544689347")
        self.assertEqual(parsed_data.paging_token, "544689347")
        self.assertEqual(
            parsed_data.seller,
            "GBB7HYFEUJLJLABG7EGSY54HM3QISTVCS4O3EANIGX5YFCOJK7A6MZAA",
        )
        self.assertEqual(parsed_data.selling.asset_type, "native")
        self.assertEqual(parsed_data.selling.asset_code, None)
        self.assertEqual(parsed_data.selling.asset_issuer, None)
        self.assertEqual(parsed_data.buying.asset_type, "credit_alphanum4")
        self.assertEqual(parsed_data.buying.asset_code, "SLVR")
        self.assertEqual(
            parsed_data.buying.asset_issuer,
            "GBZVELEQD3WBN3R3VAG64HVBDOZ76ZL6QPLSFGKWPFED33Q3234NSLVR",
        )
        self.assertEqual(parsed_data.amount, Decimal("677.1953280"))
        self.assertEqual(parsed_data.price_r.n, 10000000)
        self.assertEqual(parsed_data.price_r.d, 17500001)
        self.assertEqual(parsed_data.price, Decimal("0.5714285"))
        self.assertEqual(parsed_data.last_modified_ledger, 35067578)
        self.assertEqual(
            parsed_data.last_modified_time,
            datetime.datetime(2021, 4, 23, 13, 34, 40, tzinfo=datetime.timezone.utc),
        )


if __name__ == "__main__":
    unittest.main()
