from unittest import TestCase

from stellar_model import ErrorResponse
from tests.response import load_response_file


class TestErrorResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("error_response.json")
        parsed_data = ErrorResponse.parse_obj(raw_data)
        self.assertEqual(
            parsed_data.type, "https://stellar.org/horizon-errors/transaction_failed"
        )
        self.assertEqual(parsed_data.title, "Transaction Failed")
        self.assertEqual(parsed_data.status, 400)
        self.assertEqual(
            parsed_data.detail,
            "The transaction failed when submitted to the stellar network. The `extras.result_codes` field on this response contains further details.  Descriptions of each code can be found at: https://www.stellar.org/developers/guides/concepts/list-of-operations.html",
        )
        self.assertTrue(isinstance(parsed_data.extras, dict))
