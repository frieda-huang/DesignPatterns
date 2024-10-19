"""
Facade structural pattern provides a simplified interface to a complex subsystem.

Basic Structure
- Facade class provides a high-level interface for the client
- Subsystem class represents the complex system that performs specific functions
- Client uses the facade to interact with the subsystem
"""


class PaymentGateway:
    def process_payment(self, amount):
        print(f"Processing payment of ${amount}...")
        return True


class InventorySystem:
    def check_stock(self, product_id):
        print(f"Checking stock for product {product_id}...")
        return True

    def reserve_product(self, product_id):
        print(f"Reserving product {product_id} in inventory...")
        return True


class EmailService:
    def send_email(self, email, message):
        print(f"Sending email to {email}: {message}")


class ShippingService:
    def create_shipment(self, product_id, address):
        print(f"Creating shipment for product {product_id} to {address}...")
        return True


class CheckoutFacade:
    def __init__(self):
        self.payment_gateway = PaymentGateway()
        self.inventory_system = InventorySystem()
        self.email_service = EmailService()
        self.shipping_service = ShippingService()

    def complete_checkout(self, product_id, amount, email, shipping_address):
        if not self.inventory_system.check_stock(product_id):
            print("Product is out of stock.")
            return False

        if not self.payment_gateway.process_payment(amount):
            print("Payment failed.")
            return False

        if not self.inventory_system.reserve_product(product_id):
            print("Could not reserve the product.")
            return False

        if not self.shipping_service.create_shipment(product_id, shipping_address):
            print("Could not create the shipment.")
            return False

        self.email_service.send_email(
            email, f"Your order for product {product_id} has been placed successfully!"
        )

        print("Checkout completed successfully!")
        return True


if __name__ == "__main__":

    checkout_facade = CheckoutFacade()

    product_id = "AGI2025"
    amount = 199.99
    email = "me@example.com"
    shipping_address = "Mars"

    checkout_facade.complete_checkout(product_id, amount, email, shipping_address)
