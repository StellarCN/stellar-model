from pydantic import BaseModel, Field


class Price(BaseModel):
    """
    Represents a price
    """

    n: int = Field(description="The numerator.")
    d: int = Field(description="The denominator.")
