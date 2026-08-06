from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PaymentProcessor:
    def __init__(self):
        self.payment_strategy = None


    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    
    def process_payment(self, amount):
        if self.payment_strategy is None:
            print("No payment method selected.")
        else:
            self.payment_strategy.pay(amount)


if __name__ == "__main__":
    processor = PaymentProcessor()


    processor.set_payment_strategy(CreditCardPayment())
    processor.process_payment(5000)

    
    processor.set_payment_strategy(PayPalPayment())
    processor.process_payment(2500)

    
    processor.set_payment_strategy(UPIPayment())
    processor.process_payment(1000)