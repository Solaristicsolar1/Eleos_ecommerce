class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


prd = Product('Denim', 50000, 20)
print(prd.price)