class Order:
    discount = 0.25

    def __init__(self, price, strategy):
        self.price = price
        strategy(Order)

    def final_price(self):
        return int(self.price - self.price * Order.discount)


def morning_discount(order):
    order.discount = 0.5


def elder_discount(order):
    order.discount = 0.9


order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10