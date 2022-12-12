from tkinter import ttk
import tkinter as tk
import json
import schedule
import time
import threading

from dish_nutrients_form import Dish_nutrients_form
from daily_calories_standart_form import Daily_calories_standart
from food_diary_form import Food_diary_form

class MainInterface:
    window = tk.Tk()
    notebook = ttk.Notebook(window, width=800, height=800, style='lefttab.TNotebook')
    dish_nutrients_tab = Dish_nutrients_form(notebook)
    daily_calories_standart_tab = Daily_calories_standart(notebook)
    food_diary_tab = Food_diary_form(notebook)

    def __init__(self):
        self.window.title('FitnessApp')
        self.window.geometry("1600x840")
        self.window.resizable(False, False)
        self.window['padx'] = 10
        self.window['pady'] = 10

        #то, что будет отображаться на самой вкладке и ширина вкладки(^числоs)
        self.notebook.add(self.dish_nutrients_tab, text=f'{"Подсчет КБЖУ готового блюда": ^46s}')#46
        self.notebook.add(self.daily_calories_standart_tab, text=f'{"Подсчет суточной нормы калорий": ^42s}')#42
        self.notebook.add(self.food_diary_tab, text=f'{"Дневник питания": ^60s}')#60
        self.notebook.pack(expand=True, fill=tk.BOTH)
        style = ttk.Style() #создаем стиль, чтобы изменить вид вкладок
        style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"padding": [0, 0, 0, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [130, 130] }}})

        style.theme_use("MyStyle")
        #по хорошему это тоже надо запихать в создание стиля, для красоты кода
        style.configure('lefttab.TNotebook', tabposition='ws') #отображение вкладок по левой стороне
        style.configure('TNotebook.Tab', background="White") #цвет вкладок
        style.map("TNotebook.Tab", background= [("selected", "Gray")])

        style.configure('Treeview', background="white")
        style.map('Treeview', background=[("selected", "cornflower blue")])

def checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    root = MainInterface()
    #schedule.every().day.at('23:59:50').do(reset_diary)
    schedule.every(2).seconds.do(
        root.food_diary_tab.update_daily_calories_standart()
    )
    checker_thread = threading.Thread(target=checker, daemon=True)
    checker_thread.start()
    
    root.window.mainloop()
