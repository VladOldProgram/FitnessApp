import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *
from foodstruct import *
from calculate import *
import json
import os.path
from json import JSONDecodeError


class Food_diary_form(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #self.json_create()

        # поле для добавления продукта/блюда
        self.frame_foodstruct_add_saved_dish_to_diary = tk.LabelFrame(self, width=430, height=230)
        self.frame_foodstruct_add_saved_dish_to_diary.place(x=30, y=10)
        self.image_loupa = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa = Label(self.frame_foodstruct_add_saved_dish_to_diary, image=self.image_loupa)
        self.loupa.place(x=15, y=37)
        self.label_foodstruct_add_saved_dish_to_diary = tk.Label(self.frame_foodstruct_add_saved_dish_to_diary, text='Добавление продукта/блюда', font=("Arial", 10))
        self.label_foodstruct_add_saved_dish_to_diary.place(x=100, y=10)
        self.label_foodstruct_add_saved_dish_to_diary.focus()

        # поисковая строка продуктов/блюд
        self.foodstruct_show_service_recommendations_line = tk.Entry(self.frame_foodstruct_add_saved_dish_to_diary, fg='Grey')
        self.entry_text2 = 'Поиск продуктов/блюд'
        self.foodstruct_show_service_recommendations_line.insert(0, self.entry_text2)
        self.foodstruct_show_service_recommendations_line.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.foodstruct_show_service_recommendations_line))
        self.foodstruct_show_service_recommendations_line.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.foodstruct_show_service_recommendations_line, self.entry_text2))
        self.foodstruct_show_service_recommendations_line.place(x=40, y=40, width=300)


        self.show_service_recommendationsbtn = tk.Button(self.frame_foodstruct_add_saved_dish_to_diary, text="Найти", font=("Arial", 10), command = self.show_service_recommendations)
        self.show_service_recommendationsbtn.place(x=360, y=35)

        self.foodstruct_product_weight_stepper_input = ttk.Entry(self.frame_foodstruct_add_saved_dish_to_diary, font=("Arial", 10), width=10, validate='key')
        self.foodstruct_product_weight_stepper_input['validatecommand'] = (self.foodstruct_product_weight_stepper_input.register(self.value_is_float), '%P', '%d')
        self.foodstruct_product_weight_stepper_input.place(x=320, y=105)

        self.found_product_name_label = Label(self.frame_foodstruct_add_saved_dish_to_diary, text='')
        self.found_product_name_label.place(x=20, y=103)

        self.found_product_calories_label = Label(self.frame_foodstruct_add_saved_dish_to_diary, text='')
        self.found_product_calories_label.place(x=1500, y=1000)

        self.found_product_proteins_label = Label(self.frame_foodstruct_add_saved_dish_to_diary, text='')
        self.found_product_proteins_label.place(x=1500, y=1050)

        self.found_product_fats_label = Label(self.frame_foodstruct_add_saved_dish_to_diary, text='')
        self.found_product_fats_label.place(x=1500, y=2000)

        self.found_product_carbohydrates_label = Label(self.frame_foodstruct_add_saved_dish_to_diary, text='')
        self.found_product_carbohydrates_label.place(x=1500, y=2500)


        self.foodstruct_add_saved_dish_to_diary_button = tk.Button(self.frame_foodstruct_add_saved_dish_to_diary, text="Добавить в дневник питания", font=("Arial", 10), command = self.add_product)
        self.foodstruct_add_saved_dish_to_diary_button.place(x=210, y=170)

        # поле для добавления сохраненного блюда
        self.frame_foodstruct_add_dish = tk.LabelFrame(self, width=430, height=540)
        self.frame_foodstruct_add_dish.place(x=30, y=260)
        self.image_loupa2 = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa2 = Label(self.frame_foodstruct_add_dish, image=self.image_loupa2)
        self.loupa2.place(x=15, y=37)
        self.label_foodstruct_add_dish = tk.Label(self.frame_foodstruct_add_dish, text='Добавление сохраненного блюда', font=("Arial", 10))
        self.label_foodstruct_add_dish.place(x=100, y=10)

        # поисковая строка сохраненных блюд
        self.saved_dishes_show_service_recommendations_line  = tk.Entry(self.frame_foodstruct_add_dish, fg='Grey')
        self.entry_text3 = 'Поиск сохраненных блюд'
        self.saved_dishes_show_service_recommendations_line.insert(0, self.entry_text3)
        self.saved_dishes_show_service_recommendations_line.bind("<FocusIn>", lambda args: self.focus_in_entry_box(self.saved_dishes_show_service_recommendations_line))
        self.saved_dishes_show_service_recommendations_line.bind("<FocusOut>", lambda args: self.focus_out_entry_box(self.saved_dishes_show_service_recommendations_line , self.entry_text3))
        self.saved_dishes_show_service_recommendations_line.place(x=40, y=40, width=300)

        self.show_service_recommendationsbtn2 = tk.Button(self.frame_foodstruct_add_dish, text="Найти", font=("Arial", 10))
        self.show_service_recommendationsbtn2.place(x=360, y=35)

        # таблица сохраненных блюд
        self.frame_dish = ttk.Frame(self.frame_foodstruct_add_dish)
        self.frame_dish.place(x=15, y=80)

        self.saved_dishes_table = ttk.Treeview(self.frame_dish, columns=('txtDishName', 'txtDishProteins', 'txtDishFats', 'txtDishCarbohydrates', 'txtDishCalories'), height=14, show='headings')

        self.saved_dishes_table.column('txtDishName', width=130, anchor=tk.CENTER)
        self.saved_dishes_table.column('txtDishProteins', width=50, anchor=tk.CENTER)
        self.saved_dishes_table.column('txtDishFats', width=50, anchor=tk.CENTER)
        self.saved_dishes_table.column('txtDishCarbohydrates', width=65, anchor=tk.CENTER)
        self.saved_dishes_table.column('txtDishCalories', width=65, anchor=tk.CENTER)

        self.saved_dishes_table.heading('txtDishName', text ='Блюдо')
        self.saved_dishes_table.heading('txtDishProteins', text ='Белки')
        self.saved_dishes_table.heading('txtDishFats', text ='Жиры')
        self.saved_dishes_table.heading('txtDishCarbohydrates', text ='Углеводы')
        self.saved_dishes_table.heading('txtDishCalories', text ='Калории')

        self.scroll = tk.Scrollbar(self.frame_dish, command=self.saved_dishes_table.yview)  # Линейка прокрутки для списка
        self.scroll.place(x=800, y=50, height=235)
        self.saved_dishes_table.config(yscrollcommand=self.scroll.set)  
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.saved_dishes_table.pack()

        self.dish_weight_stepper_label = tk.Label(self.frame_foodstruct_add_dish, text='Введите вес блюда в граммах', font=("Arial", 10))
        self.dish_weight_stepper_label.place(x=10, y=430)
        self.saved_dish_weight_stepper_input = ttk.Entry(self.frame_foodstruct_add_dish, validate='key')
        self.saved_dish_weight_stepper_input['validatecommand'] = (self.saved_dish_weight_stepper_input.register(self.value_is_float), '%P', '%d')
        self.saved_dish_weight_stepper_input.place(x=320, y=430, width=60)

        self.delete_saved_dish_button = tk.Button(self.frame_foodstruct_add_dish, text='Удалить сохраненное\n блюдо из списка', command=self.delete_saved_dish)
        self.delete_saved_dish_button.place(x=10, y=475)

        self.add_saved_dish_button = tk.Button(self.frame_foodstruct_add_dish, text='Добавить в дневник\n питания', command=self.add_saved_dish_to_diary)
        self.add_saved_dish_button.place(x=295, y=475)

        # таблица дневника питания
        self.label_txtMealWeight = tk.Label(self, text='Дневник питания', font='Arial 15 bold')
        self.label_txtMealWeight.place(x=710, y=0)

        self.frame_diary = ttk.Frame(self)
        self.frame_diary.place(x=500, y=40)

        self.diary_table = ttk.Treeview(self.frame_diary, columns=('txtProductName', 'txtProductCalories', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductWeight'), height=34, show='headings')

        self.diary_table.column('txtProductName', width=120, anchor=tk.CENTER)
        self.diary_table.column('txtProductCalories', width=95, anchor=tk.CENTER)
        self.diary_table.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.diary_table.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.diary_table.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.diary_table.column('txtProductWeight', width=80, anchor=tk.CENTER)

        self.diary_table.heading('txtProductName', text='Продукт/блюдо')
        self.diary_table.heading('txtProductCalories', text='Калории')
        self.diary_table.heading('txtProductProteins', text='Белки, гр.')
        self.diary_table.heading('txtProductFats', text='Жиры, гр.')
        self.diary_table.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.diary_table.heading('txtProductWeight', text='Вес, гр.')

        self.scroll = tk.Scrollbar(self.frame_diary, command=self.diary_table.yview)  # Линейка прокрутки для списка
        self.scroll.place(x=1560, y=50, height=695)
        self.diary_table.config(yscrollcommand=self.scroll.set)  
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.diary_table.pack()

        self.result_calories_label = tk.Label(self, text='Суммарное количество калорий', font=("Arial", 10))
        self.result_calories_label.place(x=500, y=750)
        self.result_calories_label2 = tk.Label(self, text='', font=("Arial", 10))
        self.result_calories_label2.place(x=510, y=770)
        self.result_calories_label3 = tk.Label(self, text='из', font=("Arial", 10))
        self.result_calories_label3.place(x=600, y=770)
        self.result_calories_label4 = tk.Label(self, text ='', font=("Arial", 10))
        self.result_calories_label4.place(x=620, y=770)
        self.result_calories_label4.config(text=self.get_daily_calories_standart())
    
        self.delete_from_diary_button = tk.Button(self, text='Удалить из дневника питания', command=self.delete_from_diary)
        self.delete_from_diary_button.place(x=900, y=770)

        self.clear_diary_button = tk.Button(self, text='Очистить дневник питания', command=self.clear_diary)
        self.clear_diary_button.place(x=720, y=770)

        self.update_table_dish()


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
        

    def save_diary_to_json(self):
        self.dict_products = {}
        self.dict_products_zapacnoy = {}
        
        rows = self.diary_table.get_children()

        for i in range(len(rows)):
            #print("Продукт = ", self.diary_table.item(rows[i])["values"][0])

            self.name_products_or_dishes = self.diary_table.item(rows[i])["values"][0]
  
            m2 = float(self.diary_table.item(rows[i])["values"][1]) #К
            m3 = float(self.diary_table.item(rows[i])["values"][2]) #Б
            m4 = float(self.diary_table.item(rows[i])["values"][3]) #Ж
            m5 = float(self.diary_table.item(rows[i])["values"][4]) #У
            m6 = float(self.diary_table.item(rows[i])["values"][5]) #вес



            # если продукт из таблицы содержаться в словаре
            if self.diary_table.item(rows[i])["values"][0] in self.dict_products.keys():
                # создаем запасной словарь
                #print("Сделали запасной")
                self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]] = {
                    "calories": float(self.dict_products[self.diary_table.item(rows[i])["values"][0]]["calories"]),
                    "proteins": float(self.dict_products[self.diary_table.item(rows[i])["values"][0]]["proteins"]),
                    "fats": float(self.dict_products[self.diary_table.item(rows[i])["values"][0]]["fats"]),
                    "carbohydrates": float(self.dict_products[self.diary_table.item(rows[i])["values"][0]]["carbohydrates"]),
                    "weight": float(self.dict_products[self.diary_table.item(rows[i])["values"][0]]["weight"])
                    }
                    
                self.dict_products[self.diary_table.item(rows[i])["values"][0]] = {
                    "calories": round(float(self.diary_table.item(rows[i])["values"][1]) + float(self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]]["calories"]), 2), 
                    "proteins": round(float(self.diary_table.item(rows[i])["values"][2]) + float(self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]]["proteins"]), 2), 
                    "fats": round(float(self.diary_table.item(rows[i])["values"][3]) + float(self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]]["fats"]), 2), 
                    "carbohydrates": round(float(self.diary_table.item(rows[i])["values"][4]) + float(self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]]["carbohydrates"]), 2), 
                    "weight": round(float(self.diary_table.item(rows[i])["values"][5]) + float(self.dict_products_zapacnoy[self.diary_table.item(rows[i])["values"][0]]["weight"]), 2)
                    } 

                #print("ЗАПАСНОЙ СЛОВАРЬ", self.dict_products_zapacnoy)
                self.dict_products_zapacnoy = {}


            else: # иначе добавляем в словарь
                #print("Добавили 1 раз")
                self.dict_products[self.diary_table.item(rows[i])["values"][0]] = {
                    "calories": round(float(self.diary_table.item(rows[i])["values"][1]), 2) , 
                    "proteins": round(float(self.diary_table.item(rows[i])["values"][2]), 2) , 
                    "fats": round(float(self.diary_table.item(rows[i])["values"][3]), 2) , 
                    "carbohydrates": round(float(self.diary_table.item(rows[i])["values"][4]), 2) , 
                    "weight": round(float(self.diary_table.item(rows[i])["values"][5]), 2)
                    }
            # print("Словарь 1 раз =", self.dict_products)


        print(self.dict_products)
        print(self.dict_products[self.name_products_or_dishes]['proteins'])



        #self.foodstruct_product_weight_stepper_input.delete(0, tk.END)
        #if os.path.exists('json\diary.json') == FALSE:
        self.create_json()
       #else:
           # self.add_to_json()


    # Метод создание json файл, для сохранения в него блюда
    def create_json(self):
        self.dish = [{
            self.name_products_or_dishes: {
                'weight': self.dict_products[self.name_products_or_dishes]['weight'],
                'proteins': self.dict_products[self.name_products_or_dishes]['proteins'],
                'fats': self.dict_products[self.name_products_or_dishes]['fats'],
                'carbohydrates': self.dict_products[self.name_products_or_dishes]['carbohydrates'],
                'calories': self.dict_products[self.name_products_or_dishes]['calories']
            }
        }]

        with open('json\diary.json', 'w+', encoding='utf-8') as file:
            file.write(json.dumps(self.dish, indent=2, ensure_ascii=True))



    def add_saved_dish_to_diary(self):

        if not self.saved_dishes_table.selection():
            mb.showinfo('Выберите из списка сохраненных блюд')
        else:
            #rows = self.saved_dishes_table.get_children()
            q = self.saved_dishes_table.selection()
            current_line = self.saved_dishes_table.item(q)["values"]

            m6 = float(self.saved_dish_weight_stepper_input.get()) # вес

            m1 = current_line[0] # навание блюда
            m2 = round(float(current_line[1]) * m6 / 100, 2) #Б
            m3 = round(float(current_line[2]) * m6 / 100, 2) #Ж
            m4 = round(float(current_line[3]) * m6 / 100, 2) #У
            m5 = round(float(current_line[4]) * m6 / 100, 2) #К

            self.diary_table.insert('', 'end', values=(m1, m5, m2, m3, m4, m6))
            self.update_label_sum_calories()
            self.save_diary_to_json()
            self.foodstruct_product_weight_stepper_input.delete(0, tk.END)          

    def update_table_dish(self):
        try:
            with open('json\saved_dishes.json', 'r', encoding='utf-8') as f:
                try:
                    result = json.load(f)
                    #print(type(result))
                    for i in range(len(result)):
                        #print(result[i])
                        #print(result[i].keys())
                        name_dish = list(result[i].keys())
                        name = name_dish[0] # название блюда
                        proteins = result[i][name_dish[0]]["proteins"]
                        fats = result[i][name_dish[0]]["fats"]
                        carbohydrates = result[i][name_dish[0]]["carbohydrates"]
                        calories = result[i][name_dish[0]]["calories"]
                        self.saved_dishes_table.insert('', 'end', values=(name, proteins, fats, carbohydrates, calories))
                except JSONDecodeError:
                    return 
        except FileNotFoundError:
            return

    def show_service_recommendations(self):
        get = get_service_recommendations(
            'stroka')  # получаем словарь продуктов
        self.table2 = ttk.Treeview(self, columns=('1'), height=8, show="")
        self.table2.place(x=30, y=80)
        self.table2.column("1", width=425)
        self.table2.delete(*self.table2.get_children())
        for x in get.keys():  # проходимся по всем рекомендациям
            self.table2.insert('', 'end', values=[x])
        # по двойному щелчку вызываем функцию show_input_hints
        self.table2.bind("<Double-Button-1>", self.show_input_hints)

    def show_input_hints(self, event):
        #print("Нажала")
        cur_row = self.table2.focus()
        self.vals = self.table2.item(cur_row, "values")
        #print("Продукт = ", str(self.vals[0]))
        self.product_data = get_product_nutrients_data(str(self.vals[0]))
        #print(self.product_data)
        # print(get.get(vals[0])) # ссылка на выбранный продукт
        self.table2.place(x=20000, y=20000)

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


    def update_label_sum_calories(self):
        sum_calories = 0.0
        rows = self.diary_table.get_children()
        for i in range(len(rows)):
            sum_calories += float(self.diary_table.item(rows[i])['values'][1])
        self.result_calories_label2.config(text = sum_calories)



    def clear_diary(self):
        if self.diary_table == '':
            mb.showinfo('Удаление', 'Дневник питания пуст')
        else:
            answer = mb.askyesno(
                message='Вы уверены, что хотите удалить все продукты/блюда из дневника?')
                
            if answer:
                self.result_calories_label2.config(text = '')
                self.diary_table.delete(*self.diary_table.get_children())
                mb.showinfo(message='Список продуктов очищен')

    def delete_from_diary(self):
        if not self.diary_table.selection():
            mb.showinfo('Удаление', 'Данные для удаления не найдены')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить данные  о продукте/блюде?')
            if answer:
                item = self.diary_table.selection()[0]
                self.diary_table.delete(item)
                self.diary_table.config(height=34)
                mb.showinfo(message='Данные удалены')

    def delete_saved_dish(self):
        if not self.saved_dishes_table.selection():
            mb.showinfo('Удаление', 'Данные для удаления не найдены')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить данные  о продукте/блюде?')
            if answer:
                item = self.saved_dishes_table.selection()[0]
                try:
                    with open('json\saved_dishes.json') as f:
                        try:
                            result = json.load(f)
                            q = self.saved_dishes_table.selection()
                            
                            stroka = str(q[0])[1:]

                            number_10 = int(self.convert_base(stroka, from_base=16, to_base=10)) - 1

                            result.pop(number_10)
                            self.saved_dishes_table.delete(item)
                            self.saved_dishes_table.config(height=14)
                            mb.showinfo(message='Данные удалены')
                            with open("json\saved_dishes.json", "w") as file:
                                json.dump(result, file, ensure_ascii=True)
                        except JSONDecodeError:
                            return 
                except FileNotFoundError:
                    return

    def convert_base(self, num, to_base=10, from_base=10):
        # first convert to decimal number
        if isinstance(num, str):
            n = int(num, from_base)
        else:
            n = int(num)
        # now convert decimal to 'to_base' base
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if n < to_base:
            return alphabet[n]
        else:
            return self.convert_base(n // to_base, to_base) + alphabet[n % to_base]



    def get_daily_calories_standart(self):
        try:
            with open('json\daily_calories_standart.json', 'r') as my_file:
                f = my_file.read()
                try:
                    return json.loads(f)['daily_calories_standart']
                except JSONDecodeError:
                    return 0.0
        except FileNotFoundError:
            return 0.0



        # Метод вывода рекомендаций на интерфейс
    def get_selected_product_nutrients_data(self, event):
        self.foodstruct_show_service_recommendations_line.delete(0, tk.END)
            
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
        if self.foodstruct_show_service_recommendations_line.get() == 'Поиск продуктов' or self.foodstruct_show_service_recommendations_line.get() == '':
            return
        service_recommendations = get_service_recommendations(self.foodstruct_show_service_recommendations_line.get())  # получаем словарь продуктов
        self.service_recommendations_list = ttk.Treeview(self, columns=('1'), height=10, show='')
        self.service_recommendations_list.place(x=72, y=71)
        self.service_recommendations_list.column('1', width=298)
        self.service_recommendations_list.delete(*self.service_recommendations_list.get_children())
        for e in service_recommendations:  # проходимся по всем рекомендациям
            self.service_recommendations_list.insert('', 'end', values=[e]) # выводим рекомендации на интерфейс в виде таблицы
        # по двойному щелчку вызуваем функцию recommendations
        self.service_recommendations_list.bind('<ButtonRelease-1>', self.get_selected_product_nutrients_data)

    
    # Добавляет продукт и его КБЖУ в таблицу ингредиентов готового блюда
    def add_product(self):

        m1 = self.selected_product_name # название продукт выбранного (нового для добавления)
        rows = self.diary_table.get_children()
        not_product = False

        if  len(rows) != 0:

            for i in range(len(rows)):
                self.name_products_or_dishes = self.diary_table.item(rows[i])["values"][0] # Продукты из таблицы
                
                if m1 == self.name_products_or_dishes:

                    m6 = round(float(self.foodstruct_product_weight_stepper_input.get()), 2) +  round(float(self.diary_table.item(rows[i])["values"][5]), 2)
                    m2 = round(float(self.selected_product_nutrients_data['calories']) * m6 / 100, 2) + round(float(self.diary_table.item(rows[i])["values"][1]), 2)
                    m3 = round(float(self.selected_product_nutrients_data['proteins']) * m6 / 100, 2) + round(float(self.diary_table.item(rows[i])["values"][2]), 2)
                    m4 = round(float(self.selected_product_nutrients_data['fats']) * m6 / 100, 2) + round(float(self.diary_table.item(rows[i])["values"][3]), 2)
                    m5 = round(float(self.selected_product_nutrients_data['carbohydrates']) * m6 / 100, 2) + round(float(self.diary_table.item(rows[i])["values"][4]), 2)

                    self.diary_table.set(rows[i], 1, round(m2, 2))
                    self.diary_table.set(rows[i], 2, round(m3, 2))
                    self.diary_table.set(rows[i], 3, round(m4, 2))
                    self.diary_table.set(rows[i], 4, round(m5, 2))
                    self.diary_table.set(rows[i], 5, round(m6, 2))

                    #self.diary_table.insert('', 'end', values=(m1, m2, m3, m4, m5, m6))
                    not_product = True
                    break

        if not_product == False:
            m6 = float(self.foodstruct_product_weight_stepper_input.get()) # вес продукта
            m2 = float(self.selected_product_nutrients_data['calories']) * m6 / 100
            m3 = float(self.selected_product_nutrients_data['proteins']) * m6 / 100
            m4 = float(self.selected_product_nutrients_data['fats']) * m6 / 100
            m5 = float(self.selected_product_nutrients_data['carbohydrates']) * m6 / 100

            self.diary_table.insert('', 'end', values=(m1, round(m2, 2), round(m3, 2), round(m4, 2), round(m5, 2), round(m6, 2)))


        self.update_label_sum_calories()
        self.save_diary_to_json()
        self.foodstruct_product_weight_stepper_input.delete(0, tk.END)


