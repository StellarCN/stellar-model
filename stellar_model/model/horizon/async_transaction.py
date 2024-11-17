from typing import Literal, Optional

from pydantic import BaseModel, Field


class AsyncTransaction(BaseModel):
    """
    Represents an asynchronous transaction response.
    """

    error_result_xdr: Optional[str] = Field(default=None)
    tx_status: Literal["ERROR", "PENDING", "DUPLICATE", "TRY_AGAIN_LATER"]
    hash: str
