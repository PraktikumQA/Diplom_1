import pytest
from praktikum.bun import Bun


class TestBun:

    name_list = ["black bun",
                 "white bun",
                 "red bun"]

    price_list = [100,
                  200,
                  300]

    @pytest.mark.parametrize("name", name_list)
    def test_get_bun_name(self, name):
        bun_name = Bun(name, 111)
        assert bun_name.get_name() == name

    @pytest.mark.parametrize("price", price_list)
    def test_get_bun_price(self, price):
        bun_price = Bun("red bun", price)
        assert bun_price.get_price() == price

    def test_bun_empty_name(self):
        bun = Bun("", 100)
        assert bun.get_name() == ""

    def test_get_name_is_string(self):
        bun_name = Bun("Ultra", 100)
        assert isinstance(bun_name.get_name(), str)
