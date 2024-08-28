from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Mock(Bun)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock(Ingredient)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock(Ingredient)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self):
        burger = Burger()
        ingredient1 = Mock(Ingredient)
        ingredient2 = Mock(Ingredient)
        ingredient3 = Mock(Ingredient)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(2, 0)
        assert burger.ingredients[0] == ingredient3
        assert burger.ingredients[1] == ingredient1

    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        assert burger.get_price() == 400.0

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[2])
        burger.add_ingredient(database.available_ingredients()[2])
        burger.add_ingredient(database.available_ingredients()[4])

        expected_receipt = "(==== red bun ====)\n" \
                           "= sauce chili sauce =\n" \
                           "= filling dinosaur =\n" \
                           "(==== red bun ====)\n\n" \
                           "Price: 1100"

        assert burger.get_receipt() == expected_receipt
