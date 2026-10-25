
# Assignment # 2
# Online Shopping and Payment Processing System

# Parent class for all products
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self):
        return self.price


# Physical product inherits from Product
class PhysicalProduct(Product):
    def __init__(self, name, price, shipping_cost):
        super().__init__(name, price)
        self.shipping_cost = shipping_cost

    def get_total_price(self):
        return self.price + self.shipping_cost


# Digital product inherits from Product
class DigitalProduct(Product):
    def get_total_price(self):
        return self.price


# Parent class for payment methods
class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Payment method must be implemented")


# Card payment inherits from PaymentMethod
class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} completed using Card.")


# Cash payment inherits from PaymentMethod
class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of Rs. {amount:.2f} selected using Cash on Delivery.")


# Order contains multiple products
class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total

    def show_order(self):
        print("\n----- ORDER DETAILS -----")
        for product in self.products:
            print(
                f"{product.name}: Rs. {product.price:.2f}"
                f" | Total with extra cost: Rs. "
                f"{product.get_total_price():.2f}"
            )

        print(f"Order Total: Rs. {self.calculate_total():.2f}")

    def checkout(self, payment_method):
        amount = self.calculate_total()
        print("\n----- CHECKOUT -----")
        payment_method.pay(amount)


# Main program
if __name__ == "__main__":

    # Create sample products
    keyboard = PhysicalProduct("Keyboard", 2500, 200)
    book = PhysicalProduct("Python Book", 1000, 100)
    ebook = DigitalProduct("E-Book", 500)

    # Create an order
    order = Order()
    order.add_product(keyboard)
    order.add_product(book)
    order.add_product(ebook)

    # Display order details
    order.show_order()

    # Checkout using card payment
    card = CardPayment()
    order.checkout(card)

    # Checkout using cash payment
    cash = CashPayment()
    order.checkout(cash)
