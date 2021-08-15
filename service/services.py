from domain.entities import Product

class Service:
    def __init__(self):
        self._Product_list = [Product("Ceai de tei", 4, "543", "Fanta", 20),
                               Product("Lapte", 9, "299", "Napolact", 18),
                               Product("Baton de cereale", 5, "76", "Nestle", 30)]

#este functie pblica - se va folosi in ui
    def get_all_products(self):
        if len(self._Product_list) == 0:
            return ValueError("\nNo products for now!")
        return self._Product_list

#este fct publica
    def add_product(self, new_product):
        for Product in self._Product_list:
            if(Product == new_product):
                raise ValueError("The product {0} already exists".format(new_product))
        self._Product_list.append(new_product)

#este fct privata - se foloseste doar in interiorul services
    def _get_product_pos(self, code):
        for i in range(len(self._Product_list)):
            if self._Product_list[i].get_code() == code:
                return i
        return None

#este publica - se foloseste in ui
    def delete_product(self, code):
        product_pos = self._get_product_pos(code)
        del self._Product_list[product_pos]

    def edit_product(self, code, change, new_data):
        product_pos = self._get_product_pos(code)
        if change == "name" or change == "Name":
            self._Product_list[product_pos].set_name(new_data)
        elif change == "price" or change == "Price":
            self._Product_list[product_pos].set_price(new_data)
        elif change == "code" or change == "Code":
            self._Product_list[product_pos].set_code(new_data)
        elif change == "company" or change == "Company":
            self._Product_list[product_pos].set_company(new_data)
        elif change == "quantity" or change == "Quantity":
            self._Product_list[product_pos].set_quantity(new_data)

