from stellar_model.model.horizon.order_book_summary import OrderBookSummary


__all__ = ["OrderBookResponse"]


class OrderBookResponse(OrderBookSummary):
    """
    An order book is a collections of offers for a specific pair of assets.

    Can be used for the following endpoint(s):

        - GET /order_book


    See `Order Books <https://developers.stellar.org/api/aggregations/order-books/>`_ on Stellar API Reference.
    """
