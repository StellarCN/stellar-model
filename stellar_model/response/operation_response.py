from pydantic import BaseModel

from stellar_model import __issues__
from stellar_model.model.horizon.operations import _OPERATION_TYPE_I_MAP
from stellar_model.model.horizon.operations import _OPERATION_TYPE_UNION


__all__ = ["OperationResponse"]


class OperationResponse(BaseModel):
    """
    Represents single operation response.

    Can be used for the following endpoint(s):

        - GET /operations/:operation_id


    See `Operations <https://developers.stellar.org/api/resources/operations/>`_ on Stellar API Reference.
    """

    record: _OPERATION_TYPE_UNION

    def __init__(self, **data):
        if "type_i" not in data:
            raise ValueError(
                "Invalid data, `type_i` does not appear in the raw data. "
                "Please check the raw data first, if the data is correct, "
                "try to upgrade the library or raise an issue at {__issues__}."
            )
        op_type = data["type_i"]
        if op_type not in _OPERATION_TYPE_I_MAP:
            raise ValueError(
                f"The type of operation is {op_type}, which is not currently supported in the version. "
                f"Please try to upgrade the library or raise an issue at {__issues__}."
            )
        parser = _OPERATION_TYPE_I_MAP[op_type]
        record = parser.parse_obj(data)
        super().__init__(record=record)
