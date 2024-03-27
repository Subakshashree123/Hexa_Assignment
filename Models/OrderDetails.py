class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.order_detail_id = order_detail_id
        self.order = order
        self.product = product
        self.quantity = quantity
    
    def calculate_subtotal(self):
        return self.product.price * self.quantity
    
    def get_order_detail_info(self):
        order_detail_info = {
            'OrderDetailID': self.order_detail_id,
            'OrderID': self.order.order_id,
            'ProductID': self.product.product_id,
            'ProductName': self.product.product_name,
            'Price': self.product.price,
            'Quantity': self.quantity
        }
        return order_detail_info
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def add_discount(self, discount_amount):
        self.discount = discount_amount
    