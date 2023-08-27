import datetime
import unittest

from decimal import Decimal

from stellar_model.model.horizon.ledger import Ledger
from tests.model.horizon import load_horizon_file


class TestLedger(unittest.TestCase):
    def test_valid(self):
        raw_data = load_horizon_file("ledger.json")
        parsed_data = Ledger.model_validate(raw_data)
        self.assertEqual(
            parsed_data.id,
            "548393ec23959e1959a62f003029ecf96be89e13df036073bf64918996ec4227",
        )
        self.assertEqual(parsed_data.paging_token, "115352659677937664")
        self.assertEqual(
            parsed_data.hash,
            "548393ec23959e1959a62f003029ecf96be89e13df036073bf64918996ec4227",
        )
        self.assertEqual(
            parsed_data.prev_hash,
            "446d6eca81dd6db6daf50d93ca9d297bd60b1233b91de3765cccdf503cfffcb0",
        )
        self.assertEqual(parsed_data.sequence, 26857634)
        self.assertEqual(parsed_data.successful_transaction_count, 27)
        self.assertEqual(parsed_data.failed_transaction_count, 1)
        self.assertEqual(parsed_data.operation_count, 133)
        self.assertEqual(parsed_data.tx_set_operation_count, 134)
        self.assertEqual(
            parsed_data.closed_at,
            datetime.datetime(2019, 11, 18, 19, 27, 21, tzinfo=datetime.timezone.utc),
        )
        self.assertEqual(parsed_data.total_coins, Decimal("105443902087.3472865"))
        self.assertEqual(parsed_data.fee_pool, Decimal("1807038.9789761"))
        self.assertEqual(parsed_data.base_fee_in_stroops, 100)
        self.assertEqual(parsed_data.base_reserve_in_stroops, 5000000)
        self.assertEqual(parsed_data.max_tx_set_size, 1000)
        self.assertEqual(parsed_data.protocol_version, 12)
        self.assertEqual(
            parsed_data.header_xdr,
            "AAAADERtbsqB3W222vUNk8qdKXvWCxIzuR3jdlzM31A8//ywoQieYsSc05/BpgEqnLR7fKXz7t0K42V7NOjbGZA/wTEAAAAAXdLwmQAAAAAAAAAAplf68mTg/Z/DDyEZeLCoNbJnMZm4SYsYWjUjuDOSfPeRNFE4n9Hm19yKutjwVurFjk72JKVHI8J+ELwLZgWsywGZ0KIOoh6z7HlbYQAAEG9XKhRBAAABFgAAAAAH9M6YAAAAZABMS0AAAAPop9+CeMs1/7BHgFltiQPH+VT+ACYb5P0lSXh7RpBLtd34kEpeL8qKJxYz4ufmkQ2lEv/HMR/i3bi1Rt0PYj185/0kAZ3ZRbmm2mVRMzmaCOak1rn2vejHXDh+MGlr6D6vI2tc/M6VIumTKUa7SgumWDyW0r5FcJTbu/FXDQ/6C4YAAAAA",
        )


if __name__ == "__main__":
    unittest.main()
