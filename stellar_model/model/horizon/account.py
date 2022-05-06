from datetime import datetime
from decimal import Decimal
from typing import List
from typing import Mapping
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


__all__ = ["Account"]


class Links(BaseModel):
    self: Link
    transactions: Link
    operations: Link
    payments: Link
    effects: Link
    offers: Link
    trades: Link
    data: Link


class AccountThresholds(BaseModel):
    """
    Represents an accounts **thresholds**, the numerical values
    needed to satisfy the authorization of a given operations.
    """

    low_threshold: int = Field(
        description="The weight required for a valid transaction including the Allow "
        "Trust and Bump Sequence operations."
    )
    med_threshold: int = Field(
        description="The weight required for a valid transaction "
        "including the Create Account, Payment, Path Payment, "
        "Manage Buy Offer, Manage Sell Offer, Create Passive Sell Offer, "
        "Change Trust, Inflation, and Manage Data operations."
    )
    high_threshold: int = Field(
        description="The weight required for a valid transaction including the "
        "Account Merge and Set Options operations."
    )


class AccountFlags(BaseModel):
    """
    Represents the state of an account's flags.
    """

    auth_required: bool = Field(
        description="If set to **true**, anyone who wants to hold an asset issued by this "
        "account must first be approved by this account."
    )
    auth_revocable: bool = Field(
        description="If set to **true**, this account can freeze the balance of a holder of "
        "an asset issued by this account."
    )
    auth_immutable: bool = Field(
        description="If set to **true**, none of the following flags can be changed."
    )
    auth_clawback_enabled: bool = Field(description="")


class Balance(BaseModel):
    """
    Represents an account's holdings for a single currency type.
    """

    balance: Decimal = Field(
        description="The number of units of an asset held by this account."
    )
    liquidity_pool_id: Optional[str] = Field(
        description="This liquidity pool’s id encoded in a "
        "hex string representation."
    )
    limit: Optional[Decimal] = Field(
        description="The maximum amount of this asset that this account "
        "is willing to accept. Specified when opening a trustline."
    )
    buying_liabilities: Optional[Decimal] = Field(
        description="The sum of all buy offers owned by this account " "for this asset."
    )
    selling_liabilities: Optional[Decimal] = Field(
        description="The sum of all sell offers owned by this account "
        "for this asset."
    )
    sponsor: Optional[str] = Field(
        description="The account ID of the sponsor who is paying "
        "the reserves for this trustline."
    )
    last_modified_ledger: Optional[int]
    is_authorized: Optional[bool]
    is_authorized_to_maintain_liabilities: Optional[bool]
    is_clawback_enabled: Optional[bool]
    asset_type: str = Field(
        description="Either **native**, **credit_alphanum4**, or **credit_alphanum12**."
    )
    asset_code: Optional[str] = Field(description="The code for this asset.")
    asset_issuer: Optional[str] = Field(
        description="The Stellar address of this asset's issuer."
    )


class Signer(BaseModel):
    """
    Represents one of an account's signers.
    """

    weight: int
    key: str
    type: str


class Account(BaseModel):
    """
    Represents the summary of an account.
    """

    id: str = Field(description="A unique identifier for this account.")
    account_id: str = Field(
        description="This account's public key encoded in a base32 string representation."
    )
    sequence: int = Field(
        description="This account's current sequence number. "
        "For use when submitting this account's next transaction."
    )
    sequence_ledger: Optional[int] = Field(
        description="The unsigned 32-bit ledger " "number of the sequence number's age."
    )
    sequence_time: Optional[datetime] = Field(
        description="The time of the sequence number's age."
    )
    subentry_count: int = Field(description="The number of subentries on this account.")
    inflation_destination: Optional[str] = Field(
        description="The inflation destination set for this account."
    )
    home_domain: Optional[str] = Field(
        description="The domain that hosts this account's stellar.toml file."
    )
    last_modified_ledger: int = Field(
        description="The ID of the last ledger that included changes to this account."
    )
    last_modified_time: Optional[datetime] = Field(
        description="The time of the last ledger that included "
        "changes to this account."
    )
    thresholds: AccountThresholds = Field(
        description="Operations have varying levels of access. "
        "This field specifies thresholds for different access levels, "
        "as well as the weight of the master key."
    )
    flags: AccountFlags = Field(
        description="Flags denote the enabling/disabling of certain asset issuer privileges."
    )
    balances: List[Balance] = Field(description="The assets this account holds.")
    signers: List[Signer] = Field(
        description="The public keys and associated weights that can be used to "
        "authorize transactions for this account. Used for multi-sig."
    )
    data: Mapping[str, str] = Field(description="An array of account data fields.")
    num_sponsoring: int = Field(
        description="The number of reserves sponsored by this account."
    )
    num_sponsored: int = Field(
        description="The number of reserves sponsored for this account."
    )
    sponsor: Optional[str] = Field(
        description="The account ID of the sponsor who is paying the "
        "reserves for this account."
    )
    paging_token: str = Field(description="A cursor value for use in pagination.")
    links: Links = Field(alias="_links")
