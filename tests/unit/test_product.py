
from decimal import Decimal

import pytest

from eleos_ecommerce.products.domain import Product


@pytest.fixture
def product() -> Product:
    return Product(
        name="Klin",
        price=Decimal("30000.00"),
        stock=15,
        sku="ELC-KL-456",
        description="A quality household cleaning product",
        image_url="https://example.com/images/klin.jpg",
    )


def test_product_creation(product: Product) -> None:
    assert product.name == "Klin"
    assert product.price == Decimal("30000.00")
    assert product.stock == 15
    assert product.sku == "ELC-KL-456"
    assert product.description == "A quality household cleaning product"
    assert product.image_url == "https://example.com/images/klin.jpg"


def test_product_allows_optional_fields() -> None:
    product = Product(
        name="Klin",
        price=Decimal("30000.00"),
        stock=0,
        sku="ELC-KL-456",
    )

    assert product.description is None
    assert product.image_url is None
    assert product.stock == 0


@pytest.mark.parametrize("name", ["", "   "])
def test_product_rejects_empty_name(name: str) -> None:
    with pytest.raises(ValueError, match="Product name cannot be empty"):
        Product(name, Decimal("30000.00"), 15, "ELC-KL-456")


@pytest.mark.parametrize("price", [Decimal("0"), Decimal("-500.00")])
def test_product_rejects_invalid_price(price: Decimal) -> None:
    with pytest.raises(
        ValueError, match="Product price must be greater than zero"
    ):
        Product("Klin", price, 15, "ELC-KL-456")


@pytest.mark.parametrize("stock", [-1, 1.5, True])
def test_product_rejects_invalid_stock(stock: int) -> None:
    with pytest.raises(ValueError):
        Product("Klin", Decimal("30000.00"), stock, "ELC-KL-456")


def test_product_rejects_empty_sku() -> None:
    with pytest.raises(ValueError, match="SKU cannot be empty"):
        Product("Klin", Decimal("30000.00"), 15, "   ")


def test_product_rejects_empty_description() -> None:
    with pytest.raises(ValueError, match="Description cannot be empty"):
        Product(
            "Klin",
            Decimal("30000.00"),
            15,
            "ELC-KL-456",
            description="   ",
        )


def test_product_rejects_empty_image_url() -> None:
    with pytest.raises(ValueError, match="Image URL cannot be empty"):
        Product(
            "Klin",
            Decimal("30000.00"),
            15,
            "ELC-KL-456",
            image_url="   ",
        )


def test_update_price_successfully(product: Product) -> None:
    product.update_price(Decimal("50000.00"))

    assert product.price == Decimal("50000.00")


@pytest.mark.parametrize("price", [Decimal("-500.00"), Decimal("0.00")])
def test_update_price_rejects_invalid_price(
    product: Product, price: Decimal
) -> None:
    with pytest.raises(ValueError):
        product.update_price(price)

    assert product.price == Decimal("30000.00")


def test_decrease_stock_successfully(product: Product) -> None:
    product.decrease_stock(4)

    assert product.stock == 11


def test_decrease_stock_rejects_insufficient_stock(
    product: Product,
) -> None:
    with pytest.raises(ValueError, match="Insufficient stock"):
        product.decrease_stock(20)

    assert product.stock == 15


@pytest.mark.parametrize("quantity", [0, -1])
def test_decrease_stock_rejects_invalid_quantity(
    product: Product, quantity: int
) -> None:
    with pytest.raises(ValueError):
        product.decrease_stock(quantity)

    assert product.stock == 15


def test_increase_stock_successfully(product: Product) -> None:
    product.increase_stock(10)

    assert product.stock == 25


@pytest.mark.parametrize("quantity", [0, -1])
def test_increase_stock_rejects_invalid_quantity(
    product: Product, quantity: int
) -> None:
    with pytest.raises(ValueError):
        product.increase_stock(quantity)

    assert product.stock == 15


def test_price_property(product: Product) -> None:
    assert product.price == Decimal("30000.00")


def test_stock_property(product: Product) -> None:
    assert product.stock == 15
