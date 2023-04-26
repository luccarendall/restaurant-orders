from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("farinha")
    ingredient_two = Ingredient("farinha")
    ingredient_three = Ingredient("manteiga")

    assert ingredient_one.name == "farinha"
    assert ingredient_two.name == "farinha"
    assert ingredient_three.name == "manteiga"

    assert ingredient_one == ingredient_two
    assert ingredient_one != ingredient_three
    assert ingredient_two != ingredient_three

    assert hash(ingredient_one) == hash(ingredient_two)
    assert hash(ingredient_one) != hash(ingredient_three)

    assert repr(ingredient_three) == "Ingredient('manteiga')"
    assert repr(ingredient_two) == "Ingredient('farinha')"

    assert ingredient_three.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.LACTOSE
    }
