import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        parent = parent
        self.init_ui()

    def init_ui(self):  # Хранение и инициализация всех объектов графического интерфейса

        def search():

            def rekomend(event):
                print("Нажала")
                cur_row = table2.focus()
                vals = table2.item(cur_row, "values")
                print("Продукт = ", str(vals[0]))
                product_data = get_product_nutrients_data(str(vals[0]))
                print(product_data)
                # print(get.get(vals[0])) # ссылка на выбранный продукт
                table2.place(x=2000, y=2000)

                found_product_name_label.config(text=vals[0])
                found_product_calories_label.config(
                    text=product_data['calories'])
                found_product_proteins_label.config(
                    text=product_data['proteins'])
                found_product_fats_label.config(text=product_data['fats'])
                found_product_carbohydrates_label.config(
                    text=product_data['carbohydrates'])

            get = get_service_recommendations(
                'stroka')  # получаем словарь продуктов
            table2 = ttk.Treeview(self, columns=('1'), show="")
            table2.place(x=28, y=50)
            table2.column("1", width=400)
            table2.delete(*table2.get_children())
            for x in get.keys():  # проходимся по всем рекомендациям
                table2.insert('', 'end', values=[x])
            # по двойному щелчку вызываем функцию rekomend
            table2.bind("<Double-Button-1>", rekomend)


        

        self.image_loupa = ImageTk.PhotoImage(
            file="assets\images\loupa_small.png")
        self.loupa = Label(self, image=self.image_loupa)
        self.loupa.place(x=26, y=6)

        label_txtMealWeight = tk.Label(
            self, text='КБЖУ готового блюда', font='Arial 15 bold')
        label_txtMealWeight.place(x=710, y=0)

        save_dish_button = tk.Button(
            self, text='Сохранить\n блюдо', font=("Arial", 10))
        save_dish_button.place(x=400, y=750)
        searchbtn = tk.Button(self, text="Найти", font=(
            "Arial", 10), command=search)
        searchbtn.place(x=380, y=10)

        # поисковая строка
        entry_txtNameProduct = tk.Entry(self, fg='Grey')
        entry_text2 = 'Поиск продуктов'
        entry_txtNameProduct.insert(0, entry_text2)
        entry_txtNameProduct.bind(
            "<FocusIn>", lambda args: focus_in_entry_box(entry_txtNameProduct))
        entry_txtNameProduct.bind("<FocusOut>", lambda args: focus_out_entry_box(
            entry_txtNameProduct, entry_text2))
        entry_txtNameProduct.place(x=50, y=10, width=300)

        # поле для информации о продукте
        frame_info_product = tk.LabelFrame(self, width=430, height=290)
        frame_info_product.place(x=30, y=50)
        label_info_product = tk.Label(
            frame_info_product, text='Информация о продукте в 100 граммах', font=("Arial", 10))
        label_info_product.place(x=90, y=10)
        # product_weight_stepper_input = tk.Spinbox(frame_info_product, font=("Arial", 10), width=10, from_=0.0, to=100.0)
        # product_weight_stepper_input.place(x=140, y=55)
        product_weight_stepper_input = ttk.Entry(
            frame_info_product, font=("Arial", 10), width=10)
        product_weight_stepper_input.place(x=160, y=55)

        found_product_name_label = Label(frame_info_product, text='')
        found_product_name_label.place(x=20, y=53)

        found_product_calories_label = Label(frame_info_product, text='')
        found_product_calories_label.place(x=150, y=100)

        found_product_proteins_label = Label(frame_info_product, text='')
        found_product_proteins_label.place(x=150, y=150)

        found_product_fats_label = Label(frame_info_product, text='')
        found_product_fats_label.place(x=150, y=200)

        found_product_carbohydrates_label = Label(frame_info_product, text='')
        found_product_carbohydrates_label.place(x=150, y=250)

        # поле для информации о КБЖУ готового блюда
        frame_info_dish = tk.LabelFrame(self, width=430, height=290)
        frame_info_dish.place(x=30, y=450)

        results_dish_calories11 = tk.Label(frame_info_dish, text='', font=("Arial", 10))
        results_dish_calories11.place(x=200, y=60)

        def save_dish():
            f = full_dish_weight_stepper_input.get()
            print(f)
            results_dish_calories11.config(text=f)

        def add_product():
            #found_product_name_label.cget("text"), found_product_calories_label.cget("text"), found_product_proteins_label.cget("text"), found_product_fats_label.cget("text"), found_product_carbohydrates_label.cget("text"), product_weight_stepper_input.get()
            m1=found_product_name_label.cget("text")
            m2=found_product_calories_label.cget("text")
            m3=found_product_proteins_label.cget("text")
            m4=found_product_fats_label.cget("text") 
            m5=found_product_carbohydrates_label.cget("text")
            m6=product_weight_stepper_input.get()

            print(m1)
            print(m2)
            print(m3)
            print(m4)
            print(m5)
            print(m6)

            l = [m1,m2,m3,m4,m5,m6]
            print("лист ", l)

            table.insert('', 'end', values=(m1, m2,m3, m4, m5, m6))


        calculate_dish_nutrients_button = tk.Button(self, text='Рассчитать КБЖУ готового блюда', font=("Arial", 10), command=save_dish)
        calculate_dish_nutrients_button.place(x=120, y=400)
        add_product_button = tk.Button(frame_info_product, text="Добавить в список", font=("Arial", 10), command=add_product)
        
        
        add_product_button.place(x=270, y=50)
        found_product_calories = tk.Label(
            frame_info_product, text='Калорийность', font=("Arial", 10))
        found_product_calories.place(x=20, y=100)
        found_product_proteins = tk.Label(
            frame_info_product, text='Белки', font=("Arial", 10))
        found_product_proteins.place(x=20, y=150)
        found_product_fats = tk.Label(
            frame_info_product, text='Жиры', font=("Arial", 10))
        found_product_fats.place(x=20, y=200)
        found_product_carbohydrates = tk.Label(
            frame_info_product, text='Углеводы', font=("Arial", 10))
        found_product_carbohydrates.place(x=20, y=250)

        full_dish_weight_stepper_label = tk.Label(
            self, text='Введите вес готового блюда в граммах', font=("Arial", 10))
        full_dish_weight_stepper_label.place(x=50, y=360)
        full_dish_weight_stepper_input = ttk.Entry(self)
        full_dish_weight_stepper_input.place(x=300, y=360, width=60)

        label_info_dish = tk.Label(
            frame_info_dish, text='КБЖУ готового блюда', font=("Arial", 10))
        label_info_dish.place(x=140, y=10)
        results_dish_calories = tk.Label(
            frame_info_dish, text='Итог для', font=("Arial", 10))
        results_dish_calories.place(x=130, y=60)
        results_dish_calories = tk.Label(
            frame_info_dish, text='гр.', font=("Arial", 10))
        results_dish_calories.place(x=250, y=60)
        results_dish_calories = tk.Label(
            frame_info_dish, text='Итог для 100 гр.', font=("Arial", 10))
        results_dish_calories.place(x=300, y=60)
        results_dish_calories = tk.Label(
            frame_info_dish, text='Калорийность', font=("Arial", 10))
        results_dish_calories.place(x=20, y=100)
        results_dish_proteins = tk.Label(
            frame_info_dish, text='Белки', font=("Arial", 10))
        results_dish_proteins.place(x=20, y=150)
        results_dish_fats = tk.Label(
            frame_info_dish, text='Жиры', font=("Arial", 10))
        results_dish_fats.place(x=20, y=200)
        results_dish_carbohydrates = tk.Label(
            frame_info_dish, text='Углеводы', font=("Arial", 10))
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
        entry_txtNameMeal.bind(
            "<FocusIn>", lambda args: focus_in_entry_box(entry_txtNameMeal))
        entry_txtNameMeal.bind("<FocusOut>", lambda args: focus_out_entry_box(
            entry_txtNameMeal, entry_text))
        entry_txtNameMeal.place(x=50, y=760, width=300)

        # таблица добавленных продуктов
        frame = ttk.Frame(self)
        frame.place(x=500, y=40)


        def delete_all():
            if not table.selection():
                mb.showinfo('Удаление', 'Список продуктов пуст')
            else:
                answer = mb.askyesno(
                    message='Вы уверены, что хотите удалить все продукты из списка?')
                    
                if answer:
                    table.delete(*table.get_children())
                    mb.showinfo(message='Список продуктов очищен')

        def delete_by():
            if not table.selection():
                mb.showinfo('Удаление', 'Данные для удаления не найдены')
            else:
                answer = mb.askyesno(message='Вы уверены, что хотите удалить данные о продукте?')
                if answer:
                    item = table.selection()[0]
                    table.delete(item)
                    table.config(height=34)
                    mb.showinfo(message='Данные удалены')


        table = ttk.Treeview(self, columns=('txtProductName', 'txtProductCalories', 'txtProductProteins',
                             'txtProductFats', 'txtProductCarbohydrates', 'txtProductWeight'), height=34, show='headings')

        table.column('txtProductName', width=150, anchor=tk.CENTER)
        table.column('txtProductCalories', width=95, anchor=tk.CENTER)
        table.column('txtProductProteins', width=80, anchor=tk.CENTER)
        table.column('txtProductFats', width=80, anchor=tk.CENTER)
        table.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        table.column('txtProductWeight', width=80, anchor=tk.CENTER)

        table.heading('txtProductName', text='Продукт')
        table.heading('txtProductCalories', text='Калории, ккал.')
        table.heading('txtProductProteins', text='Белки, гр.')
        table.heading('txtProductFats', text='Жиры, гр.')
        table.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        table.heading('txtProductWeight', text='Вес, гр.')

        # Линейка прокрутки для списка
        scroll = tk.Scrollbar(frame, command=table.yview)
        scroll.place(x=1560, y=50, height=695)
        table.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        table.place(x=500, y=40)

        clear_table_button = tk.Button(self, text='Очистить таблицу', font=(
            "Arial", 10), command=delete_all)
        clear_table_button.place(x=750, y=770)
        delete_line_button = tk.Button(
            self, text='Удалить запись из таблицы', font=("Arial", 10), command=delete_by)
        delete_line_button.place(x=900, y=770)

