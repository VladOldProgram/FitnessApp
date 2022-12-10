import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):

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



        # поле для добавления продукта/блюда
        frame_foodstruct_add_product = tk.LabelFrame(self, width=430, height=230)
        frame_foodstruct_add_product.place(x=30, y=10)
        self.image_loupa = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa = Label(frame_foodstruct_add_product, image=self.image_loupa)
        self.loupa.place(x=15, y=37)
        label_foodstruct_add_product = tk.Label(frame_foodstruct_add_product, text='Добавление продукта/блюда', font=("Arial", 10))
        label_foodstruct_add_product.place(x=100, y=10)

        # поисковая строка продуктов/блюд
        foodstruct_search_line = tk.Entry(frame_foodstruct_add_product, fg='Grey')
        entry_text2 = 'Поиск продуктов/блюд'
        foodstruct_search_line.insert(0, entry_text2)
        foodstruct_search_line.bind("<FocusIn>", lambda args: focus_in_entry_box(foodstruct_search_line))
        foodstruct_search_line.bind("<FocusOut>", lambda args: focus_out_entry_box(foodstruct_search_line, entry_text2))
        foodstruct_search_line.place(x=40, y=40, width=300)

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

        searchbtn = tk.Button(frame_foodstruct_add_product, text="Найти", font=("Arial", 10), command=search)
        searchbtn.place(x=360, y=35)

        product_weight_stepper_input = ttk.Entry(frame_foodstruct_add_product, font=("Arial", 10), width=10)
        product_weight_stepper_input.place(x=320, y=105)

        found_product_name_label = Label(frame_foodstruct_add_product, text='')
        found_product_name_label.place(x=20, y=103)

        found_product_calories_label = Label(frame_foodstruct_add_product, text='')
        found_product_calories_label.place(x=1500, y=1000)

        found_product_proteins_label = Label(frame_foodstruct_add_product, text='')
        found_product_proteins_label.place(x=1500, y=1050)

        found_product_fats_label = Label(frame_foodstruct_add_product, text='')
        found_product_fats_label.place(x=1500, y=2000)

        found_product_carbohydrates_label = Label(frame_foodstruct_add_product, text='')
        found_product_carbohydrates_label.place(x=1500, y=2500)


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

            self.tree.insert('', 'end', values=(m1, m2,m3, m4, m5, m6))

        add_product_button = tk.Button(frame_foodstruct_add_product, text="Добавить в дневник питания", font=("Arial", 10), command=add_product)
        add_product_button.place(x=210, y=170)

        # поле для добавления сохраненного блюда
        frame_foodstruct_add_dish = tk.LabelFrame(self, width=430, height=540)
        frame_foodstruct_add_dish.place(x=30, y=260)
        self.image_loupa2 = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa2 = Label(frame_foodstruct_add_dish, image=self.image_loupa2)
        self.loupa2.place(x=15, y=37)
        label_foodstruct_add_dish = tk.Label(frame_foodstruct_add_dish, text='Добавление сохраненного блюда', font=("Arial", 10))
        label_foodstruct_add_dish.place(x=100, y=10)

        # поисковая строка сохраненных блюд
        saved_dishes_search_line  = tk.Entry(frame_foodstruct_add_dish, fg='Grey')
        entry_text3 = 'Поиск сохраненных блюд'
        saved_dishes_search_line.insert(0, entry_text2)
        saved_dishes_search_line.bind("<FocusIn>", lambda args: focus_in_entry_box(saved_dishes_search_line ))
        saved_dishes_search_line.bind("<FocusOut>", lambda args: focus_out_entry_box(saved_dishes_search_line , entry_text3))
        saved_dishes_search_line.place(x=40, y=40, width=300)

        searchbtn2 = tk.Button(frame_foodstruct_add_dish, text="Найти", font=("Arial", 10))
        searchbtn2.place(x=360, y=35)

        # таблица сохраненных блюд
        frame_dish = ttk.Frame(frame_foodstruct_add_dish)
        frame_dish.place(x=15, y=80)

        self.tree2 = ttk.Treeview(frame_dish, columns=('txtDishName', 'txtDishProteins', 'txtDishFats', 'txtDishCarbohydrates', 'txtDishCalories'), height=14, show='headings')

        self.tree2.column('txtDishName', width=70, anchor=tk.CENTER)
        self.tree2.column('txtDishProteins', width=90, anchor=tk.CENTER)
        self.tree2.column('txtDishFats', width=70, anchor=tk.CENTER)
        self.tree2.column('txtDishCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree2.column('txtDishCalories', width=70, anchor=tk.CENTER)

        self.tree2.heading('txtDishName', text='Блюдо')
        self.tree2.heading('txtDishProteins', text='Белки, гр.')
        self.tree2.heading('txtDishFats', text='Жиры, гр.')
        self.tree2.heading('txtDishCarbohydrates', text='Углеводы, гр.')
        self.tree2.heading('txtDishCalories', text='Калории, ккал.')

        scroll = tk.Scrollbar(frame_dish, command=self.tree2.yview)  # Линейка прокрутки для списка
        scroll.place(x=800, y=50, height=235)
        self.tree2.config(yscrollcommand=scroll.set)  
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree2.pack()

        dish_weight_stepper_label = tk.Label(frame_foodstruct_add_dish, text='Введите вес блюда в граммах', font=("Arial", 10))
        dish_weight_stepper_label.place(x=10, y=430)
        dish_weight_stepper_input = ttk.Entry(frame_foodstruct_add_dish)
        dish_weight_stepper_input.place(x=320, y=430, width=60)

        btn_add3 = tk.Button(frame_foodstruct_add_dish, text='Удалить сохраненное\n блюдо из списка')
        btn_add3.place(x=10, y=475)

        btn_add4 = tk.Button(frame_foodstruct_add_dish, text='Добавить в дневник\n питания')
        btn_add4.place(x=295, y=475)

        # таблица дневника питания
        label_txtMealWeight = tk.Label(self, text='Дневник питания', font='Arial 15 bold')
        label_txtMealWeight.place(x=710, y=0)

        frame_diary = ttk.Frame(self)
        frame_diary.place(x=500, y=40)

        def delete_all():
            if not self.tree.selection():
                mb.showinfo('Удаление', 'Дневник питания пуст')
            else:
                answer = mb.askyesno(
                    message='Вы уверены, что хотите удалить все продукты/блюда из дневника?')
                    
                if answer:
                    self.tree.delete(*self.tree.get_children())
                    mb.showinfo(message='Список продуктов очищен')

        def delete_by():
            if not self.tree.selection():
                mb.showinfo('Удаление', 'Данные для удаления не найдены')
            else:
                answer = mb.askyesno(message='Вы уверены, что хотите удалить данные  о продукте/блюде?')
                if answer:
                    item = self.tree.selection()[0]
                    self.tree.delete(item)
                    self.tree.config(height=34)
                    mb.showinfo(message='Данные удалены')

        self.tree = ttk.Treeview(frame_diary, columns=('txtProductName', 'txtProductCalories', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductWeight'), height=34, show='headings')

        self.tree.column('txtProductName', width=150, anchor=tk.CENTER)
        self.tree.column('txtProductCalories', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductWeight', width=95, anchor=tk.CENTER)

        self.tree.heading('txtProductName', text='Продукт/блюдо')
        self.tree.heading('txtProductCalories', text='Калории, ккал.')
        self.tree.heading('txtProductProteins', text='Белки, гр.')
        self.tree.heading('txtProductFats', text='Жиры, гр.')
        self.tree.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.tree.heading('txtProductWeight', text='Вес, гр.')

        scroll = tk.Scrollbar(frame_diary, command=self.tree.yview)  # Линейка прокрутки для списка
        scroll.place(x=1560, y=50, height=695)
        self.tree.config(yscrollcommand=scroll.set)  
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.pack()

        result_calories_label = tk.Label(self, text='Суммарное количество калорий', font=("Arial", 10))
        result_calories_label.place(x=500, y=750)

        btn_add2 = tk.Button(self, text='Удалить из дневника питания', command=delete_by)
        btn_add2.place(x=900, y=770)

        btn_add3 = tk.Button(self, text='Очистить дневник питания', command=delete_all)
        btn_add3.place(x=720, y=770)
