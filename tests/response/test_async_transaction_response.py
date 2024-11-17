import unittest

from stellar_model.response.async_transaction_response import AsyncTransactionResponse
from tests.model.horizon import load_horizon_file


class TestAsyncTransactionResponse(unittest.TestCase):
    def test_pending(self):
        raw_data = load_horizon_file("async_transaction_pending.json")
        parsed_data = AsyncTransactionResponse.model_validate(raw_data)
        self.assertEqual(parsed_data.error_result_xdr, None)
        self.assertEqual(parsed_data.tx_status, "PENDING")
        self.assertEqual(
            parsed_data.hash,
            "7dfaa088db9a220568bb520649a52fe66de8ae4d18d7bf06c8c1544e85a29f60",
        )

    def test_error(self):
        raw_data = load_horizon_file("async_transaction_error.json")
        parsed_data = AsyncTransactionResponse.model_validate(raw_data)
        self.assertEqual(parsed_data.error_result_xdr, "AAAAAAAAAGT////9AAAAAA==")
        self.assertEqual(parsed_data.tx_status, "ERROR")
        self.assertEqual(
            parsed_data.hash,
            "267a9d1b5faac774c6f74ee059b28d63cb2f6880c0f75be90415cd392327af88",
        )


if __name__ == "__main__":
    unittest.main()
