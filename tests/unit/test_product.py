from decimal import Decimal

import pytest

from eleos_ecommerce.products.domain import Product


def test_update_price_successfully():
    product = Product(
        name="Klin",
        price=Decimal("30000.00"),
        stock=15,
        sku="ELC-KL-456",
    )

    product.update_price(Decimal("50000.00"))

    assert product._price == Decimal("50000.00")


def test_update_price_rejects_negative_price():
    product = Product(
        name="Klin",
        price=Decimal("30000.00"),
        stock=15,
        sku="ELC-KL-456",
    )

    with pytest.raises(ValueError):
        product.update_price(Decimal("-500.00"))

    assert product._price == Decimal("30000.00")


def test_update_price_rejects_zero_price():
    product = Product(
        name="Klin",
        price=Decimal("30000.00"),
        stock=15,
        sku="ELC-KL-456",
    )

    with pytest.raises(ValueError):
        product.update_price(Decimal("0.00"))

    assert product._price == Decimal("30000.00")