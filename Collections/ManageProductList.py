class Product:
    def __init__(self, product_id, name, description, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product in self.products:
            raise ValueError("Product already exists in the list")
        self.products.append(product)
        print("Product added successfully")

    def update_product(self, product_id, new_product):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                self.products[i] = new_product
                print("Product updated successfully")
                return
        raise ValueError("Product with given ID not found")

    def remove_product(self, product_id):
        for i, product in enumerate(self.products):
            if product.product_id == product_id:
                if self.has_existing_orders(product_id):
                    raise ValueError("Product has existing orders and cannot be removed")
                del self.products[i]
                print("Product removed successfully")
                return
        raise ValueError("Product with given ID not found")

    def has_existing_orders(self, product_id):
        return False  


