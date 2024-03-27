class Products:
    def __init__(self, product_id, product_name, description, price):
        self.__product_id = product_id
        self.__product_name = product_name
        self.__description = description
        self.__price = price


    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__product_id = value
        else:
            raise ValueError("ProductID must be a positive integer")

    @property
    def product_name(self):
        return self.__product_name
    
    @product_name.setter
    def product_name(self, value):
        if isinstance(value, str):
            self.__product_name = value
        else:
            raise ValueError("ProductName must be a string")

    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value
        else:
            raise ValueError("Description must be a string")
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) or isinstance(value, int):
            if value >= 0:
                self.__price = value
            else:
                raise ValueError("Price cannot be negative")
        else:
            raise ValueError("Price must be a numeric value")



    # Getter and setter for ProductID
    @property
    def product_id(self):
        return self.__product_id
    
    @product_id.setter
    def product_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__product_id = value
        else:
            raise ValueError("ProductID must be a positive integer")

    # Getter and setter for ProductName
    @property
    def product_name(self):
        return self.__product_name
    
    @product_name.setter
    def product_name(self, value):
        if isinstance(value, str):
            self.__product_name = value
        else:
            raise ValueError("ProductName must be a string")

    # Getter and setter for Description
    @property
    def description(self):
        return self.__description
    
    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value
        else:
            raise ValueError("Description must be a string")

    # Getter and setter for Price
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if isinstance(value, float) or isinstance(value, int):
            if value >= 0:
                self.__price = value
            else:
                raise ValueError("Price cannot be negative")
        else:
            raise ValueError("Price must be a numeric value")

