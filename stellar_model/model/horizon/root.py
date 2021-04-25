from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.link import Link


__all__ = ["Root"]


class Links(BaseModel):
    account: Link
    accounts: Link
    account_transactions: Link
    claimable_balances: Link
    assets: Link
    effects: Link
    fee_stats: Link
    friendbot: Optional[Link]
    ledger: Link
    ledgers: Link
    offer: Link
    offers: Link
    operation: Link
    operations: Link
    order_book: Link
    payments: Link
    self: Link
    strict_receive_paths: Link
    strict_send_paths: Link
    trade_aggregations: Link
    trades: Link
    transaction: Link
    transactions: Link


class Root(BaseModel):
    """
    Represents the initial map of links into the api.
    """

    horizon_version: str
    core_version: str
    ingest_latest_ledger: int
    history_latest_ledger: int
    history_latest_ledger_closed_at: datetime
    history_elder_ledger: int
    core_latest_ledger: int
    network_passphrase: str
    current_protocol_version: int
    core_supported_protocol_version: int
    links: Links = Field(alias="_links")
