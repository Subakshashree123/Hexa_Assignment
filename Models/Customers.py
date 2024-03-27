class Customers:
    def __init__(self, customer_id, first_name, last_name, email, phone, address, orders):
        self.customer_id = customer_id,
        self.first_name = first_name,
        self.last_name = last_name,
        self.email = email,
        self.phone = phone,
        self.address = address,
        self.total_orders=orders
    
    def calculate_total_orders(self):
        print("Total_orders")
        return len(self.total_orders)
    
    def get_customer_details(self):
        return {
            'customer_id': self.customer_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }
    def update_customer_info(self, email=None, phone=None, address=None):
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if address:
            self.address = address