from turtle import width
import json
import pyodbc
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Radiobutton  

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        # self.button = tk.Button(self, text='Append', command=self.on_append)
        # self.button.pack()

        # self.pack()

         #радиобаттон
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


        #поля с выводом текста
        # self.radio_woman = ttk.Radiobutton(self, text='Женщина', value=0)
        # self.radio_woman.place(x=100, y=30)  
        # self.radio_man = ttk.Radiobutton(self, text='Мужчина', value=0)  
        # self.radio_man.place(x=250, y=30)
        label_height = tk.Label(self, text='Рост(см.)')
        label_height.place(x=325, y=280)
        label_weight = tk.Label(self, text='Вес(кг.)')
        label_weight.place(x=120, y=580)
        label_age = tk.Label(self, text='Возраст')
        label_age.place(x=340, y=550)
        label_age = tk.Label(self, text='лет')
        label_age.place(x=540, y=550)

        #поля для ввода параметров
        self.entry_height = ttk.Entry(self)
        self.entry_height.place(x=300, y=260)
        self.entry_weight = ttk.Entry(self)
        self.entry_weight.place(x=80, y=550)

        self.entry_age = ttk.Entry(self)
        self.entry_age.place(x=400, y=550)

        #уровень активности
        v = tk.IntVar()
        v.set(2)  #выбор по умолчанию

        #берем данные из json
        #with open('CalorieDailyRate.json', 'r') as file:
        #    data = json.load(file)

        #print(data['activity'])

        #брать из json
        activity = [("минимальная", 0),
                    ("низкая", 1),
                    ("умеренная", 2),
                    ("высокая", 3),
                    ("экстремальная", 4)]

        def ShowChoice():
            print(v.get()) 

        tk.Label(self, 
                text="""Уровень активности:""",
                justify = tk.LEFT,
                padx = 200).pack()
        for activ, val in activity:
            position = {"padx":300, "pady":0, "anchor":tk.NW}
            self.activiity=tk.Radiobutton(self, 
                    text=activ,
                    indicatoron = 0,
                    width = 30,
                    padx = 180, 
                    variable=v, 
                    command=ShowChoice,
                    value=val).pack(position)


                
        #нередактируемое поле с информацией об уровне активности
        activity_definition = ''
        print(val)
        for activ, val in activity:
            print(val)
            if (val == 0):
                activity_definition = 'описание минимальной активности'
        labelframe = tk.LabelFrame(self, width=300, height=80)
        labelframe.place(x=500, y=340)
        
        lbl_count2 = tk.Label(labelframe, text=activity_definition, font=("Arial", 10))
        lbl_count2.pack()
        
        #нередактируемое поле с информацией о суточной норме калорий
        print_calories = ''
        labelframe = tk.LabelFrame(self, width=200, height=40, text='Суточная норма калорий')
        labelframe.place(x=100, y=700)
        
        lbl_count2 = tk.Label(labelframe, text=print_calories, font=("Arial", 10))
        lbl_count2.pack()

        #расчет суточной нормы калорий
        btn_ok = ttk.Button(self, text='Рассчитать')
        btn_ok.place(x=300, y=710)

    # def on_append(self):
    #     print('Hello World!')

