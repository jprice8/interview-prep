import sys

from products import Product, ProductCategory
from users import Member
from search import Catalog 


if __name__ == '__main__':
    # Create product category and products
    food_category = ProductCategory('food', 'Buy our food')
    food = Product(1, 'food', 'food', 1200.00, 'food', 4)

    # Add products and categories to product catalog
    catalog = Catalog()
    catalog.add_product_category_to_catalog(food_category.get_name(), food_category)
    catalog.add_product_name_to_catalog(food.get_name(), food)

    # Welcome
    print("Welcome to food!")

    # Auth
    name = input("Please enter your name: ")
    new_user = Member(name)

    print('\n')
    print(f'Thank you for being a loyal member {name}!')
    print('\n')

    while True:
        # Main menu
        choices = """
        1: buy product
        2: rage quit
        """
        # First decision
        print('What would you like to do?')
        print(choices)
        user_choice = input('Please select an option: ')

        # If buying...
        if user_choice == '1':
            print('\n')
            user_category = input('Please select a category to shop: ')
            print('\n')

            query_result = catalog.search_products_by_category(user_category)
            print(query_result)
            

        # If quitter...
        elif user_choice == '2':
            print('Goodbye!')
            sys.exit()


