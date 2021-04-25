from pydantic import BaseModel
from pydantic import Field


class Price(BaseModel):
    """
    Represents a price
    """

    n: int = Field(description="The numerator.")
    d: int = Field(description="The denominator.")
