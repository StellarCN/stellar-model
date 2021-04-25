from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


__all__ = ["Ledger"]


class Links(BaseModel):
    self: Link
    transactions: Link
    operations: Link
    payments: Link
    effects: Link


class Ledger(BaseModel):
    """
    Represents a single closed ledger.
    """

    id: str = Field(description="A unique identifier for this ledger.")
    paging_token: str = Field(description="A cursor value for use in pagination.")
    hash: str = Field(
        description="A hex-encoded SHA-256 hash of this ledger's XDR-encoded form."
    )
    prev_hash: Optional[str] = Field(
        description="The hash of the ledger immediately preceding this ledger."
    )
    sequence: int = Field(
        description="The sequence number of this ledger, and the parameter used in Horizon "
        "calls that require a ledger number."
    )
    successful_transaction_count: int = Field(
        description="The number of successful transactions in this ledger."
    )
    failed_transaction_count: int = Field(
        description="The number of failed transactions in this ledger."
    )
    operation_count: int = Field(
        description="The number of operations applied in this ledger."
    )
    # TODO: add description
    operation_count: int
    # TODO: add description
    tx_set_operation_count: int
    closed_at: datetime = Field(
        description="The datetime of when this ledger was closed."
    )
    total_coins: Decimal = Field(
        description="The total number of lumens in circulation."
    )
    fee_pool: Decimal = Field(description="The sum of all transaction fees.")
    base_fee_in_stroops: int = Field(
        description="The fee the network charges per operations in a transaction."
    )
    base_reserve_in_stroops: int = Field(
        description="The reserve the network uses when "
        "calculating an account's minimum balance."
    )
    max_tx_set_size: int = Field(
        description="The maximum number of transactions "
        "validators have agreed to process in a given ledger."
    )
    protocol_version: int = Field(
        description="The model version that the Stellar network was running "
        "when this ledger was committed."
    )
    header_xdr: str = Field(
        description="A base64 encoded string of the raw LedgerHeader xdr struct for this ledger."
    )
    links: Links = Field(alias="_links")
