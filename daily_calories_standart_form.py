import json
from tkinter import ttk
import tkinter as tk
from calculate import * 
from json import JSONDecodeError
import json
from tkinter import messagebox as mb


''' Описывает структуру и работу второй экранной формы Подсчет среднесуточной нормы калорий '''
class Daily_calories_standart(tk.Frame):
    daily_calories_standart = 0.0

    def __init__(self, parent: ttk.Notebook):
        super().__init__(parent)

        self.daily_calories_standart = self.get_daily_calories_standart()

        ''' Логический тип данных - пол, изначально True - Мужской пол'''
        self.sex = True

        ''' Загружаются картинки'''
        self.image_female_button = tk.PhotoImage(file='assets\\images\\female_button.png')
        self.image_male_button = tk.PhotoImage(file='assets\\images\\male_button.png')
        self.image_female = tk.PhotoImage(file='assets\\images\\female.png')
        self.image_male = tk.PhotoImage(file='assets\\images\\male.png')

        self.selected_sex_image = tk.Label(self, image=self.image_male)
        self.selected_sex_image.place(x=80, y=80)

        '''Кнопка переключения пола на женский'''
        self.switch_female_button = tk.Button(self, image=self.image_female_button)
        self.switch_female_button.place(x=450, y=30)
        self.switch_female_button.bind('<Button-1>', self.switch_female)

        '''Кнопка переключения пола на мужской'''
        self.switch_male_button = tk.Button(self, image=self.image_male_button)
        self.switch_male_button.place(x=750, y=30)
        self.switch_male_button.bind('<Button-1>', self.switch_male)

        '''Массив описаний всех уровней физической активности'''
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

        '''Выбранный уровень физической активности'''
        self.selected_activity_level = tk.IntVar()
        self.selected_activity_level.set(0)
        self.activity_level_label = tk.Label(self, text='Уровень активности:', font=("Arial", 10))
        self.activity_level_label.place(x=743, y=215)
        
        '''Меню выбора уровня физической активности'''
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

        '''Поле ввода роста'''
        self.height_text_input = tk.Entry(self, font=("Arial", 10), width=15, validate='key')
        self.height_text_input['validatecommand'] = (self.height_text_input.register(self.value_is_float), '%P', '%d')
        self.height_text_input.place(x=300, y=260)

        '''Поле ввода веса'''
        self.weight_text_input = tk.Entry(self, font=("Arial", 10), width=15, validate='key')
        self.weight_text_input['validatecommand'] = (self.weight_text_input.register(self.value_is_float), '%P', '%d')
        self.weight_text_input.place(x=100, y=490)
        
        '''Поле ввода возраста'''
        self.age_text_input = tk.Entry(self, font=("Arial", 10), width=11, validate='key')
        self.age_text_input['validatecommand'] = (self.weight_text_input.register(self.value_is_int), '%P', '%d')
        self.age_text_input.place(x=400, y=550)

        self.label_frame = tk.LabelFrame(self, width=165, height=50, text='Суточная норма калорий', font=("Arial", 10))
        self.label_frame.place(x=120, y=640)
        self.label_frame.pack_propagate(False)

        '''Лейбл с подсчитанной суточной нормой калорий'''
        self.daily_calories_standart_label = tk.Label(self.label_frame, text=self.daily_calories_standart, font=("Arial", 10))

        ''' Кнопка расчета и сохранения в json-файл суточной нормы калорий'''
        self.calculate_daily_calories_standart_button = tk.Button(
            self,
            text='Рассчитать', 
            font=("Arial", 10),
            command=self.calculate_and_save_daily_calories_standart
        )
        self.calculate_daily_calories_standart_button.place(x=320, y=655)

        '''Кнопка очистки всех полей ввода страницы'''
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

    def value_is_int(self, P, d):
        if d == '1':
            try:
                int(P)
            except ValueError:
                return False
        return True
 
    def switch_female(self, event):
        '''Устанавливает sex = False и устанавливает картинку силуэта человека на женский. 
        Ничего не возвращает.'''
        self.sex = False
        self.selected_sex_image.configure(image=self.image_female)

    def switch_male(self, event):
        '''Устанавливает sex = True и устанавливает картинку силуэта человека на мужской. 
        Ничего не возвращает'''
        self.sex = True
        self.selected_sex_image.configure(image=self.image_male)

    def switch_activity_level_description(self):
        '''Изменяет текст activity_level_description_label по выбору текущего уровня физической активности 
        (элемент массива activity_level_descriptions). 
        Ничего не возвращает.'''
        self.activity_level_description_text.configure(state=tk.NORMAL)
        self.activity_level_description_text.delete(1.0, tk.END)
        i = self.selected_activity_level.get()
        self.activity_level_description_text.insert(1.0, self.activity_level_descriptions[i])
        self.activity_level_description_text.configure(state=tk.DISABLED)

    def calculate_and_save_daily_calories_standart(self):
        '''Вызывает метод calculate_daily_calorie_standart() и 
        записывает суточную норму калорий в файл daily_calorie_standart.json. 
        Ничего не возвращает.'''
        if self.height_text_input.get() == '' and self.weight_text_input.get() == '' and self.age_text_input.get() == '':
            mb.showinfo('Уведомление', 'Введите все параметры!')
            return
        elif self.height_text_input.get() == '':
            mb.showinfo('Уведомление', 'Введите рост!')
            return
        elif self.weight_text_input.get() == '':
            mb.showinfo('Уведомление', 'Введите вес!')
            return
        elif self.age_text_input.get() == '': 
            mb.showinfo('Уведомление', 'Введите возраст!')
            return

        try:
            height_f = float(self.height_text_input.get())
            weight_f = float(self.weight_text_input.get())
            age_i = int(self.age_text_input.get())
            activity_level = int(self.selected_activity_level.get())
        except:
            return

        '''Проверка введенных значений'''
        if height_f < 120 or height_f > 272:
            mb.showinfo('Уведомление', 'Рост должен быть в диапазоне от 120 до 272!')
            return
        elif weight_f < 40 or weight_f > 200:
            mb.showinfo('Уведомление', 'Вес должен быть в диапазоне от 40 до 200!')
            return
        elif age_i < 14 or age_i > 80:
            mb.showinfo('Уведомление', 'Возраст должен быть в диапазоне от 14 до 80!')
            return

        self.daily_calories_standart = calculate_and_save_daily_calories(self.sex, height_f, weight_f, age_i, activity_level)

        self.daily_calories_standart_label.configure(text=self.daily_calories_standart)
        self.daily_calories_standart_label.pack()

    def clear_inputs(self):
        ''' Очищает поля ввода height_text_input, weight_text_input, age_text_input 
        и устанавливает первое состояние для activity_level_vertical_menu. 
        Ничего не возвращает.'''
        self.height_text_input.delete('0', tk.END)
        self.weight_text_input.delete('0', tk.END)
        self.age_text_input.delete('0', tk.END)
        self.selected_activity_level.set(0)
        self.activity_level_description_text.configure(state=tk.NORMAL)
        self.activity_level_description_text.delete(1.0, tk.END)
        self.activity_level_description_text.insert(1.0, self.activity_level_descriptions[0])
        self.activity_level_description_text.configure(state=tk.DISABLED)
