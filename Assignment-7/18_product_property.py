class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @price.deleter
    def price(self):
        del self.__price

p = Product(1000)
print(p.price)
p.price = 2000
print(p.price)
del p.price