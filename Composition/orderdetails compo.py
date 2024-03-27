class Orders:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.order_id = order_id
        self.customer = customer
        self.order_date = order_date
        self.total_amount = total_amount

class Products:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

class OrderDetails:
    def __init__(self, order_detail_id, order, product, quantity):
        self.__order_detail_id = order_detail_id
        self.__order = order  
        self.__product = product  
        self.__quantity = quantity

    @property
    def order_detail_id(self):
        return self.__order_detail_id

    @property
    def order(self):
        return self.__order

    @property
    def product(self):
        return self.__product

    @property
    def quantity(self):
        return self.__quantity