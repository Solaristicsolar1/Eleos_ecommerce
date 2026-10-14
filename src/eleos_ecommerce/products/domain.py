
from decimal import Decimal


class Product:
    def __init__(
        self,
        name: str,
        price: Decimal,
        stock: int,
        sku: str,
        description: str | None = None,
        image_url: str | None = None,
    ) -> None:
        if not name.strip():
            raise ValueError("Product name cannot be empty")

        if price <= 0:
            raise ValueError("Product price must be greater than zero")

        if isinstance(stock, bool) or not isinstance(stock, int):
            raise ValueError("Stock must be an integer")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        if not sku.strip():
            raise ValueError("SKU cannot be empty")

        if description is not None and not description.strip():
            raise ValueError("Description cannot be empty")

        if image_url is not None and not image_url.strip():
            raise ValueError("Image URL cannot be empty")

        self.name = name.strip()
        self.description = description.strip() if description else None
        self.image_url = image_url.strip() if image_url else None
        self._price = price
        self._stock = stock
        self.sku = sku.strip()

    def update_price(self, new_price: Decimal) -> None:
        if new_price <= 0:
            raise ValueError("Product price must be greater than zero")

        self._price = new_price

    def decrease_stock(self, quantity: int) -> None:
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if quantity > self._stock:
            raise ValueError("Insufficient stock")

        self._stock -= quantity

    def increase_stock(self, quantity: int) -> None:
        if isinstance(quantity, bool) or not isinstance(quantity, int):
            raise ValueError("Quantity must be an integer")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        self._stock += quantity

    @property
    def price(self) -> Decimal:
        return self._price

    @property
    def stock(self) -> int:
        return self._stock
