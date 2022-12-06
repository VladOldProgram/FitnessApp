import unittest
from calculate import *
from foodstruct import *

class Test_unit_tests(unittest.TestCase):
    def test_M4(self):
        expected_result = 365.0
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 15.0,
                'proteins': 0.65,
                'fats': 0.11,
                'carbohydrates': 3.63
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 160.0,
                'proteins': 2.0,
                'fats': 14.66,
                'carbohydrates': 8.53
            }
        }
        result = calculate_dish_calories(products)
        self.assertEqual(expected_result, result)

    def test_M5(self):
        expected_result = TypeError
        products = 'stroka'
        result = calculate_dish_calories(products)
        self.assertEqual(expected_result, result)

    def test_M6(self):
        expected_result = 5.95
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 15.0,
                'proteins': 0.65,
                'fats': 0.11,
                'carbohydrates': 3.63
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 160.0,
                'proteins': 2.0,
                'fats': 14.66,
                'carbohydrates': 8.53
            }
        }
        result = calculate_dish_proteins(products)
        self.assertEqual(expected_result, result)

    def test_M7(self):
        expected_result = TypeError
        products = 'stroka'
        result = calculate_dish_proteins(products)
        self.assertEqual(expected_result, result)

    def test_M8(self):
        expected_result = 29.65
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 15.0,
                'proteins': 0.65,
                'fats': 0.11,
                'carbohydrates': 3.63
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 160.0,
                'proteins': 2.0,
                'fats': 14.66,
                'carbohydrates': 8.53
            }
        }
        result = calculate_dish_fats(products)
        self.assertEqual(expected_result, result)

    def test_M9(self):
        expected_result = TypeError
        products = 'stroka'
        result = calculate_dish_fats(products)
        self.assertEqual(expected_result, result)

    def test_M10(self):
        expected_result = 27.95
        products = {
            'Огурец': {
                'weight': 300.0,
                'calories': 15.0,
                'proteins': 0.65,
                'fats': 0.11,
                'carbohydrates': 3.63
            },
            'Авокадо': {
                'weight': 200.0,
                'calories': 160.0,
                'proteins': 2.0,
                'fats': 14.66,
                'carbohydrates': 8.53
            }
        }
        result = calculate_dish_carbohydrates(products)
        self.assertEqual(expected_result, result)

    def test_M11(self):
        expected_result = TypeError
        products = 'stroka'
        result = calculate_dish_carbohydrates(products)
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
        # url = r'https://foodstruct.com/ru/food/' + product_name
        # response = requests.get(url)
        # response.raise_for_status()
        expected_result = HTTPError.response
        result = get_product_nutrients_data(product_name)
        self.assertEqual(expected_result, result)

if (__name__ == '__main__'):
    unittest.main()

