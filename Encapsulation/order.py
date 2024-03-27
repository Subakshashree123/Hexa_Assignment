class Orders:
    def __init__(self, order_id, customer, order_date, total_amount):
        self.__order_id = order_id
        self.__customer = customer
        self.__order_date = order_date
        self.__total_amount = total_amount

    # Getter and setter for OrderID
    @property
    def order_id(self):
        return self.__order_id
    
    @order_id.setter
    def order_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__order_id = value
        else:
            raise ValueError("OrderID must be a positive integer")

    @property
    def customer(self):
        return self.__customer
    
    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def order_date(self):
        return self.__order_date
    
    @order_date.setter
    def order_date(self, value):
        self.__order_date = value

    @property
    def total_amount(self):
        return self.__total_amount
    
    @total_amount.setter
    def total_amount(self, value):
        if isinstance(value, float) or isinstance(value, int):
            if value >= 0:
                self.__total_amount = value
            else:
                raise ValueError("TotalAmount cannot be negative")
        else:
            raise ValueError("TotalAmount must be a numeric value")