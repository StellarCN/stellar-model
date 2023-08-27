from unittest import TestCase

from stellar_model import OperationsResponse
from stellar_model.model.horizon.operations import *
from tests.response import load_response_file


ops = {
    "create_account": CreateAccountOperation,
    "payment": PaymentOperation,
    "path_payment_strict_receive": PathPaymentStrictReceiveOperation,
    "manage_sell_offer": ManageSellOfferOperation,
    "create_passive_sell_offer": CreatePassiveSellOfferOperation,
    "set_options": SetOptionsOperation,
    "change_trust": ChangeTrustOperation,
    "allow_trust": AllowTrustOperation,
    "account_merge": AccountMergeOperation,
    "inflation": InflationOperation,
    "manage_data": ManageDataOperation,
    "bump_sequence": BumpSequenceOperation,
    "manage_buy_offer": ManageBuyOfferOperation,
    "path_payment_strict_send": PathPaymentStrictSendOperation,
    "create_claimable_balance": CreateClaimableBalanceOperation,
    "claim_claimable_balance": ClaimClaimableBalanceOperation,
    "begin_sponsoring_future_reserves": BeginSponsoringFutureReservesOperation,
    "end_sponsoring_future_reserves": EndSponsoringFutureReservesOperation,
    "revoke_sponsorship": RevokeSponsorshipOperation,
    "clawback": ClawbackOperation,
    "clawback_claimable_balance": ClawbackClaimableBalanceOperation,
    "set_trust_line_flags": SetTrustLineFlagsOperation,
}


class TestOperationsResponse(TestCase):
    def test_valid(self):
        raw_data = load_response_file("operations_response.json")
        parsed_data = OperationsResponse.model_validate(raw_data)
        self.assertEqual(len(parsed_data.embedded.records), 18)
        for record in parsed_data.embedded.records:
            self.assertTrue(record.type in ops)
            class_type = ops[record.type]
            self.assertTrue(isinstance(record, class_type))

        self.assertEqual(
            parsed_data.links.self.href,
            "https://horizon.stellar.org/operations?cursor=&include_failed=true&limit=1&order=desc",
        )
        self.assertEqual(parsed_data.links.self.templated, None)
        self.assertEqual(
            parsed_data.links.next.href,
            "https://horizon.stellar.org/operations?cursor=150724090477830145&include_failed=true&limit=1&order=desc",
        )
        self.assertEqual(parsed_data.links.next.templated, None)
        self.assertEqual(
            parsed_data.links.prev.href,
            "https://horizon.stellar.org/operations?cursor=150724090477830145&include_failed=true&limit=1&order=asc",
        )
        self.assertEqual(parsed_data.links.prev.templated, None)
