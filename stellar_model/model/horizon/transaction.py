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
        description="The datetime after which a transaction is valid."
    )
    valid_before: Optional[datetime] = Field(
        description="The datetime before which a transaction is valid."
    )
    # TODO: add description
    fee_bump_transaction: Optional[FeeBumpTransaction]
    inner_transaction: Optional[InnerTransaction]
    links: Links = Field(alias="_links")

    def __init__(self, **data):
        if data.get("memo_bytes") is not None:
            data["memo_bytes"] = base64.b64decode(data["memo_bytes"])
        super().__init__(**data)
