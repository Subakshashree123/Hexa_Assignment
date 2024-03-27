class Products:
    def __init__(self, product_id, product_name, description, price):
        self.product_id = product_id
        self.product_name = product_name
        self.description = description
        self.price = price

class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.__product = product  # Composition relationship with Products class
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, new_product):
        # Ensure that the new product is an instance of the Products class
        if isinstance(new_product, Products):
            self.__product = new_product
            
        else:
            print("Invalid product.")