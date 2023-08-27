from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model import __issues__
from stellar_model.model.horizon.operations import _OPERATION_TYPE_I_MAP
from stellar_model.model.horizon.operations import _PAYMENT_TYPE_UNION
from stellar_model.response.page_model import PageModel


__all__ = ["PaymentsResponse"]


class Embedded(BaseModel):
    records: List[_PAYMENT_TYPE_UNION]

    def __init__(self, records):
        model_records: List[_PAYMENT_TYPE_UNION] = []
        for record in records:
            if "type_i" not in record:
                raise ValueError(
                    "Invalid data, `type_i` does not appear in the raw data. "
                    "Please check the raw data first, if the data is correct, "
                    "try to upgrade the library or raise an issue at {__issues__}."
                )
            op_type = record["type_i"]
            if op_type not in _OPERATION_TYPE_I_MAP:
                raise ValueError(
                    f"The type of operation is {op_type}, which is not currently supported in the version. "
                    f"Please try to upgrade the library or raise an issue at {__issues__}."
                )
            parser = _OPERATION_TYPE_I_MAP[op_type]
            model = parser.model_validate(record)
            model_records.append(model)

        super().__init__(records=model_records)


class PaymentsResponse(PageModel):
    """
    Represents payments response.

    Can be used for the following endpoint(s):

        - /payments{?cursor,limit,order,include_failed}

    """

    embedded: Embedded = Field(alias="_embedded")
