class DuplicateProductError(Exception):
    pass

class Product:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        # Check for duplicate products by name or SKU
        if any(p.product_name == product.product_name or p.product_id == product.product_id for p in self.products):
            raise DuplicateProductError("A product with the same name or ID already exists")

        self.products.append(product)
        print("Product added successfully")