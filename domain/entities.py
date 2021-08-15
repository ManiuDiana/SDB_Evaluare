class Product:
    def __init__(self, name, price, code, company, quantity):
        self._name = name
        self._price = price
        self._code = code
        self._company = company
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_code(self):
        return self._code

    def get_company(self):
        return self._company

    def get_quantity(self):
        return self._quantity

    def set_price(self, new_price):
        self._price = new_price

    def set_code(self, new_code):
        self._code = new_code

    def set_quantity(self, new_quantity):
        self._quantity = new_quantity

    def set_name(self, new_name):
        self._name = new_name

    def set_company(self, new_company):
        self._company = new_company

    def __str__(self):
        return "Name: {0}, Price: {1}, Code: {2}, Company: {3}, Quantity: {4}".format(self._name, self._price, self._code,
                                                                       self._company, self._quantity)