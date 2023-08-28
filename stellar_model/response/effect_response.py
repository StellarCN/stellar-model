from pydantic import BaseModel

from stellar_model import __issues__
from stellar_model.model.horizon.effects import _EFFECT_TYPE_I_MAP, _EFFECT_TYPE_UNION

__all__ = ["EffectResponse"]


class EffectResponse(BaseModel):
    """
    Represents single effect response.
    Can be used for parsing individual records returned from the following endpoint:

        - GET /effects

    See `Effects <https://developers.stellar.org/api/resources/effects/>`_ on Stellar API Reference.

    The primary intended use-case for this model is to allow parsing individual Effects using the relevant type
    parser in situations where EffectsResponse cannot be used over the entire list, like if one or
    more items in the list throws a ValidationError.
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
        record = parser.model_validate(data)
        super().__init__(record=record)
