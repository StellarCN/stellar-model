from typing import Optional

from pydantic import BaseModel
from pydantic import Field


__all__ = ["AccountData"]


class AccountData(BaseModel):
    """
    Represents a single data object stored on by an account.
    """

    value: str = Field(description="The key value for this data.")
    # TODO: add description
    sponsor: Optional[str]
