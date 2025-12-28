import pytest



class ShoppingCart:
    """
    Простейшая корзина интернет-магазина.

    Возможности:
    - добавить товар (name, price, quantity)
    - удалить товар по имени
    - посчитать общую стоимость
    - посчитать стоимость со скидкой
    """

    def __init__(self):
        self._items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """Добавить товар в корзину."""
        if price <= 0:
            raise ValueError("Price must be positive")

        if name in self._items:
            self._items[name]["price"] = price
            self._items[name]["quantity"] = quantity
        else:
            self._items[name] = {
                "price": float(price),
                "quantity": int(quantity),
            }

    def remove_item(self, name: str) -> None:
        """Удалить товар из корзины по имени."""
        if name not in self._items:
            raise ValueError(f"Item '{name}' not found")
        del self._items[name]

    def total(self) -> float:
        """Посчитать общую стоимость корзины."""
        total_price = sum((item["price"] * item['quantity']) for item in self._items.values())
        return round(total_price, 2)

    def apply_discount(self, percent: float) -> float:
        """Применить скидку в процентах."""
        if percent < 0 or percent > 100:
            raise ValueError("Discount must be between 0 and 100")

        base_total = self.total()
        discounted = base_total * (1 - percent/100)
        return round(discounted, 2)

    def items(self):
        """Вернуть копию содержимого корзины."""
        return {
            name: {"price": data["price"], "quantity": data["quantity"]}
            for name, data in self._items.items()
        }

@pytest.fixture()
def function_creat_shop():
    shop = ShoppingCart()
    shop.add_item("tabel", 100, 1)
    shop.add_item("tabel1", 200, 3)
    shop.add_item("tabel2", 500, 2)
    return shop

def test_add_item(function_creat_shop):
    function_creat_shop.add_item("tabel3", 100, 1)
    function_creat_shop.add_item('tabel2', 2, 3)
    assert 'tabel3' in function_creat_shop.items()

def test_remove_item(function_creat_shop):
    function_creat_shop.remove_item("tabel2")
    assert 'tabel2' not in function_creat_shop.items()

def test_total(function_creat_shop):
    assert function_creat_shop.total() == 1700

def test_discount(function_creat_shop):
    assert function_creat_shop.apply_discount(50) == 850


#@pytest.mark.xfail
def test_test_discount_negative(function_creat_shop):
    with pytest.raises(ValueError):
        assert function_creat_shop.apply_discount(101)
    with pytest.raises(ValueError):
        assert function_creat_shop.apply_discount(-100)
    with pytest.raises(ValueError):
        assert function_creat_shop.apply_discount(-1)

def test_del_item_negative(function_creat_shop):
    with pytest.raises(ValueError):
        assert function_creat_shop.remove_item("tabel3")

    function_creat_shop.remove_item("tabel2")

    with pytest.raises(ValueError):
        assert function_creat_shop.remove_item("tabel2")

    with pytest.raises(AssertionError):
        assert 'tabel2' in function_creat_shop.items()

def test_add_item_negative(function_creat_shop):
    with pytest.raises(ValueError):
        assert function_creat_shop.add_item('tabel3', 0, 3)

@pytest.mark.xpass
def test_add_item_zero_quantity_negative(function_creat_shop):
        function_creat_shop.add_item('tabel3', 10, 0)
        assert 'tabel3' in function_creat_shop.items()

