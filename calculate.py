import json
from json import JSONDecodeError

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

    if (daily_calories_standart <= 0.0):
        return 0.0
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

def calculate_dish_calories(products: dict[str, dict[str, float]], w):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_calories = 0.0
    for key in products.keys():
        dish_calories += (products[key]['calories'])
    dish_calories = round(dish_calories / float(w) * 100, 2)
    
    if (dish_calories <= 0.0):
        return 0.0
    return dish_calories

def calculate_dish_proteins(products: dict[str, dict[str, float]], w):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_proteins = 0.0
    for key in products.keys():
        dish_proteins += (products[key]['proteins'])
    dish_proteins = round(dish_proteins / float(w) * 100, 2)
    
    if (dish_proteins <= 0.0):
        return 0.0
    return dish_proteins


def calculate_dish_fats(products: dict[str, dict[str, float]], w):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_fats = 0.0
    for key in products.keys():
        dish_fats += (products[key]['fats'])
    dish_fats = round(dish_fats / float(w) * 100, 2)

    if (dish_fats <= 0.0):
        return 0.0
    return dish_fats

def calculate_dish_carbohydrates(products: dict[str, dict[str, float]], w):
    if (not complex_dict_is_correct(products)):
        return TypeError

    dish_carbohydrates = 0.0
    for key in products.keys():
        dish_carbohydrates += (products[key]['carbohydrates'])
    dish_carbohydrates = round(dish_carbohydrates / float(w) * 100, 2)

    if (dish_carbohydrates <= 0.0):
        return 0.0
    return dish_carbohydrates

def calculate_and_save_daily_calories(
    sex: bool,
    height: float,
    weight: float,
    age: int,
    activity_level: int
):
    activity_level_coefficients = [1.2, 1.375, 1.55, 1.7, 1.9]
    activity_level_coefficient = activity_level_coefficients[activity_level]
        
    daily_calories_standart = calculate_daily_calories_standart(
        height, 
        weight, 
        age, 
        sex, 
        activity_level_coefficient
    )
    daily_calories_standart = round(daily_calories_standart, 2)

    data = {
        'daily_calories_standart': daily_calories_standart,
        'sex': sex,
        'height': height,
        'weight': weight,
        'age': age,
        'activity_level': activity_level
    }
        
    with open('json\daily_calories_standart.json', 'w+') as outfile:
        json.dump(data, outfile)

    return daily_calories_standart

def get_daily_calories_standart():
    try:
        with open('json\daily_calories_standart.json', 'r') as my_file:
            f = my_file.read()
            try:
                return json.loads(f)['daily_calories_standart']
            except JSONDecodeError:
                return 0.0
    except FileNotFoundError:
        return 0.0
    
def save_100_gramm_dish_nutriens(name_dish, result_100_gramm_proteins, result_100_gramm_fats, result_100_gramm_carbohydrates, result_100_gramm_calories):
        
        dish = {
            name_dish: {
            'proteins': result_100_gramm_proteins,
            'fats': result_100_gramm_fats,
            'carbohydrates': result_100_gramm_carbohydrates,
            'calories': result_100_gramm_calories,
            }
        }

        data = []
        try:
            with open('json\saved_dishes.json', 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        except FileNotFoundError:
            data = []

        data.append(dish)
        with open('json\saved_dishes.json', 'w+', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=True)

        return data


def get_saved_dish():
    try:
        with open('json\saved_dishes.json', 'r', encoding='utf-8') as f:
            try:
                result = json.load(f)
                return result
            except JSONDecodeError:
                return 
    except FileNotFoundError:
        return
