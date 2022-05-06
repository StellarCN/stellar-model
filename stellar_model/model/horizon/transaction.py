import base64

from datetime import datetime
from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


__all__ = ["Transaction"]


class Links(BaseModel):
    self: Link
    account: Link
    ledger: Link
    operations: Link
    effects: Link
    precedes: Link
    succeeds: Link
    transaction: Link


class FeeBumpTransaction(BaseModel):
    """
    Contains information about a fee bump transaction.
    """

    hash: str
    signatures: List[str]


class InnerTransaction(BaseModel):
    """
    Contains information about the inner transaction contained
    within a fee bump transaction.
    """

    hash: str
    signatures: List[str]
    max_fee: int


class TimeBounds(BaseModel):
    min_time: Optional[datetime] = Field(description="The lower bound.")
    max_time: Optional[datetime] = Field(description="The upper bound.")


class LedgerBounds(BaseModel):
    min_ledger: int = Field(description="The lower bound.")
    max_ledger: int = Field(description="The lower bound.")


class TransactionPreconditions(BaseModel):
    timebounds: Optional[TimeBounds] = Field(
        description="The time range for which this transaction is valid, "
        "with bounds as unsigned 64-bit UNIX timestamps."
    )
    ledgerbounds: Optional[LedgerBounds] = Field(
        description="The ledger range for which this transaction is valid, as unsigned 32-bit integers."
    )
    min_account_sequence: Optional[int] = Field(
        description="Containing a positive, signed 64-bit "
        "integer representing the lowest source account "
        "sequence number for which the transaction is valid."
    )
    min_account_sequence_age: Optional[int] = Field(
        description="The minimum duration of time (in seconds as an unsigned 64-bit "
        "integer) that must have passed since the source account's sequence "
        "number changed for the transaction to be valid."
    )
    min_account_sequence_ledger_gap: Optional[int] = Field(
        description="An unsigned 32-bit integer representing the minimum number of "
        "ledgers that must have closed since the source account's "
        "sequence number changed for the transaction to be valid."
    )
    extra_signers: Optional[List[str]] = Field(
        description="The list of up to two additional signers that must "
        "have corresponding signatures for this transaction to be valid."
    )


class Transaction(BaseModel):
    """
    Represents a single, successful transaction.
    """

    id: str = Field(description="A unique identifier for this transaction.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    successful: bool = Field(
        description="Indicates if this transaction was successful or not."
    )
    hash: str = Field(
        description="A hex-encoded SHA-256 hash of this transaction's XDR-encoded form."
    )
    ledger: int = Field(
        description="The sequence number of the ledger that this transaction was included in."
    )
    created_at: datetime = Field(
        description="The datetime this transaction was created."
    )
    source_account: str = Field(
        description="The account that originates the transaction."
    )
    account_muxed: Optional[str] = Field(
        description="account_muxed for source_account."
    )
    account_muxed_id: Optional[int] = Field(
        description="account_muxed_id for source_account."
    )
    source_account_sequence: int = Field(
        description="The source account's sequence number that "
        "this transaction consumed."
    )
    fee_account: str = Field(description="Account for paying transaction fees.")
    fee_account_muxed: Optional[str] = Field(
        description="account_muxed for fee_account."
    )
    fee_account_muxed_id: Optional[int] = Field(
        description="account_muxed_id for fee_account."
    )
    fee_charged: int = Field(
        description="The fee (in stroops) paid by the fee account to "
        "apply this transaction to the ledger."
    )
    max_fee: int = Field(
        description="The maximum fee (in stroops) that the source account was willing to pay."
    )
    operation_count: int = Field(
        description="The number of operations contained within this transaction."
    )
    envelope_xdr: str = Field(
        description="A base64 encoded string of the raw **TransactionEnvelope** "
        "XDR struct for this transaction."
    )
    result_xdr: str = Field(
        description="A base64 encoded string of the raw **TransactionResult** "
        "XDR struct for this transaction."
    )
    result_meta_xdr: str = Field(
        description="A base64 encoded string of the raw **TransactionMeta** "
        "XDR struct for this transaction"
    )
    fee_meta_xdr: str = Field(
        description="A base64 encoded string of the raw **LedgerEntryChanges** "
        "XDR struct produced by taking fees for this transaction."
    )
    memo_type: str = Field(
        description="The type of memo. Potential values include **MEMO_TEXT**, "
        "**MEMO_ID**, **MEMO_HASH**, **MEMO_RETURN**."
    )
    memo: Optional[str] = Field(
        description="The optional memo attached to a transaction."
    )
    memo_bytes: Optional[bytes]
    signatures: List[str] = Field(
        description="An array of signatures used to sign this transaction."
    )
    valid_after: Optional[datetime] = Field(
        description="The datetime after which a transaction is valid. This field is deprecated in lieu "
        "of `preconditions.time_bounds.min_time` and will be removed in Horizon v3."
    )
    valid_before: Optional[datetime] = Field(
        description="The datetime before which a transaction is valid. This field is deprecated in lieu "
        "of `preconditions.time_bounds.max_time` and will be removed in Horizon v3."
    )
    preconditions: Optional[TransactionPreconditions] = Field(
        description="A set of transaction preconditions affecting its validity."
    )
    fee_bump_transaction: Optional[FeeBumpTransaction]
    inner_transaction: Optional[InnerTransaction]
    links: Links = Field(alias="_links")

    def __init__(self, **data):
        if data.get("memo_bytes") is not None:
            data["memo_bytes"] = base64.b64decode(data["memo_bytes"])
        super().__init__(**data)
