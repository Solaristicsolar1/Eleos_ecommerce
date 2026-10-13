from decimal import Decimal

class Product:
    def __init__(self, name: str, price: Decimal, stock: int, sku: str) -> None:
        self.name = name
        self._price = price
        self._stock = stock
        self.sku = sku

    def update_price(self, new_price: Decimal) -> None:
        if new_price <= 0:
            raise ValueError("Price of product can't be less than 0")
        self._price = new_price