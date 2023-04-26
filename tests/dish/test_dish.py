from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish_one = Dish("hamburguer", 14.70)
    dish_two = Dish("hamburguer", 14.70)
    dish_three = Dish("paella", 39.99)

    assert dish_one.name == "hamburguer"
    assert dish_one == dish_two
    assert dish_three != dish_one

    assert hash(dish_one) == hash(dish_two)
    assert hash(dish_three) != hash(dish_one)

    assert repr(dish_one) == "Dish('hamburguer', R$14.70)"

    third_dish_ingredient = Ingredient("ovo")
    dish_three.add_ingredient_dependency(third_dish_ingredient, 1)

    assert dish_three.get_restrictions() == {Restriction.ANIMAL_DERIVED}
    assert dish_three.get_ingredients() == {third_dish_ingredient}

    with pytest.raises(ValueError):
        Dish("hamburguer", -2)

    with pytest.raises(TypeError):
        Dish("hamburguer", "valor")
