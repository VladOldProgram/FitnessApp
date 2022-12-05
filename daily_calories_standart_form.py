from turtle import width
import json
import pyodbc
import tkinter as tk
from tkinter import ttk, Button
from tkinter.ttk import Radiobutton
from PIL import ImageTk
from tkinter import *
from calculate import * 

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):

        self.image_woman = ImageTk.PhotoImage(file="assets\images\\female_button.png")
        self.image_men = ImageTk.PhotoImage(file="assets\images\male_button.png")
        self.image_women_puctires = ImageTk.PhotoImage(
            file="assets\images\\female.png")
        self.image_men_puctires = ImageTk.PhotoImage(
            file="assets\images\male.png")

        sex = True

        def switch_female(event):
            print("Девушка")
            global sex
            sex = False
            woman_pictures = Label(self, image=self.image_women_puctires)
            woman_pictures.place(x=80, y=140)
            print('sex = ', sex)
            return sex

        def switch_male(event):
            print("Парень")
            global sex
            sex = True
            man_pictures = Label(self, image=self.image_men_puctires)
            man_pictures.place(x=80, y=140)
            print('sex = ', sex)
            return sex
        
            
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
                activity_level_description_label.insert(1.0, activity_level_descriptions[0])
            elif sel == 1:
                activity_level_description_label.insert(1.0, activity_level_descriptions[1])
            elif sel == 2:
                activity_level_description_label.insert(1.0, activity_level_descriptions[2])
            elif sel == 3:
                activity_level_description_label.insert(1.0, activity_level_descriptions[3])
            elif sel == 4:
                activity_level_description_label.insert(1.0, activity_level_descriptions[4])

            activity_level_description_label.config(state=DISABLED)  # запрет на ввод текста

        def clear_inputs():
            height_text_input.delete("0", END)
            weight_text_input.delete("0", END)
            age_text_input.delete("0", END)

            selected_activity_level.set(0)

            activity_level_description_label.config(
                state=NORMAL)  # позволяем ввести текст
            activity_level_description_label.delete(1.0, END)
            activity_level_description_label.insert(
                1.0, activity_level_descriptions[0])
            activity_level_description_label.config(
                state=DISABLED)  # запрет на ввод текста

        man_pictures = Label(self, image=self.image_men_puctires)
        man_pictures.place(x=80, y=140)
        

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

        def calculate_and_save_daily_calories_standart():
            if selected_activity_level.get() == 0:
                activity_level_coefficient = 1.2
            if selected_activity_level.get() == 1:
                activity_level_coefficient = 1.375 
            if selected_activity_level.get() == 2:
                activity_level_coefficient = 1.55 
            if selected_activity_level.get() == 3:
                activity_level_coefficient = 1.7 
            if selected_activity_level.get() == 4:
                activity_level_coefficient = 1.9
            
            js = calculate_daily_calories_standart(
                float(height_text_input.get()), float(weight_text_input.get()), int(age_text_input.get()), sex, activity_level_coefficient)
            print('js = ', js)
            
            daily_calories_standart_label.configure(text=round(js, 2))
            daily_calories_standart_label.pack()
            data = {
                "daily_calorie_standart": round(js, 2),
                "sex": sex,
                "height": float(height_text_input.get()),
                "weight": float(weight_text_input.get()),
                "age": int(age_text_input.get()),
                "activity": int(selected_activity_level.get())
            }
            with open('json\daily_calories_standart.json ', 'w') as outfile:
                json.dump(data, outfile)

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


        # вызов функции расчета суточной нормы калорий
        calculate_daily_calories_standart_button = Button(self,
                                                          text='Рассчитать', font=("Arial", 14),
                                                          command=lambda: calculate_and_save_daily_calories_standart())
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

        #def cliker(event):
        #    if event.char.isnumeric() or event.char == '.':  # надо проверить что точка одна?
        #        my_label = Label(self, text="что: " + event.char)
        #        my_label.place(x=500, y=580)
        #        my_label.pack()

        # поля для ввода параметров
        height_text_input = ttk.Entry(
            self, font=("Arial", 12), width=15)  # рост
        height_text_input.place(x=300, y=260)
        #height_text_input.bind("<Key>", cliker)

        weight_text_input = ttk.Entry(
            self, font=("Arial", 12), width=15)  # вес
        weight_text_input.place(x=80, y=550)
        age_text_input = ttk.Entry(self, font=(
            "Arial", 12), width=11)  # возраст
        age_text_input.place(x=400, y=550)
