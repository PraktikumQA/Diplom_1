import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:

    price_list = [100,
                  200,
                  300]

    name_list = ["black bun",
                 "white bun",
                 "red bun"]

    type_list = ["sauce",
                 "filling"]

    @pytest.mark.parametrize("price", price_list)
    def test_get_ingredient_price(self, price):
        ingredient = Ingredient("sauce", "hot sauce", price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("name", name_list)
    def test_get_ingredient_name(self, name):
        ingredient = Ingredient("sause", name, 333)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("type", type_list)
    def test_get_ingredient_type(self, type):
        ingredient = Ingredient(type, "white bun", 222)
        assert ingredient.get_type() == type
