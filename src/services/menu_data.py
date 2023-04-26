import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        dishes = {}
        with open(source_path, "r") as file:
            for recipe in csv.DictReader(file):
                name = recipe["dish"]
                dish = dishes.get(name)

                if dish is None:
                    dish = Dish(name, float(
                        recipe["price"]
                        ))
                    dishes[name] = dish

                ingredient = Ingredient(recipe["ingredient"])
                recipe_amount = int(recipe["recipe_amount"])
                dish.add_ingredient_dependency(ingredient, recipe_amount)
            self.dishes = set(dishes.values())
