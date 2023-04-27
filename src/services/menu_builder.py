import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def check_recipe(self, recipe):
        try:
            if self.inventory.check_recipe_availability(recipe) is False:
                return False
            return True
        except KeyError:
            return False

    # Req 4 e Req 6
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        data = []
        menu_data_dishes = self.menu_data.dishes

        for dish in menu_data_dishes:
            recipe_info = {
                "dish_name": "",
                "ingredients": "",
                "price": 0,
                "restrictions": "",
            }

            recipe_info["restrictions"] = dish.get_restrictions()
            if restriction in recipe_info["restrictions"]:
                continue

            if self.check_recipe(dish.recipe) is False:
                continue

            recipe_info["dish_name"] = dish.name
            recipe_info["ingredients"] = dish.get_ingredients()
            recipe_info["price"] = dish.price
            # recipe_info["restrictions"] = dish.restrictions
            data.append(recipe_info)

        data_dish = pd.DataFrame(data)
        return data_dish
