class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class Machine:
    def __init__(self):
        self.products = {}
        self.balance = 0

    def new_product(self, name: str, price: int):
        price = int(price)
        try:
            if price <= 0:
                raise ValueError("Please enter a value greater than 0 for price.")
        except ValueError as e:
            print(f"Error occured entering valid price: {e}")

        product = Product(name, price)
        self.products[name] = product

    def print_products(self):
        for key, val in self.products.items():
            print("Printing all products")
            print("----")
            print(f"Item: {key}. Price: {val.price}.\n")
            print("----")

    def insert_coin(self, amount: str):
        amount = int(amount)
        self.balance += amount

    def purchase(self, name: str):
        product = self.products[name]
        if product.price <= self.balance:
            self.balance -= product.price
            return True
        return False

    def checkout(self):
        print(self.balance)
        # Clear state for next user
        self.balance = 0

if __name__ == '__main__':
    m = Machine()
    print(m.new_product('apple', '4'))
    print(m.insert_coin('5'))
    print(m.purchase('apple')) # True
    print(m.purchase('apple')) # False
    print(m.checkout()) # 1