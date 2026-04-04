class Product:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def print_info(self):
        print(f'Nimi: {self.name} | Hinta: {self.cost}$')

class Electronics(Product):
    def __init__(self, name, cost, warranty):
        self.warranty = warranty
        super().__init__(name, cost)

    def print_info(self):
        print(f'Elektroniikka: {self.name} | Hinta: {self.cost:.2f}$ | Takuu: {self.warranty}kk')

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_cost(self):
        sum = 0
        for item in self.products:
            sum = sum + item.cost
        return sum

    def show_cart(self):
        for item in self.products:
            item.print_info()


# Main
bread = Product('Bread', 2.50)
phone = Electronics('Iphone', 599.00, 24)

shopping_cart = ShoppingCart()
shopping_cart.add_product(bread)
shopping_cart.add_product(phone)

shopping_cart.show_cart()

total = shopping_cart.calculate_cost()
print(f'Yhteensä: {total:.2f}$')