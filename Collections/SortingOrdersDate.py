#from datetime import datetime

class Order:
    def __init__(self, order_id, customer_id, order_date, status, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.status = status
        self.products = products

    def __str__(self):
        return f"Order {self.order_id} - Date: {self.order_date}, Status: {self.status}"

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def sort_orders_by_date(self, ascending=True):
        self.orders.sort(key=lambda x: x.order_date, reverse=not ascending)

    def get_orders_in_date_range(self, start_date, end_date):
        return [order for order in self.orders if start_date <= order.order_date <= end_date]
