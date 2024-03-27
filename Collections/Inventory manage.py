class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product_id, quantity):
        if product_id in self.inventory:
            raise ValueError("Product already exists in inventory")
        self.inventory[product_id] = quantity
        print(f"Product {product_id} added to inventory with quantity {quantity}")

    def remove_product(self, product_id):
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory")
        del self.inventory[product_id]
        print(f"Product {product_id} removed from inventory")

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self.inventory:
            raise ValueError("Product not found in inventory")
        self.inventory[product_id] = new_quantity
        print(f"Quantity updated for product {product_id}: {new_quantity}")

    def get_inventory_info(self):
        print("Inventory Information:")
        for product_id, quantity in self.inventory.items():
            print(f"Product ID: {product_id}, Quantity: {quantity}")
