import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        parent = parent
        self.init_ui()

    def init_ui(self): # Хранение и инициализация всех объектов графического интерфейса

        label_txtMealWeight = tk.Label(self, text='КБЖУ готового блюда', font='Arial 15 bold')
        label_txtMealWeight.place(x=710, y=0)

        clear_table_button = tk.Button(self, text='Очистить таблицу', font=("Arial", 10), command=self.delete_all)
        clear_table_button.place(x=750, y=770)
        delete_line_button = tk.Button(self, text='Удалить запись из таблицы', font=("Arial", 10))
        delete_line_button.place(x=900, y=770)
        save_dish_button = tk.Button(self, text='Сохранить\n блюдо', font=("Arial", 10))
        save_dish_button.place(x=400, y=750)
        searchbtn = tk.Button(self, text="Найти", font=("Arial", 10))
        searchbtn.place(x=380, y=10)
        calculate_dish_nutrients_button = tk.Button(self, text='Рассчитать КБЖУ готового блюда', font=("Arial", 10))
        calculate_dish_nutrients_button.place(x=120, y=400)


        # поисковая строка
        entry_txtNameProduct = tk.Entry(self, fg='Grey')
        entry_text2 = 'Поиск продуктов'
        entry_txtNameProduct.insert(0, entry_text2)
        entry_txtNameProduct.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_txtNameProduct))
        entry_txtNameProduct.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_txtNameProduct, entry_text2))
        entry_txtNameProduct.place(x=50, y=10, width=300)

        # поле для информации о продукте
        frame_info_product = tk.LabelFrame(self, width=430, height=290)
        frame_info_product.place(x=30, y=50)
        label_info_product = tk.Label(frame_info_product, text='Информация о продукте в 100 граммах', font=("Arial", 10))
        label_info_product.place(x=90, y=10)
        # product_weight_stepper_input = tk.Spinbox(frame_info_product, font=("Arial", 10), width=10, from_=0.0, to=100.0)
        # product_weight_stepper_input.place(x=140, y=55)
        product_weight_stepper_input = ttk.Entry(frame_info_product, font=("Arial", 10), width=10)
        product_weight_stepper_input.place(x=160, y=55)
        add_product_button = tk.Button(frame_info_product, text="Добавить в список", font=("Arial", 10))
        add_product_button.place(x=270, y=50)
        found_product_calories = tk.Label(frame_info_product, text='Калорийность', font=("Arial", 10))
        found_product_calories.place(x=20, y=100)
        found_product_proteins = tk.Label(frame_info_product, text='Белки', font=("Arial", 10))
        found_product_proteins.place(x=20, y=150)
        found_product_fats = tk.Label(frame_info_product, text='Жиры', font=("Arial", 10))
        found_product_fats.place(x=20, y=200)
        found_product_carbohydrates = tk.Label(frame_info_product, text='Углеводы', font=("Arial", 10))
        found_product_carbohydrates.place(x=20, y=250)

        full_dish_weight_stepper_label = tk.Label(self, text='Введите вес готового блюда в граммах', font=("Arial", 10))
        full_dish_weight_stepper_label.place(x=50, y=360)
        full_dish_weight_stepper_input = ttk.Entry(self)
        full_dish_weight_stepper_input.place(x=300, y=360, width=60)

        # поле для информации о КБЖУ готового блюда
        frame_info_dish = tk.LabelFrame(self, width=430, height=290)
        frame_info_dish.place(x=30, y=450)
        label_info_dish = tk.Label(frame_info_dish, text='КБЖУ готового блюда', font=("Arial", 10))
        label_info_dish.place(x=140, y=10)
        results_dish_calories = tk.Label(frame_info_dish, text='Итог для', font=("Arial", 10))
        results_dish_calories.place(x=130, y=60)
        # results_dish_calories = tk.Label(frame_info_dish, text=, font=("Arial", 10))
        # results_dish_calories.place(x=150, y=60)
        results_dish_calories = tk.Label(frame_info_dish, text='гр.', font=("Arial", 10))
        results_dish_calories.place(x=250, y=60)
        results_dish_calories = tk.Label(frame_info_dish, text='Итог для 100 гр.', font=("Arial", 10))
        results_dish_calories.place(x=300, y=60)
        results_dish_calories = tk.Label(frame_info_dish, text='Калорийность', font=("Arial", 10))
        results_dish_calories.place(x=20, y=100)
        results_dish_proteins = tk.Label(frame_info_dish, text='Белки', font=("Arial", 10))
        results_dish_proteins.place(x=20, y=150)
        results_dish_fats = tk.Label(frame_info_dish, text='Жиры', font=("Arial", 10))
        results_dish_fats.place(x=20, y=200)
        results_dish_carbohydrates = tk.Label(frame_info_dish, text='Углеводы', font=("Arial", 10))
        results_dish_carbohydrates.place(x=20, y=250)
        
        # создание placeholder...
        def focus_out_entry_box(self, self_text):
            if self['fg'] == 'Black' and len(self.get()) == 0:
                self.delete(0, tk.END)
                self['fg'] = 'Grey'
                self.insert(0, self_text)

        def focus_in_entry_box(self):
            if self['fg'] == 'Grey':
                self['fg'] = 'Black'
                self.delete(0, tk.END)

        # сохранение готового блюда
        entry_txtNameMeal = tk.Entry(self, fg='Grey')
        entry_text = 'Введите название блюда'
        entry_txtNameMeal.insert(0, entry_text)
        entry_txtNameMeal.bind("<FocusIn>", lambda args: focus_in_entry_box(entry_txtNameMeal))
        entry_txtNameMeal.bind("<FocusOut>", lambda args: focus_out_entry_box(entry_txtNameMeal, entry_text))
        entry_txtNameMeal.place(x=50, y=760, width=300)

        # таблица добавленных продуктов
        frame = ttk.Frame(self)
        frame.place(x=500, y=40)

        tree = ttk.Treeview(frame, columns=('txtProductName', 'txtProductWeight', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductCalories'), height=34, show='headings')

        tree.column('txtProductName', width=150, anchor=tk.CENTER)
        tree.column('txtProductWeight', width=80, anchor=tk.CENTER)
        tree.column('txtProductProteins', width=80, anchor=tk.CENTER)
        tree.column('txtProductFats', width=80, anchor=tk.CENTER)
        tree.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        tree.column('txtProductCalories', width=95, anchor=tk.CENTER)

        tree.heading('txtProductName', text='Продукт')
        tree.heading('txtProductWeight', text='Вес, гр.')
        tree.heading('txtProductProteins', text='Белки, гр.')
        tree.heading('txtProductFats', text='Жиры, гр.')
        tree.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        tree.heading('txtProductCalories', text='Калории, ккал.')

        tree.pack()
         
        scroll = tk.Scrollbar(command=tree.yview)  # Линейка прокрутки для списка
        scroll.place(x=1560, y=50, height=695)
        tree.config(yscrollcommand=scroll.set)     

    def delete_all(self):
        answer = mb.askyesno(message='Вы уверены, что хотите очистить таблицу?')

        if answer:
            #удалить все значения для конкретного блюда из json!
            self.db.delete_all()
            mb.showinfo(message='Таблица очищена')

    # def delete_by(self):

    #     # берем данные по нажатию на строку
    #     # удалить конкретный продукт из конкретного блюда из json!
    #     # db.search_by(search_dict[combobox_search.get()], enter_search.get())
    #     # fetch = db.c.fetchall()

    #     if not fetch:
    #         mb.showinfo('Удаление', 'Данные для удаления не найдены')
    #     else:
    #         answer = mb.askyesno(message='Вы уверены, что хотите удалить эти данные?')
    #         if answer:
    #             # удаляем по столбцам
    #             # db.delete_by(search_dict[combobox_search.get()], enter_search.get())
    #             mb.showinfo(message='Данные удалены')
    #             db.view_table()

    def on_select(self, val):
        sender = val.self
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)
