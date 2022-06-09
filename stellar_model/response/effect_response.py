from pydantic import BaseModel

from stellar_model import __issues__
from stellar_model.model.horizon.effects import _EFFECT_TYPE_I_MAP
from stellar_model.model.horizon.effects import _EFFECT_TYPE_UNION


__all__ = ["EffectResponse"]


class EffectResponse(BaseModel):
    """
    Represents single effect response.
    Can be used for the following endpoint(s):
        - GET /effects/:effect_id
    See `Effects <https://developers.stellar.org/api/resources/effects/>`_ on Stellar API Reference.
    """

    record: _EFFECT_TYPE_UNION

    def __init__(self, **data):
        if "type_i" not in data:
            raise ValueError(
                "Invalid data, `type_i` does not appear in the raw data. "
                "Please check the raw data first, if the data is correct, "
                "try to upgrade the library or raise an issue at {__issues__}."
            )
        effect_type = data["type_i"]
        if effect_type not in _EFFECT_TYPE_I_MAP:
            raise ValueError(
                f"The type of effect is {effect_type}, which is not currently supported in the version. "
                f"Please try to upgrade the library or raise an issue at {__issues__}."
            )
        parser = _EFFECT_TYPE_I_MAP[effect_type]
        record = parser.parse_obj(data)
        super().__init__(record=record)
