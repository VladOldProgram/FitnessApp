import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
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
        product_weight_stepper_input.place(x=160, y=55)

        # поисковая строка
        foodstruct_search_line = tk.Entry(frame_foodstruct_add_product, fg='Grey')
        entry_text2 = 'Поиск продуктов/блюд'
        foodstruct_search_line.insert(0, entry_text2)
        foodstruct_search_line.bind("<FocusIn>", lambda args: focus_in_entry_box(foodstruct_search_line))
        foodstruct_search_line.bind("<FocusOut>", lambda args: focus_out_entry_box(foodstruct_search_line, entry_text2))
        foodstruct_search_line.place(x=20, y=40, width=300)

        # создание placeholder...
        def focus_out_entry_box(frame_foodstruct_add_product, frame_foodstruct_add_product_text):
            if frame_foodstruct_add_product['fg'] == 'Black' and len(frame_foodstruct_add_product.get()) == 0:
                frame_foodstruct_add_product.delete(0, tk.END)
                frame_foodstruct_add_product['fg'] = 'Grey'
                frame_foodstruct_add_product.insert(0, frame_foodstruct_add_product_text)

        def focus_in_entry_box(frame_foodstruct_add_product):
            if frame_foodstruct_add_product['fg'] == 'Grey':
                frame_foodstruct_add_product['fg'] = 'Black'
                frame_foodstruct_add_product.delete(0, tk.END)

        searchbtn = tk.Button(frame_foodstruct_add_product, text="Найти", font=("Arial", 10))
        searchbtn.place(x=350, y=40)

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

        self.tree.pack()

