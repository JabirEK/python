class Customer:
    def __init__(self, customer_id, quantity, price):
        self.customer_id = customer_id
        self.quantity = quantity
        self.price = price
        self.discount = 0

    def generate_bill(self):
        price = self.quantity * self.price
        self.discount_amount = price * self.discount
        actual_price = price - self.discount_amount
        return actual_price

    def generate_coupon(self):
        pass

class SilverCustomer(Customer):
    def __init__(self, id, quantity, price):
        super().__init__(id, quantity, price)
        self.discount = 10/100

class GoldCustomer(Customer):
    def __init__(self, id, quantity, price):
        super().__init__(id, quantity, price)
        self.discount = 20/100

class DiamondCustomer(Customer):
    def __init__(self, customer_id, quantity, price):
        super().__init__(customer_id, quantity, price)
        self.discount = 30/100

cust_zero = Customer('c134',10,100)
print(cust_zero.generate_bill())

cust_one = SilverCustomer('c234',10,100)
print(cust_one.generate_bill())

cust_two = GoldCustomer('c334',10,100)
print(cust_two.generate_bill())

cust_three = DiamondCustomer('c434',10,100)
print(cust_three.generate_bill())

def add(a,b):
    pass
