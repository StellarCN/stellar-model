from typing import Any
from typing import Mapping
from typing import Optional

from pydantic import BaseModel


__all__ = ["ErrorResponse"]


class ErrorResponse(BaseModel):
    """
    Represents error response.

    See `Error Response <https://developers.stellar.org/api/errors/response/>`_ on Stellar API Reference.
    """

    type: str
    title: str
    status: int
    detail: Optional[str]
    extras: Optional[Mapping[str, Any]]
