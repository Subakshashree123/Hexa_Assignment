class Product:
    def __init__(self, product_id, product_name, description, price, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class OrderDetails:
    def __init__(self):
        self.order_details = []

    def add_order_detail(self, product, quantity):
        # Check product availability in inventory
        if product.quantity_in_stock < quantity:
            raise ValueError(f"Insufficient stock for product '{product.product_name}'")

        # Add order detail
        self.order_details.append({'product': product, 'quantity': quantity})
        print("Order detail added successfully")
