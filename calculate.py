def calculate_daily_calories_standart(
    height: float, 
    weight: float, 
    age: int, 
    sex: bool, 
    activity_level_coefficient: float
):
    if (not isinstance(height, float)
        or not isinstance(weight, float)
        or not isinstance(age, int)
        or not isinstance(sex, bool)
        or not isinstance(activity_level_coefficient, float)
        or height <= 0.0
        or weight <= 0.0
        or age <= 0
        or activity_level_coefficient <= 0.0
    ):
        return TypeError

    daily_calories_standart = 0.0
    if (sex == True):
        daily_calories_standart = activity_level_coefficient * (66 + (5 * height) + (13.7 * weight) - (6.8 * age))
    else:
        daily_calories_standart = activity_level_coefficient * (655 + (1.8 * height) + (9.6 * weight) - (4.7 * age))

    return daily_calories_standart

def complex_dict_is_correct(products: dict[str, dict[str, float]]):
    if (not isinstance(products, dict)):
        return False
    for key in products.keys():
        if (not isinstance(key, str) or not isinstance(products[key], dict)):
            return False
        for subkey in products[key].keys():
            if (not isinstance(subkey, str) 
                or not subkey in ['weight', 'calories', 'proteins', 'fats', 'carbohydrates']
                or not isinstance(products[key][subkey], float)
            ):
                return False

    return True

def calculate_dish_calories(products: dict[str, dict[str, float]]):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_calories = 0.0
    for key in products.keys():
        dish_calories += (products[key]['calories'])

    return dish_calories

def calculate_dish_proteins(products: dict[str, dict[str, float]]):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_proteins = 0.0
    for key in products.keys():
        dish_proteins += (products[key]['proteins'])

    return dish_proteins

def calculate_dish_fats(products: dict[str, dict[str, float]]):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_fats = 0.0
    for key in products.keys():
        dish_fats += (products[key]['fats'])

    return dish_fats

def calculate_dish_carbohydrates(products: dict[str, dict[str, float]]):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_carbohydrates = 0.0
    for key in products.keys():
        dish_carbohydrates += (products[key]['carbohydrates'])

    return dish_carbohydrates

def calculate_dish_weight(products: dict[str, dict[str, float]]):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_weight = 0.0
    for key in products.keys():
        dish_weight += products[key]['weight']

    return dish_weight
