class IncompleteOrderException(Exception):
    pass

class Order:
    def __init__(self, order_id, order_details):
        self.order_id = order_id
        self.order_details = order_details

    def process_order(self):
        for order_detail in self.order_details:
            if order_detail.product_id is None:
                raise IncompleteOrderException("Incomplete order: Product reference missing in order detail")
        print("Order processing successful")
