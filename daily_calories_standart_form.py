import json
from tkinter import ttk
import tkinter as tk
from calculate import * 
from json import JSONDecodeError
import json

class Daily_calories_standart(tk.Frame):
    daily_calories_standart = 0.0

    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

        self.daily_calories_standart = self.get_daily_calories_standart()

        self.sex = True

        self.image_female_button = tk.PhotoImage(file='assets\\images\\female_button.png')
        self.image_male_button = tk.PhotoImage(file='assets\\images\\male_button.png')
        self.image_female = tk.PhotoImage(file='assets\\images\\female.png')
        self.image_male = tk.PhotoImage(file='assets\\images\\male.png')

        self.selected_sex_image = tk.Label(self, image=self.image_male)
        self.selected_sex_image.place(x=80, y=80)

        self.switch_female_button = tk.Button(self, image=self.image_female_button)
        self.switch_female_button.place(x=450, y=30)
        self.switch_female_button.bind('<Button-1>', self.switch_female)

        self.switch_male_button = tk.Button(self, image=self.image_male_button)
        self.switch_male_button.place(x=750, y=30)
        self.switch_male_button.bind('<Button-1>', self.switch_male)

        self.activity_level_descriptions = [
            'Малоподвижный образ жизни, сидячая работа, отсутствие физических нагрузок.',
            'Интенсивные упражнения не менее 20 минут от 1 до 3 раз в неделю. Например, езда на велосипеде, бег трусцой, баскетбол, плавание, катание на коньках, и т.д. Или если часто приходится ходить в течение длительных периодов времени при отсутствии тренировок.',
            'Уровень физической активности, который несколько повышает частоту сердечных сокращений и оставляет у вас ощущение тепла и легкой одышки, например, усилия, затрачиваемые здоровым человеком при быстрой ходьбе, плавании, езде на велосипеде по ровной поверхности, танцах. Интенсивные упражнения от 30 до 60 минут от 3 до 5 раз в неделю.',
            'Уровень физической активности, который значительно повышает частоту сердечных сокращений и вызывает появление пота, например, усилия, затрачиваемые здоровым человеком при беге, занятиях аэробикой, плавании на дистанцию, быстрой езде на велосипеде, подъеме в гору.  Выполнение интенсивных упражнений не менее 60 минут от 5 до 7 дней в неделю или занятия 2 раза в день.',
            '7 или более часов в неделю очень интенсивных упражнений или интенсивные занятия 2 раза в день. Очень интенсивные и/или очень затратные виды деятельности. Например, профессиональный спортсмен с несколькими тренировками в течение дня или тяжелая физическая работа, такая, как разгрузка угля лопатой или работа на сборочной линии в течение нескольких часов.'
        ]
        self.activity_level_description_text = tk.Text(self, wrap=tk.WORD, font=("Arial", 10))
        self.activity_level_description_text.place(x=630, y=480, height=300, width=400)
        self.activity_level_description_text.insert(1.0, self.activity_level_descriptions[0])
        self.activity_level_description_text.configure(state=tk.DISABLED)

        self.selected_activity_level = tk.IntVar()
        self.selected_activity_level.set(0)
        self.activity_level_label = tk.Label(self, text='Уровень активности:', font=("Arial", 10))
        self.activity_level_label.place(x=743, y=215)
        self.activity_level_vertical_menu = tk.Radiobutton(
            self, 
            text='Минимальный', 
            font=('Arial', 10), 
            indicatoron=0, 
            width=20, 
            padx=60, 
            variable=self.selected_activity_level, 
            command=self.switch_activity_level_description, 
            value=0
        )
        self.activity_level_vertical_menu.place(x=670, y=240)
        self.activity_level_vertical_menu = tk.Radiobutton(
            self, 
            text='Низкий', 
            font=('Arial', 10), 
            indicatoron=0, 
            width=20, 
            padx=60, 
            variable=self.selected_activity_level, 
            command=self.switch_activity_level_description, 
            value=1
        )
        self.activity_level_vertical_menu.place(x=670, y=265)
        self.activity_level_vertical_menu = tk.Radiobutton(
            self, 
            text='Умеренный', 
            font=('Arial', 10), 
            indicatoron=0, 
            width=20, 
            padx=60, 
            variable=self.selected_activity_level, 
            command=self.switch_activity_level_description, 
            value=2
        )
        self.activity_level_vertical_menu.place(x=670, y=290)
        self.activity_level_vertical_menu = tk.Radiobutton(
            self, 
            text='Высокий', 
            font=('Arial', 10), 
            indicatoron=0, 
            width=20, 
            padx=60, 
            variable=self.selected_activity_level, 
            command=self.switch_activity_level_description, 
            value=3)
        self.activity_level_vertical_menu.place(x=670, y=315)
        self.activity_level_vertical_menu = tk.Radiobutton(
            self, 
            text='Экстремальный', 
            font=('Arial', 10), 
            indicatoron=0, 
            width=20, 
            padx=60, 
            variable=self.selected_activity_level, 
            command=self.switch_activity_level_description, 
            value=4)
        self.activity_level_vertical_menu.place(x=670, y=340)

        self.height_label = tk.Label(self, text='Рост (см.)', font=("Arial", 10))
        self.height_label.place(x=320, y=280)
        self.weight_label = tk.Label(self, text='Вес (кг.)', font=("Arial", 10))
        self.weight_label.place(x=120, y=520)
        self.age_label_1 = tk.Label(self, text='Возраст', font=("Arial", 10))
        self.age_label_1.place(x=330, y=546)
        self.age_label_2 = tk.Label(self, text='лет', font=("Arial", 10))
        self.age_label_2.place(x=510, y=546)

        self.height_entry = tk.Entry(self, font=("Arial", 10), width=15, validate='key')
        #self.height_entry['validatecommand'] = (self.height_entry.register(self.char_is_validate), '%P', '%d')
        self.height_entry.place(x=300, y=260)

        self.weight_entry = tk.Entry(self, font=("Arial", 10), width=15)
        self.weight_entry.place(x=100, y=490)
        self.age_entry = tk.Entry(self, font=("Arial", 10), width=11)
        self.age_entry.place(x=400, y=550)

        self.label_frame = tk.LabelFrame(self, width=165, height=50, text='Суточная норма калорий', font=("Arial", 10))
        self.label_frame.place(x=120, y=640)
        self.label_frame.pack_propagate(False)
        self.daily_calories_standart_label = tk.Label(self.label_frame, text=self.daily_calories_standart, font=("Arial", 10))

        self.calculate_daily_calories_standart_button = tk.Button(
            self,
            text='Рассчитать', 
            font=("Arial", 10),
            command=self.calculate_and_save_daily_calories_standart
        )
        self.calculate_daily_calories_standart_button.place(x=320, y=655)

        self.clear_inputs_button = tk.Button(
            self, 
            text='Очистить \n поля ввода', 
            font=("Arial", 10), 
            command=self.clear_inputs
        )
        self.clear_inputs_button.place(x=100, y=730)

    def get_daily_calories_standart(self):
        try:
            with open('json\daily_calories_standart.json', 'r') as my_file:
                f = my_file.read()
                try:
                    return(json.loads(f)['daily_calories_standart'])
                except JSONDecodeError:
                    return 0.0
        except FileNotFoundError:
            return 0.0

    #def testVal(self, inStr, acttyp):
    #    if acttyp == '1':
    #        if not inStr.isdigit():
    #            return False
    #    return True

    def char_is_validate(self, char, why_d, where_i, what_S):
        return True

    def switch_female(self, event):
        self.sex = False
        self.selected_sex_image.configure(image=self.image_female)

    def switch_male(self, event):
        self.sex = True
        self.selected_sex_image.configure(image=self.image_male)

    def switch_activity_level_description(self):
        self.activity_level_description_text.configure(state=tk.NORMAL)
        self.activity_level_description_text.delete(1.0, tk.END)
        i = self.selected_activity_level.get()
        self.activity_level_description_text.insert(1.0, self.activity_level_descriptions[i])
        self.activity_level_description_text.configure(state=tk.DISABLED)

    def calculate_and_save_daily_calories_standart(self):
        i = self.selected_activity_level.get()
        activity_level_coefficients = [1.2, 1.375, 1.55, 1.7, 1.9]
        activity_level_coefficient = activity_level_coefficients[i]
        
        try:
            height_f = float(self.height_entry.get())
            weight_f = float(self.weight_entry.get())
            age_i = int(self.age_entry.get())
        except:
            return

        self.daily_calories_standart = calculate_daily_calories_standart(
             height_f, 
             weight_f, 
             age_i, 
             self.sex, 
             activity_level_coefficient
        )
        self.daily_calories_standart = round(self.daily_calories_standart, 2)
        
        self.daily_calories_standart_label.configure(text=self.daily_calories_standart)
        self.daily_calories_standart_label.pack()
        data = {
            'daily_calories_standart': self.daily_calories_standart,
            'sex': self.sex,
            'height': float(self.height_entry.get()),
            'weight': float(self.weight_entry.get()),
            'age': int(self.age_entry.get()),
            'activity_level': int(self.selected_activity_level.get())
        }
        
        with open('json\daily_calories_standart.json', 'w+') as outfile:
            json.dump(data, outfile)

    def clear_inputs(self):
        self.height_entry.delete('0', tk.END)
        self.weight_entry.delete('0', tk.END)
        self.age_entry.delete('0', tk.END)
        self.selected_activity_level.set(0)
        self.activity_level_description_text.configure(state=tk.NORMAL)
        self.activity_level_description_text.delete(1.0, tk.END)
        self.activity_level_description_text.insert(1.0, self.activity_level_descriptions[0])
        self.activity_level_description_text.configure(state=tk.DISABLED)
