class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order
        self.__product = product
        self.__quantity = quantity

    # Getter and setter for OrderDetailID
    @property
    def order_detail_id(self):
        return self.__order_detail_id
    
    @order_detail_id.setter
    def order_detail_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__order_detail_id = value
        else:
            raise ValueError("OrderDetailID must be a positive integer")

    @property
    def order(self):
        return self.__order
    
    @order.setter
    def order(self, value):
        self.__order = value

    @property
    def product(self):
        return self.__product
    
    @product.setter
    def product(self, value):
        self.__product = value
    @property
    def quantity(self):
        return self.__quantity
    
    @quantity.setter
    def quantity(self, value):
        if isinstance(value, int) and value > 0:
            self.__quantity = value
        else:
            raise ValueError("Quantity must be a positive integer")

