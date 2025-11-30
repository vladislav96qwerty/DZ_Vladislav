class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def get_total(self):
        total = 0
        for item, qty in self.products.items():
            total += item.price * qty
        return total

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, qty in self.products.items():
            result += f"{item.name}: {qty} pcs.\n"
        return result.strip()


lemon = Item("lemon", 5, "yellow", "small")
apple = Item("apple", 2, "red", "middle")

print(lemon)
print(apple)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True
assert cart.get_total() == 60

cart.add_item(apple, 10)
print(cart)
assert cart.get_total() == 40
