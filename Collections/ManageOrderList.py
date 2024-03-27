class Order:
    def __init__(self, order_id, customer_id, status, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.status = status
        self.products = products

    def update_status(self, new_status):
        self.status = new_status
        print(f"Order {self.order_id} status updated to {new_status}")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Product {product} removed from order {self.order_id}")
        else:
            print(f"Product {product} not found in order {self.order_id}")

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)
        print(f"Order {order.order_id} added successfully")

    def remove_canceled_orders(self):
        self.orders = [order for order in self.orders if order.status != "Canceled"]
        print("Canceled orders removed successfully")

    def update_order_status(self, order_id, new_status):
        for order in self.orders:
            if order.order_id == order_id:
                order.update_status(new_status)
                break
        else:
            print(f"Order {order_id} not found")

    def synchronize_with_inventory(self, order):
        print(f"Synchronized order {order.order_id} with inventory")

    def synchronize_with_payment(self, order):
        print(f"Synchronized order {order.order_id} with payment records")
