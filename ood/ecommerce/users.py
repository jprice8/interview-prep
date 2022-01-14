from abc import ABC
class Customer(ABC):
    def __init__(self, cart, order):
        self.__cart = cart
        self.__order = order 

    def get_shopping_cart(self):
        return self.__cart

    def add_item_to_cart(self, item):
        None 

    def remove_item_from_cart(self, item):
        None 

    
class Guest(Customer):
    def register_account(self):
        None 

    
class Member(Customer):
    def __init__(self, name):
        self.__name = name

    def place_order(self, order):
        None
