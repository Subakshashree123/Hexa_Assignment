class Products:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

    def get_product_details(self):
        return {
            'ProductID': self.product_id,
            'ProductName': self.product_name,
            'Description': self.description,
            'Price': self.price
        }
    def update_product_info(self, description=None, price=None):
        if description:
            self.description = description
        if price:
            self.price = price
    
    def is_product_in_stock(self):
        return self.in_stock