class Orders:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount
    
    def calculate_total_amount(self):
        return self.total_amount
    
    def get_order_details(self):
        order_details = {
            'OrderID': self.order_id,
            'OrderDate': self.order_date,
            'TotalAmount': self.total_amount,
            'ProductList': self.product_list
        }
        return order_details
    
    def update_order_status(self, new_status):
        self.status = new_status
    
    def cancel_order(self):
        for product in self.product_list:
            product.adjust_stock_levels(product.quantity)
        self.status = "cancelled"
        print("Order cancelled successfully.")