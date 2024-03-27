class ProductManager:
    def __init__(self):
        self.products = []

    def search_products_by_name(self, name):
        found_products = [product for product in self.products if product.name.lower() == name.lower()]
        if not found_products:
            raise ValueError("No products found with the given name")
        return found_products

    def search_products_by_category(self, category):
        found_products = [product for product in self.products if product.category.lower() == category.lower()]
        if not found_products:
            raise ValueError("No products found in the given category")
        return found_products