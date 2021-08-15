from entities import Product
from services import Service

class UI:

    def __init__(self, service : Service):
        self.__service = service

    def print_menu(self):
        print("1. Show product list")
        print("2. Add product to the list")
        print("3. Delete product from the list")
        print("4. Edit product data")
        print("5. Show products from a given company")
        print("0. Exit")

    def __validate_name(self, name):
        for Product in self.__service.get_all_products():
            if Product.get_name() == name:
                raise ValueError("\nThis product already exists!\n")

    def __validate_code(self, code):
        for Product in self.__service.get_all_products():
            if Product.get_code() == code:
                raise ValueError("\nThis code already exists!\n")

    def __find_code(self, code):
        position = self.__service._get_product_pos(code)
        if position is None:
            raise ValueError("Product with code {0} does not exist!\n".format(code))
        elif code != int(code):
            raise ValueError("Incorrect code!\n")

    def __validate_input(self, word):
        if word != "name" and word != "Name" and word != "price" and word != "Price" and word != "code" and word != "Code" and word != "company" and word != "Company" and word != "quantity" and word != "Quantity":
            raise ValueError("Attribute {0} does not exist!\n".format(word))


#privata - se foloseste doar in run
    def __add(self):
        print("\nPlease enter name in lower case!")
        name = input("Product name: ")
        self.__validate_name(name)
        price = input("Price: ")
        code = input("Code: ")
        self.__validate_code(code)
        company = input("Company: ")
        quantity = input("Quantity: ")
        self.__service.add_product(Product(name, price, code, company, quantity))
        print("\nProduct added successfully!")
        pos = self.__service._get_product_pos(code)
        print(self.__service._Product_list[pos], '\n')


#se foloseste doar in run
    def __print_product_list(self):
        for Product in self.__service.get_all_products():
            print(Product)


# se foloseste doar in run
    def __delete(self):
        code = input("Enter product code: ")
        self.__find_code(code)
        self.__service.delete_product(code)
        print("\nProduct deleted successfully!")

    def __edit(self):
        code = input("Enter product code: ")
        self.__find_code(code)
        change = input("What do you want to change?  ")
        self.__validate_input(change)
        new_data = input("New {0}: ".format(change))
        self.__service.edit_product(code, change, new_data)
        print("\nProduct data changed successfully!")
        pos = self.__service._get_product_pos(code)
        print(self.__service._Product_list[pos])
        print('\n')

    def run(self):
        while True:
            self.print_menu()
            try:
                command = int(input("Choose the command: ").strip())
                if(command == 0):
                    print("\nThank you for using our services!")
                    break
                elif command == 1:
                     self.__print_product_list()
                elif command == 2:
                   self.__add()
                elif command == 3:
                    self.__delete()
                elif command == 4:
                    self.__edit()
            except ValueError as error:
                print(error)
