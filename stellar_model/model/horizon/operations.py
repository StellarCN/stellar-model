from datetime import datetime
from decimal import Decimal
from typing import List
from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.asset import Asset
from stellar_model.model.horizon.claimable_balance import Claimant
from stellar_model.model.horizon.link import Link
from stellar_model.model.horizon.liquidity_pool_asset_amount import (
    LiquidityPoolAssetAmount,
)
from stellar_model.model.horizon.price import Price
from stellar_model.model.horizon.transaction import Transaction


__all__ = [
    "CreateAccountOperation",
    "PaymentOperation",
    "PathPaymentStrictReceiveOperation",
    "ManageSellOfferOperation",
    "CreatePassiveSellOfferOperation",
    "SetOptionsOperation",
    "ChangeTrustOperation",
    "AllowTrustOperation",
    "AccountMergeOperation",
    "InflationOperation",
    "ManageDataOperation",
    "BumpSequenceOperation",
    "ManageBuyOfferOperation",
    "PathPaymentStrictSendOperation",
    "CreateClaimableBalanceOperation",
    "ClaimClaimableBalanceOperation",
    "BeginSponsoringFutureReservesOperation",
    "EndSponsoringFutureReservesOperation",
    "RevokeSponsorshipOperation",
    "ClawbackOperation",
    "ClawbackClaimableBalanceOperation",
    "SetTrustLineFlagsOperation",
    "LiquidityPoolDepositOperation",
    "LiquidityPoolWithdrawOperation",
]


class Links(BaseModel):
    self: Link
    transaction: Link
    effects: Link
    succeeds: Link
    precedes: Link


class BaseOperation(BaseModel):
    """
    Represents the common attributes of an operations resource.
    """

    id: str = Field(description="The operation’s ID number.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    transaction_successful: bool = Field(
        description="Indicates if this operation was part of a successful transaction."
    )
    source_account: str = Field(
        description="The account that originates the operation."
    )
    source_account_muxed: Optional[str]
    source_account_muxed_id: Optional[int]
    type: str = Field(description="The name of the operation type.")
    type_i: int = Field(description="A number indicating the operation type.")
    created_at: datetime = Field(description="The datetime this operation was created.")
    transaction_hash: str = Field(
        description="A unique identifier for the transaction this operation belongs to."
    )
    transaction: Optional[Transaction]
    sponsor: Optional[str]
    links: Links = Field(alias="_links")


class BaseOfferOperation(BaseOperation):
    """
    Represents the common attributes of an offer operations resource.
    """

    amount: Decimal = Field(
        description="The amount of **selling_asset** that the account making this offer is willing to sell."
    )
    price: Decimal = Field(
        description="How many units of **selling_asset** it takes to get 1 unit of **buying_asset**. "
        "A number representing the decimal form of **price_r**."
    )
    price_r: Price = Field(
        description="A precise representation of the buy and sell price of the assets on offer."
    )
    buying_asset_type: str = Field(
        description="The type for the buying asset. Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    buying_asset_code: Optional[str] = Field(
        description="The Stellar address of the buying asset’s issuer. Appears if the **buying_asset_type** is not **native**."
    )
    buying_asset_issuer: Optional[str] = Field(
        description="The code for the buying asset.  Appears if the **buying_asset_type** is not **native**."
    )
    selling_asset_type: str = Field(
        description="The type for the selling asset. Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    selling_asset_code: Optional[str] = Field(
        description="The Stellar address of the selling asset’s issuer. Appears if the **selling_asset_type** is not **native**."
    )
    selling_asset_issuer: Optional[str] = Field(
        description="The code for the selling asset.  Appears if the **selling_asset_type** is not **native**."
    )


class CreateAccountOperation(BaseOperation):
    """
    Represents a single operations whose type is CreateAccount.

    type: create_account
    type_i: 0
    """

    starting_balance: Decimal = Field(
        description="The amount of XLM to send the newly created account."
    )
    funder: str = Field(description="The account that funds the new account.")
    funder_muxed: Optional[str]
    funder_muxed_id: Optional[int]
    account: str = Field(description="A new account that is funded.")


class PaymentOperation(BaseOperation):
    """
    Represents a single operations whose type is Payment.

    type: payment
    type_i: 1
    """

    asset_type: str = Field(
        description="The type of asset being sent. Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(
        description="The code for the asset being sent. Appears if the **asset_type** is not **native**."
    )
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of the issuer of the asset being sent. "
        "Appears if the **asset_type** is not **native**."
    )
    from_: str = Field(
        alias="from",
        description="The payment sender’s public key. This variable should be called `from`, "
        "but `from` is a keyword in Python, so we named it `from_`.",
    )
    from_muxed: Optional[str]
    from_muxed_id: Optional[int]
    to: str = Field(description="The payment recipient’s public key.")
    to_muxed: Optional[str]
    to_muxed_id: Optional[int]
    amount: Decimal = Field(description="Amount sent.")


class PathPaymentStrictReceiveOperation(BaseOperation):
    """
    Represents a single operations whose type is PathPaymentStrictReceive.

    type: path_payment_strict_receive
    type_i: 2
    """

    asset_type: str = Field(
        description="The type of asset being received. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(
        description="The code for the asset being received. Appears if the "
        "**asset_type** is not **native**."
    )
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of the issuer of the asset being "
        "received. Appears if the **asset_type** is not **native**."
    )
    from_: str = Field(
        alias="from",
        description="The payment sender’s public key. This variable "
        "should be called `from`, "
        "but `from` is a keyword in Python, so we named it `from_`.",
    )
    to: str = Field(description="The payment recipient’s public key.")
    amount: Decimal = Field(
        description="Amount received designated in the destination asset."
    )
    path: List[Asset] = Field(
        description="The intermediary assets that this path hops through."
    )
    source_amount: Decimal = Field(
        description="Amount sent designated in the source asset."
    )
    source_max: Decimal = Field(
        description="The maximum amount to be sent designated in the source asset."
    )
    source_asset_type: str = Field(
        description="The type for the source asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    source_asset_code: Optional[str] = Field(
        description="The code for the source asset. Appears if the "
        "**source_asset_type** is not **native**."
    )
    source_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the source asset’s issuer. "
        "Appears if the **source_asset_type** is not **native**."
    )


class ManageSellOfferOperation(BaseOfferOperation):
    """
    Represents a single operations whose type is CreatePassiveSellOffer.

    type: manage_sell_offer
    type_i: 3
    """

    offer_id: str = Field(description="A unique identifier for this offer.")


class CreatePassiveSellOfferOperation(BaseOfferOperation):
    """
    Represents a single operations whose type is CreatePassiveSellOffer.

    type: create_passive_sell_offer
    type_i: 4
    """


class SetOptionsOperation(BaseOperation):
    """
    Represents a single operations whose type is SetOptions.

    type: set_options
    type_i: 5
    """

    home_domain: Optional[str] = Field(
        description="The home domain used for stellar.toml file discovery."
    )
    inflation_dest: Optional[str] = Field(description="")

    master_key_weight: Optional[int] = Field(
        description="The weight of the master key. Can range from **1** to **255**."
    )
    signer_key: Optional[str] = Field(description="The public key of the new signer. ")
    signer_weight: Optional[int] = Field(
        description="The weight of the new signer. Can range from **1** to **255**."
    )

    set_flags: Optional[List[int]] = Field(
        description="The array of numeric values of flags that has been set in "
        "this operation. Options include **1** for **AUTH_REQUIRED_FLAG**, "
        "**2** for **AUTH_REVOCABLE_FLAG**, and **4** for **AUTH_IMMUTABLE_FLAG**."
    )
    set_flags_s: Optional[List[str]] = Field(
        description="The array of string values of flags that has been set in this operation. "
        "Options include **AUTH_REQUIRED_FLAG**, **AUTH_REVOCABLE_FLAG**, "
        "and **AUTH_IMMUTABLE_FLAG**."
    )
    clear_flags: Optional[List[int]] = Field(
        description="The array of numeric values of flags that has been cleared in this operation. "
        "Options include **1** for **AUTH_REQUIRED_FLAG**, **2** for "
        "**AUTH_REVOCABLE_FLAG**, and **4** for **AUTH_IMMUTABLE_FLAG**."
    )
    clear_flags_s: Optional[List[str]] = Field(
        description="The array of string values of flags that has been cleared in this "
        "operation. Options include **AUTH_REQUIRED_FLAG**, **AUTH_REVOCABLE_FLAG**, "
        "and **AUTH_IMMUTABLE_FLAG**."
    )

    low_threshold: Optional[int] = Field(
        description="The sum weight for the low threshold."
    )
    med_threshold: Optional[int] = Field(
        description="The sum weight for the medium threshold."
    )
    high_threshold: Optional[int] = Field(
        description="The sum weight for the high threshold."
    )


class ChangeTrustOperation(BaseOperation):
    """
    Represents a single operations whose type is ChangeTrust.

    type: change_trust
    type_i: 6
    """

    asset_type: str = Field(
        description="The type of asset being trusted. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(
        description="The code of the asset being trusted."
    )
    asset_issuer: Optional[str] = Field(
        description="The issuer for the asset being trusted."
    )
    liquidity_pool_id: Optional[str] = Field(
        description="The id of the liquidity pool being trusted."
    )
    limit: Decimal = Field(
        description="Limits the amount of an asset that the source account can hold."
    )
    trustee: Optional[str] = Field(description="The issuing account.")
    trustor: str = Field(description="The source account.")
    trustor_muxed: Optional[str]
    trustor_muxed_id: Optional[int]


class AllowTrustOperation(BaseOperation):
    """
    Represents a single operations whose type is AllowTrust.

    type: allow_trust
    type_i: 7
    """

    asset_type: str = Field(
        description="The type of asset. Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(
        description="The code for the asset. Appears if the **asset_type** is not **native**."
    )
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of the issuer of the asset. "
        "Appears if the **asset_type** is not **native**."
    )

    trustee: str = Field(
        description="The issuing account, or source account in this instance."
    )
    trustee_muxed: Optional[str]
    trustee_muxed_id: Optional[int]
    trustor: str = Field(
        description="The trusting account, or the account being authorized or unauthorized."
    )
    authorize: bool = Field(
        description="Flag indicating whether the trustline is authorized. "
        "0 if the account is not authorized to transact with the asset in any way. "
        "1 if the account is authorized to transact with the asset. "
        "2 if the account is authorized to maintain orders, "
        "but not to perform other transactions."
    )
    authorize_to_maintain_liabilities: bool


class AccountMergeOperation(BaseOperation):
    """
    Represents a single operations whose type is AccountMerge.

    type: account_merge
    type_i: 8
    """

    account: str = Field(description="The Stellar address being removed.")
    account_muxed: Optional[str]
    account_muxed_id: Optional[int]
    into: str = Field(
        description="The Stellar address receiving the deleted account’s lumens."
    )
    into_muxed: Optional[str]
    into_muxed_id: Optional[int]


class InflationOperation(BaseOperation):
    """
    Represents a single operations whose type is Inflation.

    type: inflation
    type_i: 9
    """


class ManageDataOperation(BaseOperation):
    """
    Represents a single operations whose type is ManageData.

    type: manage_data
    type_i: 10
    """

    name: str = Field(
        description="The key for this data entry. It can be up to 64 bytes long. If this is a "
        "new **Name**, it will add the given name/value pair to the account. "
        "If this **Name** is already present, then the associated value will be modified."
    )
    # TODO: make it optional
    value: str = Field(
        description="If present, then this value will be set in the DataEntry. It can be up to 64 "
        "bytes long. If not present, then the existing **Name** will be deleted."
    )


class BumpSequenceOperation(BaseOperation):
    """
    Represents a single operations whose type is BumpSequence.

    type: bump_sequence
    type_i: 11
    """

    bump_to: int = Field(
        description="The new desired value for the source account’s sequence number."
    )


class ManageBuyOfferOperation(BaseOfferOperation):
    """
    Represents a single operations whose type is ManageBuyOffer.

    type: manage_buy_offer
    type_i: 12
    """

    offer_id: str = Field(description="A unique identifier for this offer.")


class PathPaymentStrictSendOperation(BaseOperation):
    """
    Represents a single operations whose type is PathPaymentStrictSend.

    type: path_payment_strict_send
    type_i: 13
    """

    asset_type: str = Field(
        description="The type of asset being send. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(
        description="The code for the asset being send. Appears if the "
        "**asset_type** is not **native**."
    )
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of the issuer of the asset being "
        "send. Appears if the **asset_type** is not **native**."
    )
    from_: str = Field(
        alias="from",
        description="The payment sender’s public key. This variable should be called `from`, "
        "but `from` is a keyword in Python, so we named it `from_`.",
    )
    to: str = Field(description="The payment recipient’s public key.")
    amount: Decimal = Field(
        description="Amount received designated in the source asset."
    )
    path: List[Asset] = Field(
        description="The intermediary assets that this path hops through."
    )
    source_amount: Decimal = Field(
        description="Amount sent designated in the source asset."
    )
    destination_min: Decimal = Field(
        description="The minimum amount of destination asset expected to be received."
    )
    source_asset_type: str = Field(
        description="The type for the source asset. Either **native**, "
        "**credit_alphanum4**, or **credit_alphanum12**."
    )
    source_asset_code: Optional[str] = Field(
        description="The code for the source asset. Appears if the **asset_type** "
        "is not **native**."
    )
    source_asset_issuer: Optional[str] = Field(
        description="The Stellar address of the source asset’s issuer. "
        "Appears if the **asset_type** is not **native**."
    )


class CreateClaimableBalanceOperation(BaseOperation):
    """
    Represents a single operations whose type is CreateClaimableBalance.

    type: create_claimable_balance
    type_i: 14
    """

    asset: str = Field(
        description="The asset available to be claimed in the SEP-11 form **asset_code:issuing_address** or **native** (for XLM)"
    )
    amount: Decimal = Field(description="The amount available to be claimed.")
    claimants: List[Claimant] = Field(
        description="The list of entries which could claim the claimable balance."
    )


class ClaimClaimableBalanceOperation(BaseOperation):
    """
    Represents a single operations whose type is ClaimClaimableBalance.

    type: claim_claimable_balance
    type_i: 15
    """

    balance_id: str = Field(description="The id of the claimable balance.")
    claimant: str = Field(
        description="The id of the account which claimed the balance."
    )
    claimant_muxed: Optional[str]
    claimant_muxed_id: Optional[int]


class BeginSponsoringFutureReservesOperation(BaseOperation):
    """
    Represents a single operations whose type is BeginSponsoringFutureReserves.

    type: begin_sponsoring_future_reserves
    type_i: 16
    """

    sponsored_id: str = Field(
        description="The id of the account which will be sponsored."
    )


class EndSponsoringFutureReservesOperation(BaseOperation):
    """
    Represents a single operations whose type is EndSponsoringFutureReserves.

    type: end_sponsoring_future_reserves
    type_i: 17
    """

    begin_sponsor: Optional[str] = Field(
        description="The id of the account which initiated the sponsorship."
    )
    begin_sponsor_muxed: Optional[str]
    begin_sponsor_muxed_id: Optional[int]


class RevokeSponsorshipOperation(BaseOperation):
    """
    Represents a single operations whose type is RevokeSponsorship.

    type: revoke_sponsorship
    type_i: 18
    """

    account_id: Optional[str] = Field(
        description="The id of the account which is no longer sponsored."
    )
    claimable_balance_id: Optional[str] = Field(
        description="The id of the claimable balance which is no longer sponsored."
    )
    data_account_id: Optional[str] = Field(
        description="The id of the account whose data entry is no longer sponsored."
    )
    data_name: Optional[str] = Field(
        description="The name of the data entry which is no longer sponsored."
    )
    offer_id: Optional[str] = Field(
        description="The id of the offer which is no longer sponsored."
    )
    trustline_account_id: Optional[str] = Field(
        description="The id of the account whose trustline is no longer sponsored."
    )
    trustline_liquidity_pool_id: Optional[str] = Field(
        default="The liquidity pool of the trustline which is no longer sponsored."
    )
    trustline_asset: Optional[str] = Field(
        description="The asset of the trustline which is no longer sponsored."
    )
    signer_account_id: Optional[str] = Field(
        description="The account id of the signer which is no longer sponsored."
    )
    signer_key: Optional[str] = Field(
        description="The type of the signer which is no longer sponsored."
    )


class ClawbackOperation(BaseOperation):
    """
    Represents a single operations whose type is Clawback.

    type: clawback
    type_i: 19
    """

    asset_type: str
    asset_code: str
    asset_issuer: str
    from_: str = Field(
        alias="from",
        description="This variable should be called `from`, "
        "but `from` is a keyword in Python, so we named it `from_`.",
    )
    from_muxed: Optional[str]
    from_muxed_id: Optional[int]
    amount: Decimal


class ClawbackClaimableBalanceOperation(BaseOperation):
    """
    Represents a single operations whose type is ClawbackClaimableBalance.

    type: clawback_claimable_balance
    type_i: 20
    """

    balance_id: Optional[str]


class SetTrustLineFlagsOperation(BaseOperation):
    """
    Represents a single operations whose type is SetTrustLineFlags.

    type: set_trust_line_flags
    type_i: 21
    """

    asset_type: str
    asset_code: str
    asset_issuer: str
    trustor: str
    set_flags: Optional[List[int]]
    set_flags_s: Optional[List[str]]
    clear_flags: Optional[List[int]]
    clear_flags_s: Optional[List[str]]


class LiquidityPoolDepositOperation(BaseOperation):
    """
    Represents a single operations whose type is LiquidityPoolDeposit.

    type: liquidity_pool_deposit
    type_i: 22
    """

    liquidity_pool_id: str
    reserves_max: List[LiquidityPoolAssetAmount]
    min_price: Decimal
    min_price_r: Price
    max_price: Decimal
    max_price_r: Price
    reserves_deposited: List[LiquidityPoolAssetAmount]
    shares_received: Decimal


class LiquidityPoolWithdrawOperation(BaseOperation):
    """
    Represents a single operations whose type is LiquidityPoolWithdraw.

    type: liquidity_pool_withdraw
    type_i: 23
    """

    liquidity_pool_id: str
    reserves_min: List[LiquidityPoolAssetAmount]
    shares: Decimal
    reserves_received: List[LiquidityPoolAssetAmount]


_OPERATION_TYPE_UNION = Union[
    CreateAccountOperation,
    PaymentOperation,
    PathPaymentStrictReceiveOperation,
    ManageSellOfferOperation,
    CreatePassiveSellOfferOperation,
    SetOptionsOperation,
    ChangeTrustOperation,
    AllowTrustOperation,
    AccountMergeOperation,
    InflationOperation,
    ManageDataOperation,
    BumpSequenceOperation,
    ManageBuyOfferOperation,
    PathPaymentStrictSendOperation,
    CreateClaimableBalanceOperation,
    ClaimClaimableBalanceOperation,
    BeginSponsoringFutureReservesOperation,
    EndSponsoringFutureReservesOperation,
    RevokeSponsorshipOperation,
    ClawbackOperation,
    ClawbackClaimableBalanceOperation,
    SetTrustLineFlagsOperation,
    LiquidityPoolDepositOperation,
    LiquidityPoolWithdrawOperation,
]

_PAYMENT_TYPE_UNION = Union[
    CreateAccountOperation,
    PaymentOperation,
    AccountMergeOperation,
    PathPaymentStrictReceiveOperation,
    PathPaymentStrictSendOperation,
]

_OPERATION_TYPE_I_MAP = {
    0: CreateAccountOperation,
    1: PaymentOperation,
    2: PathPaymentStrictReceiveOperation,
    3: ManageSellOfferOperation,
    4: CreatePassiveSellOfferOperation,
    5: SetOptionsOperation,
    6: ChangeTrustOperation,
    7: AllowTrustOperation,
    8: AccountMergeOperation,
    9: InflationOperation,
    10: ManageDataOperation,
    11: BumpSequenceOperation,
    12: ManageBuyOfferOperation,
    13: PathPaymentStrictSendOperation,
    14: CreateClaimableBalanceOperation,
    15: ClaimClaimableBalanceOperation,
    16: BeginSponsoringFutureReservesOperation,
    17: EndSponsoringFutureReservesOperation,
    18: RevokeSponsorshipOperation,
    19: ClawbackOperation,
    20: ClawbackClaimableBalanceOperation,
    21: SetTrustLineFlagsOperation,
    22: LiquidityPoolDepositOperation,
    23: LiquidityPoolWithdrawOperation,
}
