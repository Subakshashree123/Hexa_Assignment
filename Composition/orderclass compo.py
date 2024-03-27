
@property
def order_id(self):
        return self.__order_id

@property
def customer(self):
        return self.__customer

@property
def total_amount(self):
        return self.__total_amount

@total_amount.setter
def total_amount(self, new_total_amount):
        if new_total_amount >= 0:
            self.__total_amount = new_total_amount
        else:
            print("Total amount cannot be negative.")
