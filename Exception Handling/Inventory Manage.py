class InsufficientStockException(Exception):
    pass

class Product:
    def __init__(self, product_id, product_name, description, price, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def sell(self, quantity):
        if quantity > self.quantity_in_stock:
            raise InsufficientStockException(f"Insufficient stock for {self.product_name}. Available stock: {self.quantity_in_stock}")
        else:
            self.quantity_in_stock -= quantity

class Order:
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

    def process_order(self):
        try:
            self.product.sell(self.quantity)
            print("Order processed successfully.")
        except InsufficientStockException as e:
            print(f"Order processing failed: {str(e)}")
           

