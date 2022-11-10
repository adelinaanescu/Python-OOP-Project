from amplifier import Amplifier
from category import Category
from categories import Categories
from json import JSONDecodeError
from order import Order
from orders import Orders
from product import Product
from products import Products
import sys

#general
from receiver import Receiver


def print_menu(menu: dict):
    for key in menu.keys():
        print (key, '--', menu[key])

def error_handler():
     print("Action not supported")

#categories

def add_category():
    name = input("Enter name for the new category : ")
    cat = Category(name)
    Categories.add_category(cat)

def delete_category():
    name = input("Enter the name for the category you want to delete: ")
    cat = Category(name)
    categories = Categories.load_categories()
    if cat in categories:
        Categories.remove_category(cat)
    else:
        error_handler()

def list_categories():
    try:
        categories = Categories.load_categories()
        for cat in categories:
            print(cat)
    except JSONDecodeError as e:
        categories = None

category_menu_options = {
    1: 'Add category',
    2: 'Remove category',
    3: 'Display all categories',
    0: 'Back to main menu',
}

def category_menu():
    actions = {1: add_category, 2: delete_category, 3: list_categories}
    while True:
        print_menu(category_menu_options)
        option = int(input("Enter an option : "))
        if (option == 0):
            break
        action = actions.get(option, error_handler)
        action()

#products

def add_product():
    category = input("Enter name of the category or None: ")
    name = input("Enter name of the product : ")
    if category == "Amplifier" :
        power = input("Enter power of the "+ name + ": ")
        numerChannels = input("Enter number od channels of the " + name + ": ")
        size = input("Enter size of the " + name + ": ")
        prd = Amplifier(name, power, numerChannels, size)
    elif category == "Receiver":
        color = input("Enter color of the " + name + ": ")
        numerChannels = input("Enter number od channels of the " + name + ": ")
        size = input("Enter size of the " + name + ": ")
        prd = Receiver(name, color, numerChannels, size)
    elif category == "Turntable":
        speed = input("Enter speed of the " + name + ": ")
        connectionType = input("Enter connection type of the " + name + ": ")
        size = input("Enter size of the " + name + ": ")
        prd = Receiver(name, speed, connectionType, size)
    elif category == "None":
        prd = Product(name)
    else:
        error_handler()
        return()

    Products.add_product(prd)

def delete_product():
    name = input("Enter the name for the product you want to delete: ")
    prd = Product(name)
    products = Products.load_products()
    if prd in products:
        Products.remove_product(prd)
    else:
        error_handler()

def list_products():
    try:
        products = Products.load_products()
        for prd in products:
            print(prd)
    except JSONDecodeError as e:
        products = None

def list_products_category():
    category = input("Enter name of the category")
    try:
        products = Products.load_products()
        for prd in products:
            if isinstance(prd,getattr(sys.modules[__name__], category)):
                print(prd)
    except JSONDecodeError as e:
        products = None


products_menu_orders = {
    1: 'Add product',
    2: 'Remove product',
    3: 'Display all products',
    4: 'Display all products from a category',
    0: 'Back to main menu',
}

def products_menu():
    actions = {1: add_product, 2: delete_product, 3: list_products}
    while True:
        print_menu(products_menu_orders)
        option = int(input("Enter an option : "))
        if (option == 0):
            break
        action = actions.get(option, error_handler)
        action()


#orders

def place_order():
    products={}
    storeProducts = Products.load_products()
    address = input(f"Destination address: ")
    for product in storeProducts:
        number = input(f"How many {product.name} do you want to order: ")
        if number != 0:
            products[product.name] = number
    ord = Order(address, products)
    Orders.add_order(ord)


def list_orders():
    try:
        orders = Orders.load_orders()
        for ord in orders:
            print(ord)
    except JSONDecodeError as e:
        orders = None

order_menu_options = {
    1: 'Place order',
    2: 'List orders',
    0: 'Back to main menu',
}

def order_menu():
    actions = {1: place_order, 2: list_orders}
    while True:
        print_menu(order_menu_options)
        option = int(input("Enter an option : "))
        if (option == 0):
            break
        action = actions.get(option, error_handler)
        action()



if __name__ == "__main__":

    main_menu_options ={
        1: 'Categories',
        2: 'Products',
        3: 'Orders',
        0: 'Exit',
    }

    actions = {1: category_menu, 2: products_menu, 3: order_menu}
    while True:
        print_menu(main_menu_options)
        option = int(input("Enter an option : "))
        if (option == 0):
            break
        action = actions.get(option, error_handler)
        action()