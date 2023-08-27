from unittest import TestCase

from stellar_model import OperationResponse
from stellar_model.model.horizon.operations import *
from tests.response import load_horizon_file


ops = [
    {"filename": "create_account.json", "class": CreateAccountOperation},
    {"filename": "payment.json", "class": PaymentOperation},
    {
        "filename": "path_payment_strict_receive.json",
        "class": PathPaymentStrictReceiveOperation,
    },
    {"filename": "manage_sell_offer.json", "class": ManageSellOfferOperation},
    {
        "filename": "create_passive_sell_offer.json",
        "class": CreatePassiveSellOfferOperation,
    },
    {"filename": "set_options.json", "class": SetOptionsOperation},
    {"filename": "change_trust_asset.json", "class": ChangeTrustOperation},
    {"filename": "change_trust_liquidity_pool_id.json", "class": ChangeTrustOperation},
    {"filename": "allow_trust.json", "class": AllowTrustOperation},
    {"filename": "account_merge.json", "class": AccountMergeOperation},
    # {'filename': 'inflation.json', 'class': InflationOperation},
    {"filename": "manage_data.json", "class": ManageDataOperation},
    {"filename": "bump_sequence.json", "class": BumpSequenceOperation},
    {"filename": "manage_buy_offer.json", "class": ManageBuyOfferOperation},
    {
        "filename": "path_payment_strict_send.json",
        "class": PathPaymentStrictSendOperation,
    },
    {
        "filename": "create_claimable_balance.json",
        "class": CreateClaimableBalanceOperation,
    },
    {
        "filename": "claim_claimable_balance.json",
        "class": ClaimClaimableBalanceOperation,
    },
    {
        "filename": "begin_sponsoring_future_reserves.json",
        "class": BeginSponsoringFutureReservesOperation,
    },
    {
        "filename": "end_sponsoring_future_reserves.json",
        "class": EndSponsoringFutureReservesOperation,
    },
    {"filename": "revoke_sponsorship.json", "class": RevokeSponsorshipOperation},
    # {'filename': 'clawback.json', 'class': ClawbackOperation},
    # {'filename': 'clawback_claimable_balance.json', 'class': ClawbackClaimableBalanceOperation},
    # {'filename': 'set_trust_line_flags.json', 'class': SetTrustLineFlagsOperation}
]


class TestOperationResponse(TestCase):
    def test_valid(self):
        for op in ops:
            raw_data = load_horizon_file(f"operations/{op['filename']}")
            parsed_data = OperationResponse.model_validate(raw_data)
            self.assertTrue(isinstance(parsed_data, OperationResponse))
            self.assertTrue(isinstance(parsed_data.record, op["class"]))
            self.assertEqual(raw_data["id"], parsed_data.record.id)
