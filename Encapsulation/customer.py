    # Getter and setter for CustomerID
@property
def customer_id(self):
        return self.__customer_id
    
@customer_id.setter
def customer_id(self, value):
        if isinstance(value, int) and value > 0:
            self.__customer_id = value
        else:
            raise ValueError("CustomerID must be a positive integer")

    # Getter and setter for FirstName
@property
def first_name(self):
        return self.__first_name
    
@first_name.setter
def first_name(self, value):
        if isinstance(value, str):
            self.__first_name = value
        else:
            raise ValueError("FirstName must be a string")

    # Getter and setter for LastName
@property
def last_name(self):
        return self.__last_name
    
@last_name.setter
def last_name(self, value):
        if isinstance(value, str):
            self.__last_name = value
        else:
            raise ValueError("LastName must be a string")

    # Getter and setter for Email
@property
def email(self):
        return self.__email
    
@email.setter
def email(self, value):
        # Perform email validation here if required
        self.__email = value

    # Getter and setter for Phone
@property
def phone(self):
        return self.__phone
    
@phone.setter
def phone(self, value):
        # Perform phone number validation here if required
        self.__phone = value

    # Getter and setter for Address
@property
def address(self):
        return self.__address
    
@address.setter
def address(self, value):
        if isinstance(value, str):
            self.__address = value
        else:
            raise ValueError("Address must be a string")
