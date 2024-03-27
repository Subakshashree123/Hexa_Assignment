class Inventory:
    def __init__(self, inventory_id, product, quantity_in_stock, last_stock_update):
        self.__inventory_id = inventory_id
        self.__product = product
        self.__quantity_in_stock = quantity_in_stock
        self.__last_stock_update = last_stock_update

    # Getter and setter for InventoryID
    @property
    def inventory_id(self):
        return self.__inventory_id
    
    @inventory_id.setter
    def inventory_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__inventory_id = value
        else:
            raise ValueError("InventoryID must be a positive integer")

    # Getter and setter for Product
    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self, value):
        # Add any necessary validation logic here
        self.__product = value

    # Getter and setter for QuantityInStock
    @property
    def quantity_in_stock(self):
        return self.__quantity_in_stock
    
    @quantity_in_stock.setter
    def quantity_in_stock(self, value):
        if isinstance(value, int) and value >= 0:
            self.__quantity_in_stock = value
        else:
            raise ValueError("QuantityInStock must be a non-negative integer")

    # Getter and setter for LastStockUpdate
    @property
    def last_stock_update(self):
        return self.__last_stock_update
    
    @last_stock_update.setter
    def last_stock_update(self, value):
        # Add any necessary validation logic here
        self.__last_stock_update = value
