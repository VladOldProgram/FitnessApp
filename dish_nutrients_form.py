import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *
from calculate import *
import json
import os.path


# Описывает структуру и работу первой экранной формы Подсчет КБЖУ готового блюда
class Dish_nutrients_form(tk.Frame):
    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

        self.image_loupa = ImageTk.PhotoImage(file='assets\images\loupa_small.png')
        self.loupa = Label(self, image=self.image_loupa)
        self.loupa.place(x=26, y=6)

        self.label_txtMealWeight = tk.Label(self, text='КБЖУ готового блюда', font='Arial 15 bold')
        self.label_txtMealWeight.place(x=710, y=0)

        # Кнопка сохранения блюда
        self.save_dish_button = tk.Button(self, text='Сохранить\n блюдо', font=('Arial', 10), command = self.save_dish)
        self.save_dish_button.place(x=400, y=750)

        self.searchbtn = tk.Button(self, text='Найти', font=('Arial', 10), command=self.show_service_recommendations)
        self.searchbtn.place(x=380, y=10)
             
        # поисковая строка
        self.search_line = tk.Entry(self, fg='Grey')
        self.entry_text2 = 'Поиск продуктов'
        self.search_line.insert(0, self.entry_text2)
        self.search_line.bind('<FocusIn>', lambda args: self.focus_in_entry_box(self.search_line))
        self.search_line.bind('<FocusOut>', lambda args: self.focus_out_entry_box(self.search_line, self.entry_text2))
        self.search_line.place(x=50, y=10, width=300)

        # поле для информации о продукте
        self.frame_info_product = tk.LabelFrame(self, width=430, height=285)
        self.frame_info_product.place(x=30, y=50)
        self.label_info_product = tk.Label(self.frame_info_product, text='Информация о продукте в 100 граммах', font=('Arial', 10))
        self.label_info_product.place(x=90, y=10)
        
        # Поле ввода веса продукта для добавления в список
        self.product_weight_stepper_input = ttk.Entry(self.frame_info_product, font=('Arial', 10), width=10, validate='key')
        self.product_weight_stepper_input['validatecommand'] = (self.product_weight_stepper_input.register(self.value_is_float), '%P', '%d')
        self.product_weight_stepper_input.place(x=160, y=55)

        # Лейбл с названием продукта
        self.found_product_name_label = Label(self.frame_info_product, text='')
        self.found_product_name_label.place(x=20, y=53)

        # Лейбл с информацией о количестве калорий в продукте
        self.found_product_calories_label = Label(self.frame_info_product, text='')
        self.found_product_calories_label.place(x=150, y=100)

        # Лейбл с информацией о количестве белков в продукте
        self.found_product_proteins_label = Label(self.frame_info_product, text='')
        self.found_product_proteins_label.place(x=150, y=150)

        # Лейбл с информацией о количестве жиров в продукте
        self.found_product_fats_label = Label(self.frame_info_product, text='')
        self.found_product_fats_label.place(x=150, y=200)

        # Лейбл с информацией о количестве углеводов в продукте
        self.found_product_carbohydrates_label = Label(self.frame_info_product, text='')
        self.found_product_carbohydrates_label.place(x=150, y=250)

        # Кнопка добавления продукта в список
        self.add_product_button = tk.Button(self.frame_info_product, text='Добавить в список', font=('Arial', 10), command=self.add_product)
        self.add_product_button.place(x=270, y=50)

        # Лейбл с информацией о количестве калорий в продукте
        self.found_product_calories = tk.Label(self.frame_info_product, text='Калорийность', font=('Arial', 10))
        self.found_product_calories.place(x=20, y=100)

        # Лейбл с информацией о количестве белков в продукте
        self.found_product_proteins = tk.Label(self.frame_info_product, text='Белки', font=('Arial', 10))
        self.found_product_proteins.place(x=20, y=150)

        # Лейбл с информацией о количестве жиров в продукте
        self.found_product_fats = tk.Label(self.frame_info_product, text='Жиры', font=('Arial', 10))
        self.found_product_fats.place(x=20, y=200)

        # Лейбл с информацией о количестве углеводов в продукте
        self.found_product_carbohydrates = tk.Label(self.frame_info_product, text='Углеводы', font=('Arial', 10))
        self.found_product_carbohydrates.place(x=20, y=250)

        # Лейбл для ввода веса готового блюда
        self.full_dish_weight_stepper_label = tk.Label(self, text='Введите вес готового блюда в граммах', font=('Arial', 10))
        self.full_dish_weight_stepper_label.place(x=50, y=360)

        # Поле ввода веса готового блюда
        self.full_dish_weight_stepper_input = ttk.Entry(self, validate='key')
        self.full_dish_weight_stepper_input['validatecommand'] = (self.full_dish_weight_stepper_input.register(self.value_is_float), '%P', '%d')
        self.full_dish_weight_stepper_input.place(x=300, y=360, width=60)

        # поле для информации о КБЖУ готового блюда
        self.frame_info_dish = tk.LabelFrame(self, width=430, height=290)
        self.frame_info_dish.place(x=30, y=450)

        self.label_info_dish = tk.Label(self.frame_info_dish, text='КБЖУ готового блюда', font=('Arial', 10))
        self.label_info_dish.place(x=140, y=10)

        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Итог для', font=('Arial', 10))
        self.results_dish_calories.place(x=130, y=60)

        self.results_dish_calories = tk.Label(self.frame_info_dish, text='гр.', font=('Arial', 10))
        self.results_dish_calories.place(x=250, y=60)

        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Итог для 100 гр.', font=('Arial', 10))
        self.results_dish_calories.place(x=300, y=60)

        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Калорийность', font=('Arial', 10))
        self.results_dish_calories.place(x=20, y=100)

        self.results_dish_proteins = tk.Label(self.frame_info_dish, text='Белки', font=('Arial', 10))
        self.results_dish_proteins.place(x=20, y=150)

        self.results_dish_fats = tk.Label(self.frame_info_dish, text='Жиры', font=('Arial', 10))
        self.results_dish_fats.place(x=20, y=200)

        self.results_dish_carbohydrates = tk.Label(self.frame_info_dish, text='Углеводы', font=('Arial', 10))
        self.results_dish_carbohydrates.place(x=20, y=250)

        # Лейбл с информацией о количестве калорий в 100 граммах блюда
        self.results_dish_calories_label= Label(self.frame_info_dish, text='') 
        self.results_dish_calories_label.place(x=300, y=100) 

        # Лейбл с информацией о количестве белков в 100 граммах блюда
        self.results_dish_proteins_label = Label(self.frame_info_dish, text='') 
        self.results_dish_proteins_label.place(x=300, y=150)  

        # Лейбл с информацией о количестве жиров в 100 граммах блюда
        self.results_dish_fats_label = Label(self.frame_info_dish, text='') 
        self.results_dish_fats_label.place(x=300, y=200)  

        # Лейбл с информацией о количестве углеводов в 100 граммах блюда.
        self.results_dish_carbohydrates_label = Label(self.frame_info_dish, text='')
        self.results_dish_carbohydrates_label.place(x=300, y=250) 

        # Лейбл с информацией о количестве калорий в полном весе блюда
        self.results_full_dish_calories_label = Label(self.frame_info_dish, text='') 
        self.results_full_dish_calories_label.place(x=150, y=100) 

        # Лейбл с информацией о количестве белков в полном весе блюда
        self.results_full_dish_proteins_label = Label(self.frame_info_dish, text='') 
        self.results_full_dish_proteins_label.place(x=150, y=150)  

        # Лейбл с информацией о количестве жиров в полном весе блюда
        self.results_full_dish_fats_label = Label(self.frame_info_dish, text='') 
        self.results_full_dish_fats_label.place(x=150, y=200)  

        # Лейбл с информацией о количестве углеводов в полном весе блюда
        self.results_full_dish_carbohydrates_label = Label(self.frame_info_dish, text='')
        self.results_full_dish_carbohydrates_label.place(x=150, y=250) 

        # Поле ввода названия блюда для сохранения
        self.dish_name_text_input = tk.Entry(self, fg='Grey')
        self.entry_text = 'Введите название блюда'
        self.dish_name_text_input.insert(0, self.entry_text)
        self.dish_name_text_input.bind('<FocusIn>', lambda args: self.focus_in_entry_box(self.dish_name_text_input))
        self.dish_name_text_input.bind('<FocusOut>', lambda args: self.focus_out_entry_box(self.dish_name_text_input, self.entry_text))
        self.dish_name_text_input.place(x=50, y=760, width=300)

        self.frame = ttk.Frame(self)
        self.frame.place(x=500, y=40)

        # Таблица ингредиентов блюда и информации о них
        self.dish_ingredients_table = ttk.Treeview(
            self.frame, 
            columns=(
                'txtProductName', 
                'txtProductCalories', 
                'txtProductProteins', 
                'txtProductFats', 
                'txtProductCarbohydrates', 
                'txtProductWeight'
            ), 
            height=34, 
            show='headings')
        self.dish_ingredients_table.column('txtProductName', width=150, anchor=tk.CENTER)
        self.dish_ingredients_table.column('txtProductCalories', width=95, anchor=tk.CENTER)
        self.dish_ingredients_table.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.dish_ingredients_table.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.dish_ingredients_table.column('txtProductCarbohydrates',width=80, anchor=tk.CENTER)
        self.dish_ingredients_table.column('txtProductWeight', width=80, anchor=tk.CENTER)
        self.dish_ingredients_table.heading('txtProductName', text='Продукт')
        self.dish_ingredients_table.heading('txtProductCalories', text='Калории, ккал.')
        self.dish_ingredients_table.heading('txtProductProteins', text='Белки, гр.')
        self.dish_ingredients_table.heading('txtProductFats', text='Жиры, гр.')
        self.dish_ingredients_table.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.dish_ingredients_table.heading('txtProductWeight', text='Вес, гр.')

        # Линейка прокрутки для списка
        self.scroll = tk.Scrollbar(self.frame, command=self.dish_ingredients_table.yview)
        self.scroll.place(x=1560, y=50, height=695)
        self.dish_ingredients_table.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.dish_ingredients_table.pack()

        # Кнопка очистки таблицы ингредиентов блюда
        self.clear_table_button  = tk.Button(self, text='Очистить таблицу', font=('Arial', 10), command=self.clear_table)
        self.clear_table_button .place(x=750, y=770)

        # Кнопка удаления конкретного ингредиента блюда из таблицы
        self.delete_line_button = tk.Button(self, text='Удалить запись из таблицы', font=('Arial', 10), command=self.delete_line)
        self.delete_line_button.place(x=900, y=770)

        self.results_dish_calories11 = tk.Label(self.frame_info_dish, text='', font=('Arial', 10))
        self.results_dish_calories11.place(x=200, y=60)


    def value_is_float(self, P, d):
        if d == '1':
            try:
                float(P)
            except ValueError:
                return False
            return True
        if d == '0':
            if len(P) == 0: 
                return True
            try:
                float(P)
            except ValueError:
                return False
            return True

            
    # Удаляет все строки таблицы ингредиентов блюда
    def clear_table(self):
        if len(self.dish_ingredients_table.get_children()) == 0:
            mb.showinfo('Удаление', 'Список продуктов пуст.')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить все продукты из списка?')
            if answer:
                self.dish_name_text_input.delete(0, tk.END)
                self.full_dish_weight_stepper_input.delete(0, tk.END)
                self.dish_ingredients_table.delete(*self.dish_ingredients_table.get_children())
                mb.showinfo(message = 'Список продуктов очищен.')
                
    # Удаляет выбранную пользователем строку из таблицы ингредиентов блюда
    def delete_line(self):
        if not self.dish_ingredients_table.selection():
            mb.showinfo('Удаление', 'Продукт для удаления не выбран.')
        else:
            answer = mb.askyesno(
                message='Вы уверены, что хотите удалить выбранный продукт?')
            if answer:
                item = self.dish_ingredients_table.selection()[0]
                self.dish_ingredients_table.delete(item)
                self.dish_ingredients_table.config(height=34)
                mb.showinfo(message='Выбранный продукт удален.')

    # Добавляет строку-заполнитель поисковой строки (название)
    def focus_out_entry_box(self, self1, self_text):
        if self1['fg'] == 'Black' and len(self1.get()) == 0:
            self1.delete(0, tk.END)
            self1['fg'] = 'Grey'
            self1.insert(0, self_text)

    # Убирает строку-заполнитель поисковой строки (название)
    def focus_in_entry_box(self, self3):
        if self3['fg'] == 'Grey':
            self3['fg'] = 'Black'
            self3.delete(0, tk.END)

    # Метод записывает название готового блюда и его КБЖУ на 100 грамм в файл saved_dishes.json 
    def save_dish(self):
        rows = self.dish_ingredients_table.get_children()
        #if len(rows) == 0 or self.full_dish_weight_stepper_input.get() == '' or self.dish_name_text_input == 'Введите название блюда' or self.dish_name_text_input == '':
        if len(rows) == 0:
            mb.showinfo('Уведомление', 'Заполните таблицу!')
            return
        elif self.full_dish_weight_stepper_input.get() == '':
            mb.showinfo('Уведомление', 'Введите вес готового блюда!')
            return
        elif self.dish_name_text_input.get() == 'Введите название блюда' or self.dish_name_text_input.get() == '':
            mb.showinfo('Уведомление', 'Введите название блюда!')
            return

        self.results_dish_calories11.config(text=self.full_dish_weight_stepper_input.get())
        self.s = str(self.dish_name_text_input.get())
        #print(self.s)

        self.dict_products = {}
        self.dict_products_zapacnoy = {}
        rows = self.dish_ingredients_table.get_children()

        for i in range(len(rows)):

            print('Продукт = ', self.dish_ingredients_table.item(rows[i])['values'][0])

            # если продукт из таблицы содержаться в словаре
            if self.dish_ingredients_table.item(rows[i])['values'][0] in self.dict_products.keys():
                # создаем запасной словарь
                print('Сделали запасной')
                self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]] = {
                    'calories': float(self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]]['calories']),
                    'proteins': float(self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]]['proteins']),
                    'fats': float(self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]]['fats']),
                    'carbohydrates': float(self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]]['carbohydrates']),
                    'weight': float(self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]]['weight'])
                    }
                    
                self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]] = {
                    'calories': float(self.dish_ingredients_table.item(rows[i])['values'][1]) + float(self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]]['calories']), 
                    'proteins': float(self.dish_ingredients_table.item(rows[i])['values'][2]) + float(self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]]['proteins']), 
                    'fats': float(self.dish_ingredients_table.item(rows[i])['values'][3]) + float(self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]]['fats']), 
                    'carbohydrates': float(self.dish_ingredients_table.item(rows[i])['values'][4]) + float(self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]]['carbohydrates']), 
                    'weight': float(self.dish_ingredients_table.item(rows[i])['values'][5]) + float(self.dict_products_zapacnoy[self.dish_ingredients_table.item(rows[i])['values'][0]]['weight'])
                    } 

                print('ЗАПАСНОЙ СЛОВАРЬ', self.dict_products_zapacnoy)
                self.dict_products_zapacnoy = {}


            else: # иначе добавляем в словарь
                print('Добавили 1 раз')
                self.dict_products[self.dish_ingredients_table.item(rows[i])['values'][0]] = {
                    'calories': float(self.dish_ingredients_table.item(rows[i])['values'][1]) , 
                    'proteins': float(self.dish_ingredients_table.item(rows[i])['values'][2]) , 
                    'fats': float(self.dish_ingredients_table.item(rows[i])['values'][3]) , 
                    'carbohydrates': float(self.dish_ingredients_table.item(rows[i])['values'][4]) , 
                    'weight': float(self.dish_ingredients_table.item(rows[i])['values'][5])
                    }
                print('Словарь 1 раз =', self.dict_products)

        print('словарь таблица - ', self.dict_products)

        weight = self.full_dish_weight_stepper_input.get()

        self.result_100_gramm_proteins = calculate_dish_proteins(self.dict_products, weight) 
        self.result_100_gramm_fats = calculate_dish_fats(self.dict_products, weight)
        self.result_100_gramm_carbohydrates = calculate_dish_carbohydrates(self.dict_products, weight) 
        self.result_100_gramm_calories = calculate_dish_calories(self.dict_products, weight) 
     
        if os.path.exists('json\saved_dishes.json') == FALSE:
            self.create_json()
        else:
            self.add_to_json()


        print(float(self.full_dish_weight_stepper_input.get()))


        self.results_full_dish_calories_label.config(text = round(self.result_100_gramm_calories * float(self.full_dish_weight_stepper_input.get()) / 100, 2))
        self.results_full_dish_proteins_label.config(text = round(self.result_100_gramm_proteins * float(self.full_dish_weight_stepper_input.get()) / 100,2))
        self.results_full_dish_fats_label.config(text = round(self.result_100_gramm_fats * float(self.full_dish_weight_stepper_input.get()) / 100,2))
        self.results_full_dish_carbohydrates_label.config(text = round(self.result_100_gramm_carbohydrates * float(self.full_dish_weight_stepper_input.get()) / 100, 2))

        self.results_dish_calories_label.config(text = round(self.result_100_gramm_calories, 2))
        self.results_dish_proteins_label.config(text = round(self.result_100_gramm_proteins,2))
        self.results_dish_fats_label.config(text = round(self.result_100_gramm_fats,2))
        self.results_dish_carbohydrates_label.config(text = round(self.result_100_gramm_carbohydrates,2))

        mb.showinfo('Сохранение', 'Блюдо сохранено!')

    #self.full_dish_weight_stepper_input.delete(0, tk.END)

    # Метод создание json файл, для сохранения в него блюда   
    def create_json(self):      
        self.dish = [{
            self.s: {
                'proteins': self.result_100_gramm_proteins,
                'fats': self.result_100_gramm_fats,
                'carbohydrates': self.result_100_gramm_carbohydrates,
                'calories': self.result_100_gramm_calories
            }
        }]

        with open('json\saved_dishes.json', 'w') as file:
            file.write(json.dumps(self.dish, indent=2, ensure_ascii=False))

    # Метод добавление в json файл блюда, которое пользователь хочет сохранить        
    def add_to_json(self):
        self.dish = {
            self.s: {
            'proteins': self.result_100_gramm_proteins,
            'fats': self.result_100_gramm_fats,
            'carbohydrates': self.result_100_gramm_carbohydrates,
            'calories': self.result_100_gramm_calories,
            }
        }
        data = json.load(open('json\saved_dishes.json'))
        data.append(self.dish)
        with open('json\saved_dishes.json', 'w+', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    # Метод вывода рекомендаций на интерфейс
    def get_selected_product_nutrients_data(self, event):
        self.search_line.delete(0, tk.END)
            
        focus = self.service_recommendations_list.focus()
        self.selected_product = self.service_recommendations_list.item(focus)
        self.selected_product_name = self.selected_product['values'][0]
        self.selected_product_nutrients_data = get_product_nutrients_data(self.selected_product_name)
        self.service_recommendations_list.place(x=2000, y=2000)

        self.found_product_name_label.config(text=self.selected_product_name)
        self.found_product_calories_label.config(text=self.selected_product_nutrients_data['calories'])
        self.found_product_proteins_label.config(text=self.selected_product_nutrients_data['proteins'])
        self.found_product_fats_label.config(text=self.selected_product_nutrients_data['fats'])
        self.found_product_carbohydrates_label.config(text=self.selected_product_nutrients_data['carbohydrates'])
    
    # Метод поиска продукта и рекомендаций
    def show_service_recommendations(self):
        if self.search_line.get() == 'Поиск продуктов' or self.search_line.get() == '':
            return
        service_recommendations = get_service_recommendations(self.search_line.get())  # получаем словарь продуктов
        self.service_recommendations_list = ttk.Treeview(self, columns=('1'), height=10, show='')
        self.service_recommendations_list.place(x=49, y=30)
        self.service_recommendations_list.column('1', width=299)
        self.service_recommendations_list.delete(*self.service_recommendations_list.get_children())
        for e in service_recommendations:  # проходимся по всем рекомендациям
            self.service_recommendations_list.insert('', 'end', values=[e]) # выводим рекомендации на интерфейс в виде таблицы
        # по двойному щелчку вызуваем функцию recommendations
        self.service_recommendations_list.bind('<ButtonRelease-1>', self.get_selected_product_nutrients_data)

    # Добавляет продукт и его КБЖУ в таблицу ингредиентов готового блюда
    def add_product(self):
        m1 = self.selected_product_name # название продукт
        m6 = float(self.product_weight_stepper_input.get()) # вес продукта
        m2 = round(float(self.selected_product_nutrients_data['calories']) * m6 / 100, 2)
        m3 = round(float(self.selected_product_nutrients_data['proteins']) * m6 / 100, 2)
        m4 = round(float(self.selected_product_nutrients_data['fats']) * m6 / 100, 2)
        m5 = round(float(self.selected_product_nutrients_data['carbohydrates']) * m6 / 100, 2)

        self.dish_ingredients_table.insert('', 'end', values=(m1, m2, m3, m4, m5, m6))
        self.product_weight_stepper_input.delete(0, tk.END)
    
