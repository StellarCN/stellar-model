from decimal import Decimal

from pydantic import BaseModel
from pydantic import Field

from stellar_model.model.horizon.price import Price


__all__ = ["TradeAggregation"]


class TradeAggregation(BaseModel):
    """
    Represents trade data aggregation over a period of time.
    """

    timestamp: int = Field(
        description="Start time for this trade aggregation. "
        "Represented as milliseconds since epoch."
    )
    trade_count: int = Field(description="Total number of trades aggregated.")
    base_volume: Decimal = Field(description="Total volume of base asset.")
    counter_volume: Decimal = Field(description="Total volume of counter asset.")
    avg: Decimal = Field(
        description="Weighted average price of counter asset in terms of base asset."
    )
    high: Decimal = Field(description="The highest price for this time period.")
    high_r: Price = Field(
        description="The highest price for this time period as a rational number."
    )
    low: Decimal = Field(description="The lowest price for this time period.")
    low_r: Price = Field(
        description="The lowest price for this time period as a rational number."
    )
    open: Decimal = Field(description="The price as seen on first trade aggregated.")
    open_r: Price = Field(
        description="The price as seen on first trade aggregated as a rational number."
    )
    close: Decimal = Field(description="The price as seen on last trade aggregated.")
    close_r: Price = Field(
        description="The price as seen on last trade aggregated as a rational number."
    )
