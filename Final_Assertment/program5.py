class Product:
    # Generator for unique IDs
    _id_generator = iter(range(1, 1000))

    def __init__(self, name, price):
        self.id = next(self._id_generator)
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}"


class Depot:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        if not any(p.name == product.name for p in self.inventory):
            self.inventory.append(product)
        else:
            print("Product already exists")

    def remove_product(self, product_name):
        for product in self.inventory:
            if product.name == product_name:
                self.inventory.remove(product)
                return
        print("Product not found in inventory.")

    def display_inventory(self):
        for product in self.inventory:
            print(product)

    def find_product_by_name(self, product_name):
        for product in self.inventory:
            if product.name == product_name:
                return product
        print("Product not found in inventory")
        return None

    def sort_by_price(self):
        self.inventory.sort(key=lambda x: x.price)


p1 = Product("Book", 450)
p2 = Product("pen", 220)
p3 = Product("Notebook", 670)

depot = Depot()
depot.add_product(p1)
depot.add_product(p2)
depot.add_product(p3)

print("Initial inventory present")
depot.display_inventory()

print("\n Find product by name:")
print(depot.find_product_by_name("pen"))

print("\nSorting products")
depot.sort_by_price()
depot.display_inventory()

print("\nRemoving products")
depot.remove_product("pen")
depot.display_inventory()
