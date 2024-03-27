class PaymentFailedException(Exception):
    pass

class PaymentProcessor:
    def process_payment(self, amount):
        raise PaymentFailedException("Payment failed: Transaction declined")

class Order:
    def __init__(self, order_id, amount):
        self.order_id = order_id
        self.amount = amount

    def process_payment(self):
        payment_processor = PaymentProcessor()
        try:
            payment_processor.process_payment(self.amount)
            print("Payment processing successful")
        except PaymentFailedException as e:
            print(f"Payment processing failed: {str(e)}")