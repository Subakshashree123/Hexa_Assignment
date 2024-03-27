class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.inventory_id = inventory_id
        self.product = product
        self.quantity_in_stock = quantity_in_stock
        self.last_stock_update = last_stock_update

    def get_product(self):
        return self.product
    
    def get_quantity_in_stock(self):
        return self.quantity_in_stock
    
    def add_to_inventory(self, quantity):
        self.quantity_in_stock += quantity
    
    def remove_from_inventory(self, quantity):
        if self.quantity_in_stock >= quantity:
            self.quantity_in_stock -= quantity
        else:
            print("Error: Insufficient quantity in stock.")
    
    def update_stock_quantity(self, new_quantity):
        self.quantity_in_stock = new_quantity
    
    def is_product_available(self, quantity_to_check):
        return self.quantity_in_stock >= quantity_to_check

    def get_inventory_value(self):
        return self.product.price * self.quantity_in_stock
    
    def list_low_stock_products(self, threshold):
        if self.quantity_in_stock < threshold:
            return f"{self.product.product_name} (ID: {self.product.product_id}) - Quantity: {self.quantity_in_stock}"
        
    def list_out_of_stock_products(self):
        if self.quantity_in_stock == 0:
            return f"{self.product.product_name} (ID: {self.product.product_id})"
        
    def list_all_products(self):
        return f"{self.product.product_name} (ID: {self.product.product_id}) - Quantity: {self.quantity_in_stock}"