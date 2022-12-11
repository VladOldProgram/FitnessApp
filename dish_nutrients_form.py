import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *


class Dish_nutrients_form(tk.Frame):
    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

        self.image_loupa = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa = Label(self, image=self.image_loupa)
        self.loupa.place(x=26, y=6)

        self.label_txtMealWeight = tk.Label(self, text='КБЖУ готового блюда', font='Arial 15 bold')
        self.label_txtMealWeight.place(x=710, y=0)

        self.save_dish_button = tk.Button(self, text='Сохранить\n блюдо', font=("Arial", 10))
        self.save_dish_button.place(x=400, y=750)
        self.searchbtn = tk.Button(self, text="Найти", font=("Arial", 10), command=self.search)
        self.searchbtn.place(x=380, y=10)
        self.calculate_dish_nutrients_button = tk.Button(self, text='Рассчитать КБЖУ готового блюда', font=("Arial", 10), command=self.save_dish)
        self.calculate_dish_nutrients_button.place(x=120, y=400)

        # поисковая строка
        self.entry_txtNameProduct = tk.Entry(self, fg='Grey')
        self.entry_text2 = 'Поиск продуктов'
        self.entry_txtNameProduct.insert(0, self.entry_text2)
        self.entry_txtNameProduct.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.entry_txtNameProduct))
        self.entry_txtNameProduct.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.entry_txtNameProduct, self.entry_text2))
        self.entry_txtNameProduct.place(x=50, y=10, width=300)

        # поле для информации о продукте
        self.frame_info_product = tk.LabelFrame(self, width=430, height=290)
        self.frame_info_product.place(x=30, y=50)
        self.label_info_product = tk.Label(self.frame_info_product, text='Информация о продукте в 100 граммах', font=("Arial", 10))
        self.label_info_product.place(x=90, y=10)
        # product_weight_stepper_input = tk.Spinbox(frame_info_product, font=("Arial", 10), width=10, from_=0.0, to=100.0)
        # product_weight_stepper_input.place(x=140, y=55)
        self.product_weight_stepper_input = ttk.Entry(self.frame_info_product, font=("Arial", 10), width=10)
        self.product_weight_stepper_input.place(x=160, y=55)

        self.found_product_name_label = Label(self.frame_info_product, text='')
        self.found_product_name_label.place(x=20, y=53)

        self.found_product_calories_label = Label(self.frame_info_product, text='')
        self.found_product_calories_label.place(x=150, y=100)

        self.found_product_proteins_label = Label(self.frame_info_product, text='')
        self.found_product_proteins_label.place(x=150, y=150)

        self.found_product_fats_label = Label(self.frame_info_product, text='')
        self.found_product_fats_label.place(x=150, y=200)

        self.found_product_carbohydrates_label = Label(self.frame_info_product, text='')
        self.found_product_carbohydrates_label.place(x=150, y=250)

        
        self.add_product_button = tk.Button(self.frame_info_product, text="Добавить в список", font=(
            "Arial", 10), command=self.add_product)

        self.add_product_button.place(x=270, y=50)
        self.found_product_calories = tk.Label(self.frame_info_product, text='Калорийность', font=("Arial", 10))
        self.found_product_calories.place(x=20, y=100)
        self.found_product_proteins = tk.Label(self.frame_info_product, text='Белки', font=("Arial", 10))
        self.found_product_proteins.place(x=20, y=150)
        self.found_product_fats = tk.Label(self.frame_info_product, text='Жиры', font=("Arial", 10))
        self.found_product_fats.place(x=20, y=200)
        self.found_product_carbohydrates = tk.Label(self.frame_info_product, text='Углеводы', font=("Arial", 10))
        self.found_product_carbohydrates.place(x=20, y=250)

        self.full_dish_weight_stepper_label = tk.Label(self, text='Введите вес готового блюда в граммах', font=("Arial", 10))
        self.full_dish_weight_stepper_label.place(x=50, y=360)
        self.full_dish_weight_stepper_input = ttk.Entry(self)
        self.full_dish_weight_stepper_input.place(x=300, y=360, width=60)

        # поле для информации о КБЖУ готового блюда
        self.frame_info_dish = tk.LabelFrame(self, width=430, height=290)
        self.frame_info_dish.place(x=30, y=450)
        self.label_info_dish = tk.Label(self.frame_info_dish, text='КБЖУ готового блюда', font=("Arial", 10))
        self.label_info_dish.place(x=140, y=10)
        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Итог для', font=("Arial", 10))
        self.results_dish_calories.place(x=130, y=60)
        # results_dish_calories = tk.Label(frame_info_dish, text=, font=("Arial", 10))
        # results_dish_calories.place(x=150, y=60)
        self.results_dish_calories = tk.Label(self.frame_info_dish, text='гр.', font=("Arial", 10))
        self.results_dish_calories.place(x=250, y=60)
        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Итог для 100 гр.', font=("Arial", 10))
        self.results_dish_calories.place(x=300, y=60)
        self.results_dish_calories = tk.Label(self.frame_info_dish, text='Калорийность', font=("Arial", 10))
        self.results_dish_calories.place(x=20, y=100)
        self.results_dish_proteins = tk.Label(self.frame_info_dish, text='Белки', font=("Arial", 10))
        self.results_dish_proteins.place(x=20, y=150)
        self.results_dish_fats = tk.Label(self.frame_info_dish, text='Жиры', font=("Arial", 10))
        self.results_dish_fats.place(x=20, y=200)
        self.results_dish_carbohydrates = tk.Label(self.frame_info_dish, text='Углеводы', font=("Arial", 10))
        self.results_dish_carbohydrates.place(x=20, y=250)


        # сохранение готового блюда
        self.entry_txtNameMeal = tk.Entry(self, fg='Grey')
        self.entry_text = 'Введите название блюда'
        self.entry_txtNameMeal.insert(0, self.entry_text)
        self.entry_txtNameMeal.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.entry_txtNameMeal))
        self.entry_txtNameMeal.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.entry_txtNameMeal, self.entry_text))
        self.entry_txtNameMeal.place(x=50, y=760, width=300)

        # таблица добавленных продуктов
        self.frame = ttk.Frame(self)
        self.frame.place(x=500, y=40)

        self.table = ttk.Treeview(self.frame, columns=('txtProductName', 'txtProductCalories', 'txtProductProteins',
                             'txtProductFats', 'txtProductCarbohydrates', 'txtProductWeight'), height=34, show='headings')

        self.table.column('txtProductName', width=150, anchor=tk.CENTER)
        self.table.column('txtProductCalories', width=95, anchor=tk.CENTER)
        self.table.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.table.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.table.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.table.column('txtProductWeight', width=80, anchor=tk.CENTER)

        self.table.heading('txtProductName', text='Продукт')
        self.table.heading('txtProductCalories', text='Калории, ккал.')
        self.table.heading('txtProductProteins', text='Белки, гр.')
        self.table.heading('txtProductFats', text='Жиры, гр.')
        self.table.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.table.heading('txtProductWeight', text='Вес, гр.')

        # Линейка прокрутки для списка
        self.scroll = tk.Scrollbar(self.frame, command=self.table.yview)
        self.scroll.place(x=1560, y=50, height=695)
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.table.pack()

        self.clear_table_button = tk.Button(self, text='Очистить таблицу', font=("Arial", 10), command=self.delete_all)
        self.clear_table_button.place(x=750, y=770)
        self.delete_line_button = tk.Button(self, text='Удалить запись из таблицы', font=("Arial", 10), command = self.delete_by)
        self.delete_line_button.place(x=900, y=770)

        self.results_dish_calories11 = tk.Label(self.frame_info_dish, text='', font=("Arial", 10))
        self.results_dish_calories11.place(x=200, y=60)


    def delete_all(self):
        if self.table == '':
                mb.showinfo('Удаление', 'Список продуктов пуст')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить все продукты из списка?')
            if answer:
                self.table.delete(*self.table.get_children())
                mb.showinfo(message='Список продуктов очищен')


    def delete_by(self):
            if not self.table.selection():
                mb.showinfo('Удаление', 'Данные для удаления не найдены')
            else:
                answer = mb.askyesno(message='Вы уверены, что хотите удалить данные о продукте?')
                if answer:
                    item = self.table.selection()[0]
                    self.table.delete(item)
                    self.table.config(height=34)
                    mb.showinfo(message='Данные удалены')

    # создание placeholder...

    def focus_out_entry_box(self, self1, self_text):
        if self1['fg'] == 'Black' and len(self1.get()) == 0:
            self1.delete(0, tk.END)
            self1['fg'] = 'Grey'
            self1.insert(0, self_text)

    def focus_in_entry_box(self, self3):
        if self3['fg'] == 'Grey':
            self3['fg'] = 'Black'
            self3.delete(0, tk.END)

    def save_dish(self):
        self.results_dish_calories11.config(text=self.full_dish_weight_stepper_input.get()) 

        s = self.entry_txtNameMeal.get()

        print(s)





    '''
            data = {
            'daily_calories_standart': daily_calories_standart,
            'sex': self.sex,
            'height': float(self.height_entry.get()),
            'weight': float(self.weight_entry.get()),
            'age': int(self.age_entry.get()),
            'activity_level': int(self.selected_activity_level.get())
        }
        with open('json\daily_calories_standart.json', 'w') as outfile:
            json.dump(data, outfile)
    '''




    def rekomend(self, event):
        print("Нажала")
        self.cur_row = self.table2.focus()
        self.vals = self.table2.item(self.cur_row, "values")
        print("Продукт = ", str(self.vals[0]))
        self.product_data = get_product_nutrients_data(str(self.vals[0]))
        print(self.product_data)
        # print(get.get(vals[0])) # ссылка на выбранный продукт
        self.table2.place(x=2000, y=2000)

        self.found_product_name_label.config(text=self.vals[0])
        self.found_product_calories_label.config(text=self.product_data['calories'])
        self.found_product_proteins_label.config(text=self.product_data['proteins'])
        self.found_product_fats_label.config(text=self.product_data['fats'])
        self.found_product_carbohydrates_label.config(text=self.product_data['carbohydrates'])
    
    def search(self):
        self.get = get_service_recommendations('stroka')  # получаем словарь продуктов
        self.table2 = ttk.Treeview(self, columns=('1'), show="")
        self.table2.place(x=28, y=50)
        self.table2.column("1", width=400)
        self.table2.delete(*self.table2.get_children())
        for x in self.get.keys():  # проходимся по всем рекомендациям
            self.table2.insert('', 'end', values=[x])
        # по двойному щелчку вызуваем функцию rekomend
        self.table2.bind("<Double-Button-1>", self.rekomend)


    def add_product(self):
        #found_product_name_label.cget("text"), found_product_calories_label.cget("text"), found_product_proteins_label.cget("text"), found_product_fats_label.cget("text"), found_product_carbohydrates_label.cget("text"), product_weight_stepper_input.get()
        #m1 = self.found_product_name_label.cget("text")  # продукт
        #m2 = float(self.found_product_calories_label.cget("text")) # калории
        #m3 = float(self.found_product_proteins_label.cget("text")) # белки
        #m4 = float(self.found_product_fats_label.cget("text")) # жиры
        #m5 = float(self.found_product_carbohydrates_label.cget("text")) # углеводы
        #m6 = float(self.product_weight_stepper_input.get()) # вес

        m1 = str(self.vals[0])
        m2 = self.product_data["calories"]
        m3 = self.product_data["proteins"]
        m4 = self.product_data["fats"]
        m5 = self.product_data["carbohydrates"]
        m6 = float(self.product_weight_stepper_input.get()) # вес
        
        self.product_data["calories"] = float(self.product_data["calories"]) * m6 / 100
        self.product_data["proteins"] = float(self.product_data["proteins"]) * m6 / 100
        self.product_data["fats"] = float(self.product_data["fats"]) * m6 / 100
        self.product_data["carbohydrates"] = float(self.product_data["carbohydrates"]) * m6 / 100

        self.table.insert('', 'end', values=(m1, self.product_data["calories"], self.product_data["proteins"], self.product_data["fats"], self.product_data["carbohydrates"], m6))

    
    
    '''
            data = {
            'daily_calories_standart': daily_calories_standart,
            'sex': self.sex,
            'height': float(self.height_entry.get()),
            'weight': float(self.weight_entry.get()),
            'age': int(self.age_entry.get()),
            'activity_level': int(self.selected_activity_level.get())
        }
        with open('json\daily_calories_standart.json', 'w') as outfile:
            json.dump(data, outfile)
    '''
