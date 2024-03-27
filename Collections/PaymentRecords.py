class PaymentRecord:
    def __init__(self, payment_id, order_id, amount, status):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.status = status

class Order:
    def __init__(self, order_id, customer_id, products):
        self.order_id = order_id
        self.customer_id = customer_id
        self.products = products
        self.payment_records = []

    def record_payment(self, payment_id, amount):
        # Record payment for the order
        payment_record = PaymentRecord(payment_id, self.order_id, amount, status="Paid")
        self.payment_records.append(payment_record)
        print("Payment recorded successfully")

    def update_payment_status(self, payment_id, new_status):
        # Update payment status for the order
        for payment_record in self.payment_records:
            if payment_record.payment_id == payment_id:
                payment_record.status = new_status
                print("Payment status updated successfully")
                return
        print("Payment record not found")
