class OrderManager:
    def __init__(self, inventory_manager):
        self.inventory_manager = inventory_manager

    def process_order(self, order):
        try:
            for product_id, quantity in order.products.items():
                self.inventory_manager.update_quantity(product_id, self.inventory_manager.inventory[product_id] - quantity)
            print("Order processed successfully")
        except ValueError as e:
            print(f"Failed to process order: {str(e)}")