# Házi feladat:
# 2. Feladat: Product, Warehouse
import uuid


class Product:
    def __init__(self, product_name, price):
        self._product_name = product_name
        self._price = price

    def __repr__(self):
        rep = 'Product(product_name= \'' + self._product_name + '\', price=' + str(
            self._price) + ')'
        return rep

    @staticmethod
    def get_id():
        uuidStr = str(uuid.uuid4())
        return uuidStr.split("-")[4]


class Warehouse:
    def __init__(self):
        self.products = []
        return

    def add_product(self, product_name, price):
        prod_element = Product(product_name, price)
        if (self.products):
            is_exists = False
            for element in self.products:
                if product_name == element._product_name:
                    is_exists = True
            if (is_exists == False):
                self.products.append(prod_element)
            else:
                print("this product is already exists.")
        else:
            self.products.append(prod_element)

    def remove_product(self, product_name):
        for element in self.products:
            if product_name == element._product_name:
                self.products.remove(element)
                print(product_name + " is removed")

    def display_products(self):
        for element in self.products:
            print(element.get_id() + " " + element._product_name + " " +
                  str(element._price))

    def sort_by_price(self, ascending=True):
        self.products.sort(key=lambda x: x._price, reverse=not (ascending))
        return self.products


warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
for product in warehouse.sort_by_price():
    print(product)

# Az alábbi sorokban teszteltem a részfunkciók működését, amit a feladat nem kért
# print('Reszfunkciok tesztelese')
# warehouse.remove_product('Camera')
# print("---")
# for product in warehouse.sort_by_price(False):
#     print(product)
# print("---")
# warehouse.display_products()

#prod = Product("USB Cable", 20)
#print(repr(prod))
#print(prod.get_id())
