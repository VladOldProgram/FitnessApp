from turtle import width
import json
import pyodbc
import tkinter as tk
from tkinter import ttk, Button
from tkinter.ttk import Radiobutton
from PIL import ImageTk
from tkinter import *


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):

        self.image_woman = ImageTk.PhotoImage(file="images\Woman_button.png")
        self.image_men = ImageTk.PhotoImage(file="images\Man_button.png")
        self.image_women_puctires = ImageTk.PhotoImage(
            file="images\Women_pictures.png")
        self.image_men_puctires = ImageTk.PhotoImage(
            file="images\Man_pictures.png")

        def switch_female(event):
            global sex
            sex = False
            woman_pictures = Label(self, image=self.image_women_puctires)
            woman_pictures.place(x=80, y=140)

        def switch_male(event):
            global sex
            sex = True
            man_pictures = Label(self, image=self.image_men_puctires)
            man_pictures.place(x=80, y=140)

        # Женщина
        switch_female_button = Button(self, image=self.image_woman)
        switch_female_button.place(x=300, y=10)
        switch_female_button.bind("<Button-1>", switch_female)
        # Мужчина
        switch_male_button = Button(self, image=self.image_men)
        switch_male_button.place(x=700, y=10)
        switch_male_button.bind("<Button-1>", switch_male)

        #man_pictures = Button(self, image=self.image_men_puctires)
        #man_pictures.place(x=80, y=140)

        activity_level_descriptions = ["""Малоподвижный образ жизни, сидячая работа, отсутствие физических нагрузок.""",
                                       """Интенсивные упражнения не менее 20 минут от 1 до 3 раз в неделю. Например, езда на велосипеде, бег трусцой, баскетбол, плавание, катание на коньках, и т.д. Или если часто приходится ходить в течение длительных периодов времени при отсутствии тренировок.""",
                                       """Уровень физической активности, который несколько повышает частоту сердечных сокращений и оставляет у вас ощущение тепла и легкой одышки, например, усилия, затрачиваемые здоровым человеком при быстрой ходьбе, плавании, езде на велосипеде по ровной поверхности, танцах. Интенсивные упражнения от 30 до 60 минут от 3 до 5 раз в неделю.""",
                                       """Уровень физической активности, который значительно повышает частоту сердечных сокращений и вызывает появление пота, например, усилия, затрачиваемые здоровым человеком при беге, занятиях аэробикой, плавании на дистанцию, быстрой езде на велосипеде, подъеме в гору.  Выполнение интенсивных упражнений не менее 60 минут от 5 до 7 дней в неделю или занятия 2 раза в день. """,
                                       """7 или более часов в неделю очень интенсивных упражнений или интенсивные занятия 2 раза в день. Очень интенсивные и/или очень затратные виды деятельности. Например, профессиональный спортсмен с несколькими тренировками в течение дня или тяжелая физическая работа, такая, как разгрузка угля лопатой или работа на сборочной линии в течение нескольких часов."""]

        def switch_activity_level_description():  # получаем значение от 0 до 4 - уровень физической активности
            print("select = ", selected_activity_level.get())
            activity_level_description_label.config(
                state=NORMAL)  # позволяем ввести текст
            activity_level_description_label.delete(1.0, END)
            sel = selected_activity_level.get()
            if sel == 0:
                activity_level_description_label.insert(
                    1.0, activity_level_descriptions[0])
            else:
                if sel == 1:
                    activity_level_description_label.insert(
                        1.0, activity_level_descriptions[1])
                else:
                    if sel == 2:
                        activity_level_description_label.insert(
                            1.0, activity_level_descriptions[2])
                    else:
                        if sel == 3:
                            activity_level_description_label.insert(
                                1.0, activity_level_descriptions[3])
                        else:
                            if sel == 4:
                                activity_level_description_label.insert(
                                    1.0, activity_level_descriptions[4])

            activity_level_description_label.config(
                state=DISABLED)  # запрет на ввод текста

        def clear_inputs():
            height_text_input.delete("0", END)
            weight_text_input.delete("0", END)
            age_text_input.delete("0", END)

            selected_activity_level.set(0)

            activity_level_description_label.config(
                state=NORMAL)  # позволяем ввести текст
            activity_level_description_label.insert(
                1.0, activity_level_descriptions[0])
            activity_level_description_label.config(
                state=DISABLED)  # запрет на ввод текста

        woman_pictures = Label(self, image=self.image_men_puctires)
        woman_pictures.place(x=80, y=140)
        # Текстовое поле с описанием уровня активности
        activity_level_description_label = Text(
            self, wrap=WORD, font=("Arial", 14))
        activity_level_description_label.place(
            x=630, y=480, height=300, width=400)
        # по умолчанию описание для уровня активности - 0
        activity_level_description_label.insert(
            1.0, activity_level_descriptions[0])
        activity_level_description_label.config(
            state=DISABLED)  # запрет на ввод текста

        print_calories = 0.0

        def calculate_daily_calorie_standart(height, weight, age, activity_level, sex):
            c = float(height.get()) + float(weight.get()) + \
                float(age.get()) + float(activity_level.get())
            calories = 0
            print("sex = ", sex)
            print('Итого: ', c)

            h = float(height.get())
            w = float(weight.get())
            a = int(age.get())
            level = int(activity_level.get())
            print('level: ', level)

            if sex == True:  # Мужчина
                result = 66 + (5 * h) + (13.7 * w) - (6.8 * a)
                if level == 0:
                    calories = 1.2 * result
                if level == 1:
                    calories = 1.375 * result
                if level == 2:
                    calories = 1.55 * result
                if level == 3:
                    calories = 1.7 * result
                if level == 4:
                    calories = 1.9 * result
            else:  # Женщина
                result = 655 + (1.8 * h) + (9.6 * w) - (4.7 * a)
                if level == 0:
                    calories = 1.2 * result
                if level == 1:
                    calories = 1.375 * result
                if level == 2:
                    calories = 1.55 * result
                if level == 3:
                    calories = 1.7 * result
                if level == 4:
                    calories = 1.9 * result

            print(round(calories, 2))
            daily_calories_standart_label.configure(text=round(calories, 2))
            daily_calories_standart_label.pack()
            return round(calories, 2)

        def save_and_calculate_daily_calories_standart():
            js = calculate_daily_calorie_standart(
                height_text_input, weight_text_input, age_text_input, selected_activity_level, sex)
            print('js = ', js)
            data = {
                "daily_calorie_standart": js,
                "sex": sex,
                "height": float(height_text_input.get()),
                "weight": float(weight_text_input.get()),
                "age": int(age_text_input.get()),
                "activity": int(selected_activity_level.get())
            }
            with open('JsonFiles\daily_calories_standart.json ', 'w') as outfile:
                json.dump(data, outfile)

        sex = True
        # вызов функции расчета суточной нормы калорий
        calculate_daily_calories_standart_button = Button(self,
                                                          text='Рассчитать', font=("Arial", 14),
                                                          command=lambda: save_and_calculate_daily_calories_standart())
        calculate_daily_calories_standart_button.place(x=370, y=650)

        clear_inputs_button = Button(
            self, text='Очистить \n поля ввода', font=("Arial", 14), command=clear_inputs)
        clear_inputs_button.place(x=100, y=730)

        labelframe = tk.LabelFrame(
            self, width=270, height=40, text='Суточная норма калорий', font=("Arial", 14), )
        labelframe.place(x=100, y=640)
        daily_calories_standart_label = tk.Label(
            labelframe, text=print_calories, font=("Arial", 14))

        # поля с выводом текста
        label_height = tk.Label(self, text='Рост(см.)', font=("Arial", 12))
        label_height.place(x=325, y=280)
        label_weight = tk.Label(self, text='Вес(кг.)', font=("Arial", 12))
        label_weight.place(x=115, y=580)
        label_age = tk.Label(self, text='Возраст', font=("Arial", 12))
        label_age.place(x=330, y=546)
        label_age = tk.Label(self, text='лет', font=("Arial", 12))
        label_age.place(x=510, y=546)

        def cliker(event):
            if event.char.isnumeric() or event.char == '.':  # надо проверить что точка одна?
                my_label = Label(self, text="что: " + event.char)
                my_label.place(x=500, y=580)
                my_label.pack()

        # поля для ввода параметров
        height_text_input = ttk.Entry(
            self, font=("Arial", 12), width=15)  # рост
        height_text_input.place(x=300, y=260)
        height_text_input.bind("<Key>", cliker)

        weight_text_input = ttk.Entry(
            self, font=("Arial", 12), width=15)  # вес
        weight_text_input.place(x=80, y=550)
        age_text_input = ttk.Entry(self, font=(
            "Arial", 12), width=11)  # возраст
        age_text_input.place(x=400, y=550)

        # берем данные из json
        # with open('CalorieDailyRate.json', 'r') as file:
        #    data = json.load(file)
        # print(data['activity'])
        # брать из json
        activity = [("минимальный", 0),
                    ("низкий", 1),
                    ("умеренный", 2),
                    ("высокий", 3),
                    ("экстремальный", 4)]

        # уровень активности
        selected_activity_level = tk.IntVar()
        selected_activity_level.set(0)  # выбор по умолчанию

        # Уровень физической автивности
        u = tk.Label(self, text="Уровень активности:", font=("Arial", 16))
        u.place(x=743, y=200)
        activity_level_vertical_menu = tk.Radiobutton(self, text=activity[0][0], font=(
            "Arial", 16), indicatoron=0, width=20, padx=60, variable=selected_activity_level, command=switch_activity_level_description, value=0)
        activity_level_vertical_menu.place(x=670, y=240)
        activity_level_vertical_menu = tk.Radiobutton(self, text=activity[1][0], font=(
            "Arial", 16), indicatoron=0, width=20, padx=60, variable=selected_activity_level, command=switch_activity_level_description, value=1)
        activity_level_vertical_menu.place(x=670, y=270)
        activity_level_vertical_menu = tk.Radiobutton(self, text=activity[2][0], font=(
            "Arial", 16), indicatoron=0, width=20, padx=60, variable=selected_activity_level, command=switch_activity_level_description, value=2)
        activity_level_vertical_menu.place(x=670, y=300)
        activity_level_vertical_menu = tk.Radiobutton(self, text=activity[3][0], font=(
            "Arial", 16), indicatoron=0, width=20, padx=60, variable=selected_activity_level, command=switch_activity_level_description, value=3)
        activity_level_vertical_menu.place(x=670, y=330)
        activity_level_vertical_menu = tk.Radiobutton(self, text=activity[4][0], font=(
            "Arial", 16), indicatoron=0, width=20, padx=60, variable=selected_activity_level, command=switch_activity_level_description, value=4)
        activity_level_vertical_menu.place(x=670, y=360)

        # self.button = tk.Button(self, text='Append', command=self.on_append)
        # self.button.pack()

        # self.pack()

        # радиобаттон
        # position = {"padx":600, "pady":6, "anchor":tk.NW}

        # sex = [
        #     {"name": "Женщина", "img": tk.PhotoImage(file="./images/Woman.png")},
        #     {"name": "Мужчина", "img": tk.PhotoImage(file="./images/Man.png")},
        # ]

        # lang = tk.StringVar(value=sex[0]["name"])    # по умолчанию будет выбран элемент с value=woman

        # header = tk.Label(textvariable=lang)
        # header.pack(**position)

        # for l in sex:
        #     btn = ttk.Radiobutton(value=l["name"], text=l["name"], variable=lang, image=l["img"], compound="top")
        #     btn.pack(**position)

        # def change():
        #     if var.get() == 0:
        #         label['bg'] = 'red'
        #     elif var.get() == 1:
        #         label['bg'] = 'green'
        #     elif var.get() == 2:
        #         label['bg'] = 'blue'

        # button = Button(text="Изменить",
        #         command=change)
        # label = Label(width=20, height=10)

        # поля с выводом текста
        # self.radio_woman = ttk.Radiobutton(self, text='Женщина', value=0)
        # self.radio_woman.place(x=100, y=30)
        # self.radio_man = ttk.Radiobutton(self, text='Мужчина', value=0)
        # self.radio_man.place(x=250, y=30)

        # нередактируемое поле с информацией об уровне активности
        #activity_definition = ''
        # print(val)
        # for activ, val in activity:
        #    print(val)
        #    if (val == 0):
        #        activity_definition = 'описание минимальной активности\n далее'
        #labelframe2 = tk.LabelFrame(self, width=300, height=80)
        #labelframe2.place(x=500, y=340)

        #lbl_count2 = tk.Label(labelframe2, text=activity_definition, font=("Arial", 10))
        #lbl_count2.place(x=800, y=600)
        # lbl_count2.pack()

        # нередактируемое поле с информацией о суточной норме калорий

        #labelframe = tk.LabelFrame(self, width=200, height=40, text='Суточная норма калорий')
        #labelframe.place(x=100, y=700)
        #print_calories = '1000'

    # def on_append(self):
    #     print('Hello World!')
