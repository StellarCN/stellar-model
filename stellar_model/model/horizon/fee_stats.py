from decimal import Decimal

from pydantic import BaseModel
from pydantic import Field


__all__ = ["FeeStats"]


class FeeDistribution(BaseModel):
    """
    https://developers.stellar.org/api/aggregations/fee-stats/
    """

    # TODO: add description
    max: int
    min: int
    mode: int
    p10: int
    p20: int
    p30: int
    p40: int
    p50: int
    p60: int
    p70: int
    p80: int
    p90: int
    p95: int
    p99: int


class FeeStats(BaseModel):
    """
    Represents a horizon of fees from horizon.
    """

    last_ledger: int = Field(description="The last ledger's sequence number.")
    last_ledger_base_fee: int = Field(
        description="The base fee as defined in the last ledger."
    )
    ledger_capacity_usage: Decimal = Field(
        description="The average capacity usage over "
        "the last 5 ledgers (0 is no usage, "
        "1.0 is completely full ledgers)."
    )
    fee_charged: FeeDistribution = Field(
        description="Information about the fee charged for "
        "transactions in the last 5 ledgers."
    )
    max_fee: FeeDistribution = Field(
        description="Information about max fee bid for "
        "transactions over the last 5 ledgers."
    )
