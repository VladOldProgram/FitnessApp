from tkinter import ttk
import tkinter as tk

# import schedule
# import time
# import threading
# from FAKEFUNC import *

from dish_nutrients_form import Example as ReadyMeal
from daily_calories_standart_form import Daily_calories_standart as CalorieDailyRate
from food_diary_form import Example as NutritionDiary

class MainInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('FitnessApp')
        self.window.geometry("1600x840")
        self.window.resizable(False, False)
        self.create_widgets()
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


    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10

        self.notebook = ttk.Notebook(self.window, width=800, height=800, style='lefttab.TNotebook')

        #то, что будет отображаться, при нажатии на вкладку
        ready_meal_tab = ReadyMeal(self.notebook)
        calorie_dayli_rate_tab = CalorieDailyRate(self.notebook)
        nutrition_diary_tab = NutritionDiary(self.notebook)

        #то, что будет отображаться на самой вкладке и ширина вкладки(^числоs)
        self.notebook.add(ready_meal_tab, text=f'{"Подсчет КБЖУ готового блюда": ^46s}')#46
        self.notebook.add(calorie_dayli_rate_tab, text=f'{"Подсчет суточной нормы калорий": ^42s}')#42
        self.notebook.add(nutrition_diary_tab, text=f'{"Дневник питания": ^60s}')#60
        self.notebook.pack(expand=True, fill=tk.BOTH)

# def checker():
#    while True:
#        schedule.run_pending()
#        time.sleep(1)
        
if __name__ == '__main__':
    # schedule.every().day.at('23:59:50').do(reset_diary)
    # checker_thread = threading.Thread(target=checker, daemon=True)
    # checker_thread.start()

    root = MainInterface()
    root.window.mainloop()
