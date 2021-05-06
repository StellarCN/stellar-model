from typing import List

from pydantic import BaseModel
from pydantic import Field

from stellar_model import __issues__
from stellar_model.model.horizon.effects import _EFFECT_TYPE_I_MAP
from stellar_model.model.horizon.effects import _EFFECT_TYPE_UNION
from stellar_model.response.page_model import PageModel


__all__ = ["EffectsResponse"]


class Embedded(BaseModel):
    records: List[_EFFECT_TYPE_UNION]

    def __init__(self, records):
        model_records: List[_EFFECT_TYPE_UNION] = []
        for record in records:
            if "type_i" not in record:
                raise ValueError(
                    "Invalid data, `type_i` does not appear in the raw data. "
                    "Please check the raw data first, if the data is correct, "
                    "try to upgrade the library or raise an issue at {__issues__}."
                )
            effect_type = record["type_i"]
            if effect_type not in _EFFECT_TYPE_I_MAP:
                raise ValueError(
                    f"The type of effect is {effect_type}, which is not currently supported in the version. "
                    f"Please try to upgrade the library or raise an issue at {__issues__}."
                )
            parser = _EFFECT_TYPE_I_MAP[effect_type]
            model = parser.parse_obj(record)
            model_records.append(model)
        super().__init__(records=model_records)


class EffectsResponse(PageModel):
    """
    Represents effects response.

    Can be used for the following endpoint(s):

        - GET /effects

    See `Effects <https://developers.stellar.org/api/resources/effects/>`_ on Stellar API Reference.
    """

    embedded: Embedded = Field(alias="_embedded")
