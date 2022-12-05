import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image
from tkinter import *

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        
        self.image_loupa = ImageTk.PhotoImage(file="assets\images\loupa_small.png")
        self.loupa = Label(self, image=self.image_loupa)
        self.loupa.place(x=22, y=4)
        
        btn_add2 = tk.Button(self, text='Удалить из дневника питания')
        btn_add2.place(x=900, y=770)

        label_txtMealWeight = tk.Label(self, text='Дневник питания', font='Arial 15 bold')
        label_txtMealWeight.place(x=710, y=0)

        # поле для добавления продукта/блюда
        frame_foodstruct_add_product = tk.LabelFrame(self, width=430, height=230)
        frame_foodstruct_add_product.place(x=30, y=10)
        label_foodstruct_add_product = tk.Label(frame_foodstruct_add_product, text='Добавление продукта/блюда', font=("Arial", 10))
        label_foodstruct_add_product.place(x=100, y=10)
        product_weight_stepper_input = ttk.Entry(frame_foodstruct_add_product, font=("Arial", 10), width=10)
        product_weight_stepper_input.place(x=320, y=105)
        add_product_button = tk.Button(frame_foodstruct_add_product, text="Добавить в дневник питания", font=("Arial", 10))
        add_product_button.place(x=210, y=170)

        # поисковая строка продуктов/блюд
        foodstruct_search_line = tk.Entry(frame_foodstruct_add_product, fg='Grey')
        entry_text2 = 'Поиск продуктов/блюд'
        foodstruct_search_line.insert(0, entry_text2)
        foodstruct_search_line.bind("<FocusIn>", lambda args: focus_in_entry_box(foodstruct_search_line))
        foodstruct_search_line.bind("<FocusOut>", lambda args: focus_out_entry_box(foodstruct_search_line, entry_text2))
        foodstruct_search_line.place(x=20, y=40, width=300)

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

        searchbtn = tk.Button(frame_foodstruct_add_product, text="Найти", font=("Arial", 10))
        searchbtn.place(x=360, y=35)

        # поле для добавления сохраненного блюда
        frame_foodstruct_add_dish = tk.LabelFrame(self, width=430, height=510)
        frame_foodstruct_add_dish.place(x=30, y=260)
        label_foodstruct_add_dish = tk.Label(frame_foodstruct_add_dish, text='Добавление продукта/блюда', font=("Arial", 10))
        label_foodstruct_add_dish.place(x=100, y=10)

        # поисковая строка сохраненных блюд
        saved_dishes_search_line  = tk.Entry(frame_foodstruct_add_dish, fg='Grey')
        entry_text3 = 'Поиск сохраненных блюд'
        saved_dishes_search_line .insert(0, entry_text2)
        saved_dishes_search_line .bind("<FocusIn>", lambda args: focus_in_entry_box(saved_dishes_search_line ))
        saved_dishes_search_line .bind("<FocusOut>", lambda args: focus_out_entry_box(saved_dishes_search_line , entry_text3))
        saved_dishes_search_line .place(x=20, y=40, width=300)

        searchbtn2 = tk.Button(frame_foodstruct_add_dish, text="Найти", font=("Arial", 10))
        searchbtn2.place(x=360, y=35)

        # таблица сохраненных блюд
        frame = ttk.Frame(frame_foodstruct_add_dish)
        frame.place(x=20, y=100)

        self.tree = ttk.Treeview(frame, columns=('txtProductName', 'txtProductWeight', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductCalories'), height=34, show='headings')

        self.tree.column('txtProductName', width=150, anchor=tk.CENTER)
        self.tree.column('txtProductWeight', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCalories', width=95, anchor=tk.CENTER)

        self.tree.heading('txtProductName', text='Продукт')
        self.tree.heading('txtProductWeight', text='Вес, гр.')
        self.tree.heading('txtProductProteins', text='Белки, гр.')
        self.tree.heading('txtProductFats', text='Жиры, гр.')
        self.tree.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.tree.heading('txtProductCalories', text='Калории, ккал.')

        # таблица дневника питания
        frame = ttk.Frame(self)
        frame.place(x=500, y=40)

        self.tree = ttk.Treeview(frame, columns=('txtProductName', 'txtProductWeight', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductCalories'), height=34, show='headings')

        self.tree.column('txtProductName', width=150, anchor=tk.CENTER)
        self.tree.column('txtProductWeight', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductProteins', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductFats', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCarbohydrates', width=80, anchor=tk.CENTER)
        self.tree.column('txtProductCalories', width=95, anchor=tk.CENTER)

        self.tree.heading('txtProductName', text='Продукт')
        self.tree.heading('txtProductWeight', text='Вес, гр.')
        self.tree.heading('txtProductProteins', text='Белки, гр.')
        self.tree.heading('txtProductFats', text='Жиры, гр.')
        self.tree.heading('txtProductCarbohydrates', text='Углеводы, гр.')
        self.tree.heading('txtProductCalories', text='Калории, ккал.')

        scroll = tk.Scrollbar(frame, command=self.tree.yview)  # Линейка прокрутки для списка
        scroll.place(x=1560, y=50, height=695)
        self.tree.config(yscrollcommand=scroll.set)  
        scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.tree.pack()


