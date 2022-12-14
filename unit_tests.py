import unittest
from calculate import *
from foodstruct import *

class Test_unit_tests(unittest.TestCase):
    def test_M0(self):
        height = 164.0
        weight = 51.0
        age = 23
        sex = False
        activity_level_coefficient = 1.375
        expected_result = 1831.0875
        result = calculate_daily_calories_standart(
            height,
            weight,
            age,
            sex,
            activity_level_coefficient
        )
        self.assertEqual(expected_result, result)

    def test_M1(self):
        height = -164.0
        weight = 51.0
        age = 23
        sex = False
        activity_level_coefficient = 1.375
        expected_result = TypeError
        result = calculate_daily_calories_standart(
            height,
            weight,
            age,
            sex,
            activity_level_coefficient
        )
        self.assertEqual(expected_result, result)

    def test_M2(self):
        height = 164.0
        weight = 51.0
        age = 'stroka'
        sex = False
        activity_level_coefficient = 1.375
        expected_result = TypeError
        result = calculate_daily_calories_standart(
            height,
            weight,
            age,
            sex,
            activity_level_coefficient
        )
        self.assertEqual(expected_result, result)

    def test_M3(self):
        height = 164.0
        weight = []
        age = 23
        sex = False
        activity_level_coefficient = 1.375
        expected_result = TypeError
        result = calculate_daily_calories_standart(
            height,
            weight,
            age,
            sex,
            activity_level_coefficient
        )
        self.assertEqual(expected_result, result)

    def test_M4(self):
        expected_result = 73.0 ##############
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 45.0,
                'proteins': 1.95,
                'fats': 0.33,
                'carbohydrates': 10.89
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 320.0,
                'proteins': 4.0,
                'fats': 29.32,
                'carbohydrates': 17.06
            }
        }
        dish_weight = 500  ##########
        result = calculate_dish_calories(products, dish_weight) ###########
        self.assertEqual(expected_result, result)

    def test_M5(self):
        expected_result = TypeError
        products = 'stroka'
        dish_weight = 300
        result = calculate_dish_calories(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M6(self):
        expected_result = 1.19
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 45.0,
                'proteins': 1.95,
                'fats': 0.33,
                'carbohydrates': 10.89
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 320.0,
                'proteins': 4.0,
                'fats': 29.32,
                'carbohydrates': 17.06
            }
        }
        dish_weight = 500
        result = calculate_dish_proteins(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M7(self):
        expected_result = TypeError
        products = 'stroka'
        dish_weight = 300
        result = calculate_dish_proteins(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M8(self):
        expected_result = 5.93
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 45.0,
                'proteins': 1.95,
                'fats': 0.33,
                'carbohydrates': 10.89
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 320.0,
                'proteins': 4.0,
                'fats': 29.32,
                'carbohydrates': 17.06
            }
        }
        dish_weight = 500
        result = calculate_dish_fats(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M9(self):
        expected_result = TypeError
        products = 'stroka'
        dish_weight = 300
        result = calculate_dish_fats(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M10(self):
        expected_result = 5.59
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 45.0,
                'proteins': 1.95,
                'fats': 0.33,
                'carbohydrates': 10.89
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 320.0,
                'proteins': 4.0,
                'fats': 29.32,
                'carbohydrates': 17.06
            }
        }
        dish_weight = 500
        result = calculate_dish_carbohydrates(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M11(self):
        expected_result = TypeError
        products = 'stroka'
        dish_weight = 300
        result = calculate_dish_carbohydrates(products, dish_weight)
        self.assertEqual(expected_result, result)

    def test_M12(self):
        expected_result = {
            'calories': 160.0,
            'proteins': 2.0,
            'fats': 14.66,
            'carbohydrates': 8.53
        }
        product_name = 'Авокадо'
        result = get_product_nutrients_data(product_name)
        self.assertDictEqual(expected_result, result)

    def test_M13(self):
        product_name = 'Булка'
        expected_result = HTTPError
        result = get_product_nutrients_data(product_name)
        self.assertEqual(expected_result, result)
        
    def test_M14(self):
        product_name = 'Авокадо'
        expected_result = HTTPError
        result = get_product_nutrients_data(product_name)
        self.assertEqual(expected_result, result)

    def test_M15(self):
        product_name = 'Авокадо'
        expected_result = [
            'Авокадо', 
            'Масло авокадо', 
            'Американский сыр', 
            'Абрикос', 
            'Аннона сетчатая', 
            'Апельсин', 
            'Апельсиновый сок', 
            'Ананас', 
            'Айва', 
            'Арбуз']
        result = get_service_recommendations(product_name)
        self.assertEqual(expected_result, result)

    def test_M16(self):
        product_name = 'Булка'
        expected_result = [
            'Бри (сыр)', 
            'Бруност', 
            'Бадьян настоящий', 
            'Бэзил', 
            'Бальзамический уксус', 
            'Бабассу', 
            'Бульон', 
            'Бешамель', 
            'Бефстроганов', 
            'Боквурст']
        result = get_service_recommendations(product_name)
        self.assertEqual(expected_result, result)

    #def test_M17(self):


    #def test_M18(self):


    #def test_M19(self):


    #def test_M20(self):


    #def test_M21(self):


    #def test_M22(self):


    
if (__name__ == '__main__'):
    unittest.main()
