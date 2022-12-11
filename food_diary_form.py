import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *

class Food_diary_form(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # поле для добавления продукта/блюда
        self.frame_foodstruct_add_product = tk.LabelFrame(self, width=430, height=230)
        self.frame_foodstruct_add_product.place(x=30, y=10)
        self.image_loupa = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa = Label(self.frame_foodstruct_add_product, image=self.image_loupa)
        self.loupa.place(x=15, y=37)
        self.label_foodstruct_add_product = tk.Label(self.frame_foodstruct_add_product, text='Добавление продукта/блюда', font=("Arial", 10))
        self.label_foodstruct_add_product.place(x=100, y=10)
        self.label_foodstruct_add_product.focus()

        # поисковая строка продуктов/блюд
        self.foodstruct_search_line = tk.Entry(self.frame_foodstruct_add_product, fg='Grey')
        self.entry_text2 = 'Поиск продуктов/блюд'
        self.foodstruct_search_line.insert(0, self.entry_text2)
        self.foodstruct_search_line.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.foodstruct_search_line))
        self.foodstruct_search_line.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.foodstruct_search_line, self.entry_text2))
        self.foodstruct_search_line.place(x=40, y=40, width=300)


        self.searchbtn = tk.Button(self.frame_foodstruct_add_product, text="Найти", font=("Arial", 10), command = self.search)
        self.searchbtn.place(x=360, y=35)

        self.product_weight_stepper_input = ttk.Entry(self.frame_foodstruct_add_product, font=("Arial", 10), width=10)
        self.product_weight_stepper_input.place(x=320, y=105)

        self.found_product_name_label = Label(self.frame_foodstruct_add_product, text='')
        self.found_product_name_label.place(x=20, y=103)

        self.found_product_calories_label = Label(self.frame_foodstruct_add_product, text='')
        self.found_product_calories_label.place(x=1500, y=1000)

        self.found_product_proteins_label = Label(self.frame_foodstruct_add_product, text='')
        self.found_product_proteins_label.place(x=1500, y=1050)

        self.found_product_fats_label = Label(self.frame_foodstruct_add_product, text='')
        self.found_product_fats_label.place(x=1500, y=2000)

        self.found_product_carbohydrates_label = Label(self.frame_foodstruct_add_product, text='')
        self.found_product_carbohydrates_label.place(x=1500, y=2500)


        self.add_product_button = tk.Button(self.frame_foodstruct_add_product, text="Добавить в дневник питания", font=("Arial", 10), command = self.add_product)
        self.add_product_button.place(x=210, y=170)

        # поле для добавления сохраненного блюда
        self.frame_foodstruct_add_dish = tk.LabelFrame(self, width=430, height=540)
        self.frame_foodstruct_add_dish.place(x=30, y=260)
        self.image_loupa2 = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa2 = Label(self.frame_foodstruct_add_dish, image=self.image_loupa2)
        self.loupa2.place(x=15, y=37)
        self.label_foodstruct_add_dish = tk.Label(self.frame_foodstruct_add_dish, text='Добавление сохраненного блюда', font=("Arial", 10))
        self.label_foodstruct_add_dish.place(x=100, y=10)

        # поисковая строка сохраненных блюд
        self.saved_dishes_search_line  = tk.Entry(self.frame_foodstruct_add_dish, fg='Grey')
        self.entry_text3 = 'Поиск сохраненных блюд'
        self.saved_dishes_search_line.insert(0, self.entry_text3)
        self.saved_dishes_search_line.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.saved_dishes_search_line))
        self.saved_dishes_search_line.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.saved_dishes_search_line , self.entry_text3))
        self.saved_dishes_search_line.place(x=40, y=40, width=300)

        self.searchbtn2 = tk.Button(self.frame_foodstruct_add_dish, text="Найти", font=("Arial", 10))
        self.searchbtn2.place(x=360, y=35)

        # таблица сохраненных блюд
        self.frame_dish = ttk.Frame(self.frame_foodstruct_add_dish)
        self.frame_dish.place(x=15, y=80)

        self.tree2 = ttk.Treeview(self.frame_dish, columns=('txtDishName', 'txtDishProteins', 'txtDishFats', 'txtDishCarbohydrates', 'txtDishCalories'), height=14, show='headings')

        self.tree2.column('txtDishName', width=50, anchor=tk.CENTER)
        self.tree2.column('txtDishProteins', width=80, anchor=tk.CENTER)
        self.tree2.column('txtDishFats', width=70, anchor=tk.CENTER)
        self.tree2.column('txtDishCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree2.column('txtDishCalories', width=90, anchor=tk.CENTER)

        self.tree2.heading('txtDishName', text='Блюдо')
        self.tree2.heading('txtDishProteins', text='Белки, гр.')
        self.tree2.heading('txtDishFats', text='Жиры, гр.')
        self.tree2.heading('txtDishCarbohydrates', text='Углеводы, гр.')
        self.tree2.heading('txtDishCalories', text='Калории, ккал.')

        self.scroll = tk.Scrollbar(self.frame_dish, command=self.tree2.yview)  # Линейка прокрутки для списка
        self.scroll.place(x=800, y=50, height=235)
        self.tree2.config(yscrollcommand=self.scroll.set)  
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree2.pack()

        self.dish_weight_stepper_label = tk.Label(self.frame_foodstruct_add_dish, text='Введите вес блюда в граммах', font=("Arial", 10))
        self.dish_weight_stepper_label.place(x=10, y=430)
        self.dish_weight_stepper_input = ttk.Entry(self.frame_foodstruct_add_dish)
        self.dish_weight_stepper_input.place(x=320, y=430, width=60)

        self.delete_saved_dish_button = tk.Button(self.frame_foodstruct_add_dish, text='Удалить сохраненное\n блюдо из списка', command=self.delete_saved_dish)
        self.delete_saved_dish_button.place(x=10, y=475)

        self.add_saved_dish_button = tk.Button(self.frame_foodstruct_add_dish, text='Добавить в дневник\n питания')
        self.add_saved_dish_button.place(x=295, y=475)

        # таблица дневника питания
        self.label_txtMealWeight = tk.Label(self, text='Дневник питания', font='Arial 15 bold')
        self.label_txtMealWeight.place(x=710, y=0)

        self.frame_diary = ttk.Frame(self)
        self.frame_diary.place(x=500, y=40)

        self.tree = ttk.Treeview(self.frame_diary, columns=('txtProductName', 'txtProductCalories', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductWeight'), height=34, show='headings')

        self.tree.column('txtProductName', width=120, anchor=tk.CENTER)
        self.tree.column('txtProductCalories', width=95, anchor=tk.CENTER)
        self.tree.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductWeight', width=80, anchor=tk.CENTER)

        self.tree.heading('txtProductName', text='Продукт/блюдо')
        self.tree.heading('txtProductCalories', text='Калории, ккал.')
        self.tree.heading('txtProductProteins', text='Белки, гр.')
        self.tree.heading('txtProductFats', text='Жиры, гр.')
        self.tree.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.tree.heading('txtProductWeight', text='Вес, гр.')

        self.scroll = tk.Scrollbar(self.frame_diary, command=self.tree.yview)  # Линейка прокрутки для списка
        self.scroll.place(x=1560, y=50, height=695)
        self.tree.config(yscrollcommand=self.scroll.set)  
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.pack()

        self.result_calories_label = tk.Label(self, text='Суммарное количество калорий', font=("Arial", 10))
        self.result_calories_label.place(x=500, y=750)

        self.btn_add2 = tk.Button(self, text='Удалить из дневника питания', command = self.delete_by)
        self.btn_add2.place(x=900, y=770)

        self.btn_add3 = tk.Button(self, text='Очистить дневник питания', command = self.delete_all)
        self.btn_add3.place(x=720, y=770)


    def search(self):
        get = get_service_recommendations(
            'stroka')  # получаем словарь продуктов
        self.table2 = ttk.Treeview(self, columns=('1'), show="")
        self.table2.place(x=28, y=50)
        self.table2.column("1", width=400)
        self.table2.delete(*self.table2.get_children())
        for x in get.keys():  # проходимся по всем рекомендациям
            self.table2.insert('', 'end', values=[x])
        # по двойному щелчку вызываем функцию rekomend
        self.table2.bind("<Double-Button-1>", self.rekomend)

    def rekomend(self, event):
        print("Нажала")
        cur_row = self.table2.focus()
        self.vals = self.table2.item(cur_row, "values")
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

    def focus_in_entry_box(self, self3):
        if self3['fg'] == 'Grey':
            self3['fg'] = 'Black'
            self3.delete(0, tk.END)

    def focus_out_entry_box(self, self1, self_text):
        if self1['fg'] == 'Black' and len(self1.get()) == 0:
            self1.delete(0, tk.END)
            self1['fg'] = 'Grey'
            self1.insert(0, self_text)


    def add_product(self):
        m1 = str(self.vals[0])
        m2 = self.product_data["calories"]
        m3 = self.product_data["proteins"]
        m4 = self.product_data["fats"]
        m5 = self.product_data["carbohydrates"]
        m6 = float(self.product_weight_stepper_input.get()) # вес
        
        self.product_data["calories"] = round(float(self.product_data["calories"]) * m6 / 100, 2)
        self.product_data["proteins"] = round(float(self.product_data["proteins"]) * m6 / 100, 2)
        self.product_data["fats"] = round(float(self.product_data["fats"]) * m6 / 100, 2)
        self.product_data["carbohydrates"] = round(float(self.product_data["carbohydrates"]) * m6 / 100, 2)

        self.tree.insert('', 'end', values=(m1, self.product_data["calories"], self.product_data["proteins"], self.product_data["fats"], self.product_data["carbohydrates"], m6))
        
        self.product_weight_stepper_input.delete(0, tk.END)

    def delete_all(self):
        if self.tree == '':
            mb.showinfo('Удаление', 'Дневник питания пуст')
        else:
            answer = mb.askyesno(
                message='Вы уверены, что хотите удалить все продукты/блюда из дневника?')
                
            if answer:
                self.tree.delete(*self.tree.get_children())
                mb.showinfo(message='Список продуктов очищен')

    def delete_by(self):
        if not self.tree.selection():
            mb.showinfo('Удаление', 'Данные для удаления не найдены')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить данные  о продукте/блюде?')
            if answer:
                item = self.tree.selection()[0]
                self.tree.delete(item)
                self.tree.config(height=34)
                mb.showinfo(message='Данные удалены')

    def delete_saved_dish(self):
        if not self.tree.selection():
            mb.showinfo('Удаление', 'Данные для удаления не найдены')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить данные  о продукте/блюде?')
            if answer:
                item = self.tree.selection()[0]
                self.tree.delete(item)
                self.tree.config(height=14)
                mb.showinfo(message='Данные удалены')



