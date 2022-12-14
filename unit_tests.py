import unittest
from calculate import *
from foodstruct import *
from dish_nutrients_form import *
from daily_calories_standart_form import *

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
        expected_result = 73.0
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
        result = calculate_dish_calories(products, dish_weight)
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

    #def test_M13(self):
    #    product_name = 'Булка'
    #    expected_result = HTTPError
    #    result = get_product_nutrients_data(product_name)
    #    self.assertEqual(expected_result, result)
        
    #def test_M14(self):
    #    product_name = 'Авокадо'
    #    expected_result = HTTPError
    #    result = get_product_nutrients_data(product_name)
    #    self.assertEqual(expected_result, result)

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

    '''
    def test_M18(self):
        window = tk.Tk()
        notebook = ttk.Notebook(window, width=800, height=800)
        dish_nutrients_form = Dish_nutrients_form(notebook)

        expected_result_0 = 'Огурец'
        expected_result_1 = 300.0
        expected_result_2 = 45.0
        expected_result_3 = 1.95
        expected_result_4 = 0.33
        expected_result_5 = 10.89
        expected_result_6 = 1

        dish_nutrients_form.found_product_name_label.configure(text='Огурец')
        dish_nutrients_form.selected_product_name = 'Огурец'
        dish_nutrients_form.product_weight_stepper_input.insert(0, 300.0)
        dish_nutrients_form.selected_product_nutrients_data['calories'] = 15.0
        dish_nutrients_form.selected_product_nutrients_data['proteins'] = 0.65
        dish_nutrients_form.selected_product_nutrients_data['fats'] = 0.11
        dish_nutrients_form.selected_product_nutrients_data['carbohydrates'] = 3.63
        dish_nutrients_form.add_product()

        rows = dish_nutrients_form.dish_ingredients_table.get_children()
        result_0 = dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][0]
        result_1 = float(dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][5])
        result_2 = float(dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][1])
        result_3 = float(dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][2])
        result_4 = float(dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][3])
        result_5 = float(dish_nutrients_form.dish_ingredients_table.item(rows[0])['values'][4])
        result_6 = len(rows)

        self.assertEqual(expected_result_0, result_0)
        self.assertEqual(expected_result_1, result_1)
        self.assertEqual(expected_result_2, result_2)
        self.assertEqual(expected_result_3, result_3)
        self.assertEqual(expected_result_4, result_4)
        self.assertEqual(expected_result_5, result_5)
        self.assertEqual(expected_result_6, result_6)
    '''
    '''
    def test_M19(self):
        window = tk.Tk()
        notebook = ttk.Notebook(window, width=800, height=800)
        dish_nutrients_form = Dish_nutrients_form(notebook)

        expected_result = 0

        dish_nutrients_form.found_product_name_label.configure(text='')
        dish_nutrients_form.selected_product_name = ''
        dish_nutrients_form.product_weight_stepper_input.insert(0, '')
        dish_nutrients_form.selected_product_nutrients_data = HTTPError
        dish_nutrients_form.add_product()

        rows = dish_nutrients_form.dish_ingredients_table.get_children()
        result = len(rows)

        self.assertEqual(expected_result, result)
    '''
    '''
    def test_M20(self):
        window = tk.Tk()
        notebook = ttk.Notebook(window, width=800, height=800)
        dish_nutrients_form = Dish_nutrients_form(notebook)

        expected_result = 0

        dish_nutrients_form.found_product_name_label.configure(text='Огурец')
        dish_nutrients_form.selected_product_name = 'Огурец'
        dish_nutrients_form.product_weight_stepper_input.insert(0, 300.0)
        dish_nutrients_form.selected_product_nutrients_data['calories'] = 15.0
        dish_nutrients_form.selected_product_nutrients_data['proteins'] = 0.65
        dish_nutrients_form.selected_product_nutrients_data['fats'] = 0.11
        dish_nutrients_form.selected_product_nutrients_data['carbohydrates'] = 3.63
        dish_nutrients_form.add_product()
        dish_nutrients_form.found_product_name_label.configure(text='Авокадо')
        dish_nutrients_form.selected_product_name = 'Авокадо'
        dish_nutrients_form.product_weight_stepper_input.insert(0, 200.0)
        dish_nutrients_form.selected_product_nutrients_data['calories'] = 160.0
        dish_nutrients_form.selected_product_nutrients_data['proteins'] = 2.0
        dish_nutrients_form.selected_product_nutrients_data['fats'] = 14.66
        dish_nutrients_form.selected_product_nutrients_data['carbohydrates'] = 8.53
        dish_nutrients_form.add_product()

        dish_nutrients_form.clear_table()

        rows = dish_nutrients_form.dish_ingredients_table.get_children()
        result = len(rows)

        self.assertEqual(expected_result, result)
    '''
    '''
    def test_M21(self):
        window = tk.Tk()
        notebook = ttk.Notebook(window, width=800, height=800)
        daily_calories_standart = Daily_calories_standart(notebook)

        expected_result = daily_calories_standart.activity_level_description_text.get('1.0', END)

        daily_calories_standart.selected_activity_level.set(2)
        daily_calories_standart.switch_activity_level_description()

        result = daily_calories_standart.activity_level_description_text.get('1.0', END)

        self.assertNotEqual(expected_result, result)
    '''
    '''
    def test_M22(self):
        window = tk.Tk()
        notebook = ttk.Notebook(window, width=800, height=800)
        daily_calories_standart = Daily_calories_standart(notebook)

        expected_result = daily_calories_standart.activity_level_description_text.get('1.0', END)

        daily_calories_standart.selected_activity_level.set(0)
        daily_calories_standart.switch_activity_level_description()

        result = daily_calories_standart.activity_level_description_text.get('1.0', END)

        self.assertEqual(expected_result, result)
    '''
    #def test_M22(self):
    
    def test_I0(self):
        sex = False
        height = 164.0
        weight = 51.0
        age = 23
        activity_level = 1
        expected_result = 1831.09
        calculate_and_save_daily_calories(sex, height, weight, age, activity_level)
        result = get_daily_calories_standart()
        self.assertEqual(expected_result, result)
        
    def test_I1(self):
        sex = False
        height = 'stroka'
        weight = []
        age = -23
        activity_level = 10
        expected_result = 0.0
        calculate_and_save_daily_calories(sex, height, weight, age, activity_level)
        result = get_daily_calories_standart()
        self.assertEqual(expected_result, result)


    
if (__name__ == '__main__'):
    unittest.main()
