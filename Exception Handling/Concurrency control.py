class ConcurrencyException(Exception):
    pass

class Order:
    def __init__(self, order_id, version):
        self.order_id = order_id
        self.version = version

    def update_order(self, new_version):
        if self.version != new_version:
            raise ConcurrencyException("Order has been updated by another user. Please refresh and try again.")
        else:
            self.version = new_version
            print("Order updated successfully")