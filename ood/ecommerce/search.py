from abc import ABC, abstractmethod


class Search(ABC):
    def search_products_by_name(self, name):
        None 

    def search_products_by_category(self, category):
        None 


class Catalog(Search):
    def __init__(self):
        self.__product_names = {}
        self.__product_categories = {}

    def add_product_name_to_catalog(self, name, product):
        self.__product_names[name] = product

    def add_product_category_to_catalog(self, name, category):
        self.__product_categories[name] = category

    def search_products_by_name(self, name):
        return self.__product_names.get(name)

    def search_products_by_category(self, category):
        return self.__product_categories.get(category)
