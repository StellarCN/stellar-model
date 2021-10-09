from datetime import datetime
from decimal import Decimal
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.claimable_balance import ClaimPredicate
from stellar_model.model.horizon.link import Link


__all__ = [
    "AccountCreatedEffect",
    "AccountRemovedEffect",
    "AccountCreditedEffect",
    "AccountDebitedEffect",
    "AccountThresholdsUpdatedEffect",
    "AccountHomeDomainUpdatedEffect",
    "AccountFlagsUpdatedEffect",
    "AccountInflationDestinationUpdatedEffect",
    "SignerCreatedEffect",
    "SignerRemovedEffect",
    "SignerUpdatedEffect",
    "TrustlineCreatedEffect",
    "TrustlineRemovedEffect",
    "TrustlineUpdatedEffect",
    "TrustlineAuthorizedEffect",
    "TrustlineDeauthorizedEffect",
    "TrustlineAuthorizedToMaintainLiabilitiesEffect",
    "TrustlineFlagsUpdatedEffect",
    "OfferCreatedEffect",
    "OfferRemovedEffect",
    "OfferUpdatedEffect",
    "TradeEffect",
    "DataCreatedEffect",
    "DataRemovedEffect",
    "DataUpdatedEffect",
    "SequenceBumpedEffect",
    "ClaimableBalanceCreatedEffect",
    "ClaimableBalanceClaimantCreatedEffect",
    "ClaimableBalanceClaimedEffect",
    "AccountSponsorshipCreatedEffect",
    "AccountSponsorshipUpdatedEffect",
    "AccountSponsorshipRemovedEffect",
    "TrustlineSponsorshipCreatedEffect",
    "TrustlineSponsorshipUpdatedEffect",
    "TrustlineSponsorshipRemovedEffect",
    "DataSponsorshipCreatedEffect",
    "DataSponsorshipUpdatedEffect",
    "DataSponsorshipRemovedEffect",
    "ClaimableBalanceSponsorshipCreatedEffect",
    "ClaimableBalanceSponsorshipUpdatedEffect",
    "ClaimableBalanceSponsorshipRemovedEffect",
    "SignerSponsorshipCreatedEffect",
    "SignerSponsorshipUpdatedEffect",
    "SignerSponsorshipRemovedEffect",
    "ClaimableBalanceClawedBackEffect",
    "LiquidityPoolDepositedEffect",
    "LiquidityPoolWithdrewEffect",
    "LiquidityPoolTradeEffect",
    "LiquidityPoolCreatedEffect",
    "LiquidityPoolRemovedEffect",
    "LiquidityPoolRevokedEffect",
]

from stellar_model.model.horizon.liquidity_pool_asset_amount import (
    LiquidityPoolAssetAmount,
)


class Links(BaseModel):
    operation: Link
    succeeds: Link
    precedes: Link


class BaseEffect(BaseModel):
    """
    Represents the common attributes of an effect resource.
    """

    id: str
    paging_token: str
    account: str
    account_muxed: Optional[str]
    account_muxed_id: Optional[int]
    type: str
    type_i: int
    # The maximum year in Python is 9999
    # https://horizon.stellar.org/transactions/8761d590f853174b42c7d8e5e1a274a6dfd786091d1776eaf61965920346e9b8
    created_at: datetime
    links: Links = Field(alias="_links")


class AccountCreatedEffect(BaseEffect):
    """
    Effects occur when a new account is created.

    type: account_created
    type_i: 0
    """

    starting_balance: Decimal


class AccountRemovedEffect(BaseEffect):
    """
    Effects occur when one account is merged into another.

    type: account_removed
    type_i: 1
    """


class AccountCreditedEffect(BaseEffect):
    """
    Effects occur when an account receives some currency.

    type: account_credited
    type_i: 2
    """

    asset_type: str
    asset_code: Optional[str]
    asset_issuer: Optional[str]
    amount: Decimal


class AccountDebitedEffect(BaseEffect):
    """
    Effects occur when an account sends some currency.

    type: account_debited
    type_i: 3
    """

    asset_type: str
    asset_code: Optional[str]
    asset_issuer: Optional[str]
    amount: Decimal


class AccountThresholdsUpdatedEffect(BaseEffect):
    """
    Effects occur when an account changes its multisig thresholds.

    type: account_thresholds_updated
    type_i: 4
    """

    low_threshold: int
    med_threshold: int
    high_threshold: int


class AccountHomeDomainUpdatedEffect(BaseEffect):
    """
    Effects occur when an account changes its home domain.

    type: account_home_domain_updated
    type_i: 5
    """

    home_domain: str


class AccountFlagsUpdatedEffect(BaseEffect):
    """
    Effects occur when an account changes its account flags,
    either clearing or setting.

    type: account_flags_updated
    type_i: 6
    """

    auth_required_flag: Optional[bool]
    auth_revokable_flag: Optional[bool]


class AccountInflationDestinationUpdatedEffect(BaseEffect):
    """
    Effects occur when an account changes its inflation destination.

    type: account_inflation_destination_updated
    type_i: 7
    """


class SignerCreatedEffect(BaseEffect):
    """
    Occurs when an account gains a signer.

    type: signer_created
    type_i:n10
    """

    weight: int
    public_key: str
    key: str


class SignerRemovedEffect(BaseEffect):
    """
    Occurs when an account loses a signer.

    type: signer_removed
    type_i: 11
    """

    weight: int
    public_key: str
    key: str


class SignerUpdatedEffect(BaseEffect):
    """
    Occurs when an account changes the weight of one of its signers.

    type: signer_updated
    type_i: 12
    """

    weight: int
    public_key: str
    key: str


# In my opinion asset_code should not be optional in trustline,
# but it is optional in the source code of Horizon.
class TrustlineCreatedEffect(BaseEffect):
    """
    Occurs when an account trusts an anchor.

    type: trustline_created
    type_i: 20
    """

    asset_type: str
    asset_code: Optional[str]
    asset_issuer: Optional[str]
    liquidity_pool_id: Optional[str]
    limit: Decimal


class TrustlineRemovedEffect(BaseEffect):
    """
    Occurs when an account removes struct by setting the limit of a trustline to 0.

    type: trustline_removed
    type_i: 21
    """

    asset_type: str
    asset_code: Optional[str]
    asset_issuer: Optional[str]
    liquidity_pool_id: Optional[str]
    limit: Decimal


class TrustlineUpdatedEffect(BaseEffect):
    """
    Occurs when an account changes a trustline's limit.

    type: trustline_updated
    type_i: 22
    """

    asset_type: str
    asset_code: Optional[str]
    asset_issuer: Optional[str]
    liquidity_pool_id: Optional[str]
    limit: Decimal


class TrustlineAuthorizedEffect(BaseEffect):
    """
    Occurs when an anchor has AUTH_REQUIRED flag set to true and it
    authorizes another account's trustline.

    type: trustline_authorized
    type_i: 23
    """

    trustor: str
    asset_type: str
    asset_code: str


class TrustlineDeauthorizedEffect(BaseEffect):
    """
    Occurs when an anchor revokes access to a asset it issues.

    type: trustline_deauthorized
    type_i: 24
    """

    trustor: str
    asset_type: str
    asset_code: str


class TrustlineAuthorizedToMaintainLiabilitiesEffect(BaseEffect):
    """
    Occurs when an anchor has AUTH_REQUIRED flag set to true and it
    authorizes another account's trustline to maintain liabilities.

    type: trustline_authorized_to_maintain_liabilities
    type_i: 25
    """

    trustor: str
    asset_type: str
    asset_code: str


class TrustlineFlagsUpdatedEffect(BaseEffect):
    """
    Effects occur when a TrustLine changes its flags, either clearing or setting.

    type: trustline_flags_updated
    type_i: 26
    """

    asset_type: str
    asset_code: str
    asset_issuer: str
    trustor: str
    authorized_flag: Optional[bool]
    authorized_to_maintain_liabilites_flag: Optional[bool]
    clawback_enabled_flag: Optional[bool]


class OfferCreatedEffect(BaseEffect):
    """
    Occurs when an account offers to trade an asset.

    type: offer_created
    type_i: 30
    """


class OfferRemovedEffect(BaseEffect):
    """
    Occurs when an account removes an offer.

    type: offer_removed
    type_i: 31
    """


class OfferUpdatedEffect(BaseEffect):
    """
    Occurs when an offer is updated by the offering account.

    type: offer_updated
    type_i: 32
    """


class TradeEffect(BaseEffect):
    """
    Occurs when a trade is initiated because of a path payment or offer operations.

    type: trade
    type_i: 33
    """

    seller: str
    seller_muxed: Optional[str]
    seller_muxed_id: Optional[int]
    offer_id: str
    sold_amount: Decimal
    sold_asset_type: str
    sold_asset_code: Optional[str]
    sold_asset_issuer: Optional[str]
    bought_amount: Decimal
    bought_asset_type: str
    bought_asset_code: Optional[str]
    bought_asset_issuer: Optional[str]


class DataCreatedEffect(BaseEffect):
    """
    Occurs when an account gets a new data field.

    type: data_created
    type_i: 40
    """

    name: str
    value: str


class DataRemovedEffect(BaseEffect):
    """
    Occurs when an account removes a data field.

    type: data_removed
    type_i: 41
    """

    name: str


class DataUpdatedEffect(BaseEffect):
    """
    Occurs when an account changes a data field's value.

    type: data_updated
    type_i: 42
    """

    name: str
    value: str


class SequenceBumpedEffect(BaseEffect):
    """
    Occurs when an account bumps their sequence number.

    type: sequence_bumped
    type_i: 43
    """

    new_seq: int


class ClaimableBalanceCreatedEffect(BaseEffect):
    """
    Occurs when a claimable balance is created.

    type: claimable_balance_created
    type_i: 50
    """

    asset: str
    balance_id: str
    amount: Decimal


class ClaimableBalanceClaimantCreatedEffect(BaseEffect):
    """
    Occurs when a claimable balance claimant is created.

    type: claimable_balance_claimant_created
    type_i: 51
    """

    asset: str
    balance_id: str
    amount: Decimal
    predicate: ClaimPredicate


class ClaimableBalanceClaimedEffect(BaseEffect):
    """
    Occurs when a claimable balance is claimed.

    type: claimable_balance_claimed
    type_i: 52
    """

    asset: str
    balance_id: str
    amount: Decimal


class AccountSponsorshipCreatedEffect(BaseEffect):
    """
    Occurs when an account ledger entry is sponsored.

    type: account_sponsorship_created
    type_i: 60
    """

    sponsor: str


class AccountSponsorshipUpdatedEffect(BaseEffect):
    """
    Occurs when the sponsoring of an account ledger entry is updated.

    type: account_sponsorship_updated
    type_i: 61
    """

    former_sponsor: str
    new_sponsor: str


class AccountSponsorshipRemovedEffect(BaseEffect):
    """
    Occurs when the sponsorship of an account ledger entry is removed.

    type: account_sponsorship_removed
    type_i: 62
    """

    former_sponsor: str


class TrustlineSponsorshipCreatedEffect(BaseEffect):
    """
    Occurs when a trustline ledger entry is sponsored.

    type: trustline_sponsorship_created
    type_i: 63
    """

    asset_type: str
    asset: Optional[str]
    liquidity_pool_id: Optional[str]
    sponsor: str


class TrustlineSponsorshipUpdatedEffect(BaseEffect):
    """
    Occurs when the sponsoring of a trustline ledger entry is updated.

    type: trustline_sponsorship_updated
    type_i: 64
    """

    asset_type: str
    asset: Optional[str]
    liquidity_pool_id: Optional[str]
    former_sponsor: str
    new_sponsor: str


class TrustlineSponsorshipRemovedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a trustline ledger entry is removed.

    type: trustline_sponsorship_removed
    type_i: 65
    """

    asset_type: str
    asset: Optional[str]
    liquidity_pool_id: Optional[str]
    former_sponsor: str


class DataSponsorshipCreatedEffect(BaseEffect):
    """
    Occurs when a trustline ledger entry is sponsored.

    type: data_sponsorship_created
    type_i: 66
    """

    data_name: str
    sponsor: str


class DataSponsorshipUpdatedEffect(BaseEffect):
    """
    Occurs when the sponsoring of a trustline ledger entry is updated.

    type: data_sponsorship_updated
    type_i: 67
    """

    data_name: str
    former_sponsor: str
    new_sponsor: str


class DataSponsorshipRemovedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a trustline ledger entry is removed.

    type: data_sponsorship_removed
    type_i: 68
    """

    data_name: str
    former_sponsor: str


class ClaimableBalanceSponsorshipCreatedEffect(BaseEffect):
    """
    Occurs when a claimable balance ledger entry is sponsored.

    type: claimable_balance_sponsorship_created
    type_i: 69
    """

    balance_id: str
    sponsor: str


class ClaimableBalanceSponsorshipUpdatedEffect(BaseEffect):
    """
    Occurs when the sponsoring of a claimable balance ledger entry is updated.

    type: claimable_balance_sponsorship_updated
    type_i: 70
    """

    balance_id: str
    former_sponsor: str
    new_sponsor: str


class ClaimableBalanceSponsorshipRemovedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a claimable balance ledger entry is removed.

    type: claimable_balance_sponsorship_removed
    type_i: 71
    """

    balance_id: str
    former_sponsor: str


class SignerSponsorshipCreatedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a signer is created.

    type: signer_sponsorship_created
    type_i: 72
    """

    signer: str
    sponsor: str


class SignerSponsorshipUpdatedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a signer is updated.

    type: signer_sponsorship_updated
    type_i: 73
    """

    signer: str
    former_sponsor: str
    new_sponsor: str


class SignerSponsorshipRemovedEffect(BaseEffect):
    """
    Occurs when the sponsorship of a signer is removed.

    type: signer_sponsorship_removed
    type_i: 74
    """

    signer: str
    former_sponsor: str


class ClaimableBalanceClawedBackEffect(BaseEffect):
    """
    Occurs when a claimable balance is clawed back.

    type: claimable_balance_clawed_back
    type_i: 80
    """

    balance_id: str


class LiquidityPool(BaseModel):
    id: str
    fee_bp: int
    type: str
    total_trustlines: int
    total_shares: Decimal
    reserves: List[LiquidityPoolAssetAmount]


class LiquidityPoolDepositedEffect(BaseEffect):
    """
    Occurs when a liquidity pool incurs a deposit

    type: liquidity_pool_deposited
    type_i: 90
    """

    liquidity_pool: LiquidityPool
    reserves_deposited: List[LiquidityPoolAssetAmount]
    shares_received: Decimal


class LiquidityPoolWithdrewEffect(BaseEffect):
    """
    Occurs when a liquidity pool incurs a withdrawal

    type: liquidity_pool_withdrew
    type_i: 91
    """

    liquidity_pool: LiquidityPool
    reserves_received: List[LiquidityPoolAssetAmount]
    shares_redeemed: Decimal


class LiquidityPoolTradeEffect(BaseEffect):
    """
    Occurs when a trade happens in a liquidity pool

    type: liquidity_pool_trade
    type_i: 92
    """

    liquidity_pool: LiquidityPool
    sold: LiquidityPoolAssetAmount
    bought: LiquidityPoolAssetAmount


class LiquidityPoolCreatedEffect(BaseEffect):
    """
    Occurs when a liquidity pool is created

    type: liquidity_pool_created
    type_i: 93
    """

    liquidity_pool: LiquidityPool


class LiquidityPoolRemovedEffect(BaseEffect):
    """
    Occurs when a liquidity pool is removed

    type: liquidity_pool_removed
    type_i: 94
    """

    liquidity_pool: LiquidityPool


class LiquidityPoolClaimableAssetAmount(LiquidityPoolAssetAmount):
    claimable_balance_id: str


class LiquidityPoolRevokedEffect(BaseEffect):
    """
    Occurs when a liquidity pool is revoked

    type: liquidity_pool_revoked
    type_i: 95
    """

    liquidity_pool: LiquidityPool
    reserves_revoked: List[LiquidityPoolClaimableAssetAmount]
    shares_revoked: Decimal


_EFFECT_TYPE_I_MAP = {
    0: AccountCreatedEffect,
    1: AccountRemovedEffect,
    2: AccountCreditedEffect,
    3: AccountDebitedEffect,
    4: AccountThresholdsUpdatedEffect,
    5: AccountHomeDomainUpdatedEffect,
    6: AccountFlagsUpdatedEffect,
    7: AccountInflationDestinationUpdatedEffect,
    10: SignerCreatedEffect,
    11: SignerRemovedEffect,
    12: SignerUpdatedEffect,
    20: TrustlineCreatedEffect,
    21: TrustlineRemovedEffect,
    22: TrustlineUpdatedEffect,
    23: TrustlineAuthorizedEffect,
    24: TrustlineDeauthorizedEffect,
    25: TrustlineAuthorizedToMaintainLiabilitiesEffect,
    26: TrustlineFlagsUpdatedEffect,
    30: OfferCreatedEffect,
    31: OfferRemovedEffect,
    32: OfferUpdatedEffect,
    33: TradeEffect,
    40: DataCreatedEffect,
    41: DataRemovedEffect,
    42: DataUpdatedEffect,
    43: SequenceBumpedEffect,
    50: ClaimableBalanceCreatedEffect,
    51: ClaimableBalanceClaimantCreatedEffect,
    52: ClaimableBalanceClaimedEffect,
    60: AccountSponsorshipCreatedEffect,
    61: AccountSponsorshipUpdatedEffect,
    62: AccountSponsorshipRemovedEffect,
    63: TrustlineSponsorshipCreatedEffect,
    64: TrustlineSponsorshipUpdatedEffect,
    65: TrustlineSponsorshipRemovedEffect,
    66: DataSponsorshipCreatedEffect,
    67: DataSponsorshipUpdatedEffect,
    68: DataSponsorshipRemovedEffect,
    69: ClaimableBalanceSponsorshipCreatedEffect,
    70: ClaimableBalanceSponsorshipUpdatedEffect,
    71: ClaimableBalanceSponsorshipRemovedEffect,
    72: SignerSponsorshipCreatedEffect,
    73: SignerSponsorshipUpdatedEffect,
    74: SignerSponsorshipRemovedEffect,
    80: ClaimableBalanceClawedBackEffect,
    90: LiquidityPoolDepositedEffect,
    91: LiquidityPoolWithdrewEffect,
    92: LiquidityPoolTradeEffect,
    93: LiquidityPoolCreatedEffect,
    94: LiquidityPoolRemovedEffect,
    95: LiquidityPoolRevokedEffect,
}

_EFFECT_TYPE_UNION = Union[
    AccountCreatedEffect,
    AccountRemovedEffect,
    AccountCreditedEffect,
    AccountDebitedEffect,
    AccountThresholdsUpdatedEffect,
    AccountHomeDomainUpdatedEffect,
    AccountFlagsUpdatedEffect,
    AccountInflationDestinationUpdatedEffect,
    SignerCreatedEffect,
    SignerRemovedEffect,
    SignerUpdatedEffect,
    TrustlineCreatedEffect,
    TrustlineRemovedEffect,
    TrustlineUpdatedEffect,
    TrustlineAuthorizedEffect,
    TrustlineDeauthorizedEffect,
    TrustlineAuthorizedToMaintainLiabilitiesEffect,
    TrustlineFlagsUpdatedEffect,
    OfferCreatedEffect,
    OfferRemovedEffect,
    OfferUpdatedEffect,
    TradeEffect,
    DataCreatedEffect,
    DataRemovedEffect,
    DataUpdatedEffect,
    SequenceBumpedEffect,
    ClaimableBalanceCreatedEffect,
    ClaimableBalanceClaimantCreatedEffect,
    ClaimableBalanceClaimedEffect,
    AccountSponsorshipCreatedEffect,
    AccountSponsorshipUpdatedEffect,
    AccountSponsorshipRemovedEffect,
    TrustlineSponsorshipCreatedEffect,
    TrustlineSponsorshipUpdatedEffect,
    TrustlineSponsorshipRemovedEffect,
    DataSponsorshipCreatedEffect,
    DataSponsorshipUpdatedEffect,
    DataSponsorshipRemovedEffect,
    ClaimableBalanceSponsorshipCreatedEffect,
    ClaimableBalanceSponsorshipUpdatedEffect,
    ClaimableBalanceSponsorshipRemovedEffect,
    SignerSponsorshipCreatedEffect,
    SignerSponsorshipUpdatedEffect,
    SignerSponsorshipRemovedEffect,
    ClaimableBalanceClawedBackEffect,
    LiquidityPoolDepositedEffect,
    LiquidityPoolWithdrewEffect,
    LiquidityPoolTradeEffect,
    LiquidityPoolCreatedEffect,
    LiquidityPoolRemovedEffect,
    LiquidityPoolRevokedEffect,
]
