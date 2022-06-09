from unittest import TestCase

from stellar_model import EffectResponse
from stellar_model.model.horizon.effects import *
from tests.response import load_horizon_file


ops = [
    {"filename": "account_created.json", "class": AccountCreatedEffect},
    {"filename": "account_removed.json", "class": AccountRemovedEffect},
    {"filename": "account_credited.json", "class": AccountCreditedEffect},
    {"filename": "account_debited.json", "class": AccountDebitedEffect},
    {"filename": "account_thresholds_updated.json", "class": AccountThresholdsUpdatedEffect},
    {"filename": "account_home_domain_updated.json", "class": AccountHomeDomainUpdatedEffect},
    {"filename": "account_flags_updated.json", "class": AccountFlagsUpdatedEffect},
    {"filename": "account_inflation_destination_updated.json", "class": AccountInflationDestinationUpdatedEffect},
    {"filename": "signer_created.json", "class": SignerCreatedEffect},
    {"filename": "signer_removed.json", "class": SignerRemovedEffect},
    {"filename": "signer_updated.json", "class": SignerUpdatedEffect},
    {"filename": "trustline_created.json", "class": TrustlineCreatedEffect},
    {"filename": "trustline_removed.json", "class": TrustlineRemovedEffect},
    {"filename": "trustline_updated.json", "class": TrustlineUpdatedEffect},
    {"filename": "trustline_authorized.json", "class": TrustlineAuthorizedEffect},
    {"filename": "trustline_deauthorized.json", "class": TrustlineDeauthorizedEffect},
    {"filename": "trustline_authorized_to_maintain_liabilities.json", "class": TrustlineAuthorizedToMaintainLiabilitiesEffect},
    {"filename": "trustline_flags_updated.json", "class": TrustlineFlagsUpdatedEffect},
    {"filename": "trade.json", "class": TradeEffect},
    {"filename": "data_created.json", "class": DataCreatedEffect},
    {"filename": "data_removed.json", "class": DataRemovedEffect},
    {"filename": "data_updated.json", "class": DataUpdatedEffect},
    {"filename": "sequence_bumped.json", "class": SequenceBumpedEffect},
    {"filename": "claimable_balance_created.json", "class": ClaimableBalanceCreatedEffect},
    {"filename": "claimable_balance_claimed.json", "class": ClaimableBalanceClaimedEffect},
    {"filename": "claimable_balance_claimant_created.json", "class": ClaimableBalanceClaimantCreatedEffect},
    {"filename": "claimable_balance_clawed_back.json", "class": ClaimableBalanceClawedBackEffect},
    {"filename": "claimable_balance_sponsorship_created.json", "class": ClaimableBalanceSponsorshipCreatedEffect},
    {"filename": "claimable_balance_sponsorship_removed.json", "class": ClaimableBalanceSponsorshipRemovedEffect},
    {"filename": "account_sponsorship_created.json", "class": AccountSponsorshipCreatedEffect},
    {"filename": "account_sponsorship_removed.json", "class": AccountSponsorshipRemovedEffect},
    {"filename": "trustline_sponsorship_created.json", "class": TrustlineSponsorshipCreatedEffect},
    {"filename": "trustline_sponsorship_removed.json", "class": TrustlineSponsorshipRemovedEffect},
    {"filename": "data_sponsorship_created.json", "class": DataSponsorshipCreatedEffect},
    {"filename": "data_sponsorship_removed.json", "class": DataSponsorshipRemovedEffect},
    {"filename": "signer_sponsorship_created.json", "class": SignerSponsorshipCreatedEffect},
    {"filename": "signer_sponsorship_removed.json", "class": SignerSponsorshipRemovedEffect},
    {"filename": "liquidity_pool_deposited.json", "class": LiquidityPoolDepositedEffect},
    {"filename": "liquidity_pool_withdrew.json", "class": LiquidityPoolWithdrewEffect},
    {"filename": "liquidity_pool_created.json", "class": LiquidityPoolCreatedEffect},
    {"filename": "liquidity_pool_trade.json", "class": LiquidityPoolTradeEffect},
]


class TestEffectResponse(TestCase):
    def test_valid(self):
        for op in ops:
            raw_data = load_horizon_file(f"effects/{op['filename']}")
            parsed_data = EffectResponse.parse_obj(raw_data)
            self.assertTrue(isinstance(parsed_data, EffectResponse))
            self.assertTrue(isinstance(parsed_data.record, op["class"]))
            self.assertEqual(raw_data["id"], parsed_data.record.id)
