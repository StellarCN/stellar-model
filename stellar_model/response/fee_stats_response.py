from stellar_model.model.horizon.fee_stats import FeeStats


__all__ = ["FeeStatsResponse"]


class FeeStatsResponse(FeeStats):
    """
    Represents fee stats response.

    Can be used for the following endpoint(s):

        - GET /fee_stats

    See `Fee Stats <https://developers.stellar.org/api/aggregations/fee-stats/>`_ on Stellar API Reference.
    """
