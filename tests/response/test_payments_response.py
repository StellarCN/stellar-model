from unittest import TestCase

from stellar_model import PaymentsResponse
from stellar_model.model.horizon.operations import *
from tests.response import load_response_file


payment_ops = {
    "create_account": CreateAccountOperation,
    "payment": PaymentOperation,
    "account_merge": AccountMergeOperation,
    "path_payment_strict_send": PathPaymentStrictSendOperation,
    "path_payment_strict_receive": PathPaymentStrictReceiveOperation,
}


class TestPaymentsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("payments_response.json")
        parsed_data = PaymentsResponse.parse_obj(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 100)
        for record in parsed_data.embedded.records:
            self.assertTrue(record.type in payment_ops)
            class_type = payment_ops[record.type]
            self.assertTrue(isinstance(record, class_type), record)

        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/payments?cursor=&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/payments?cursor=150721723950796801&limit=100&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/payments?cursor=150721758310514689&limit=100&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
