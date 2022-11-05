import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb

class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self):
        btn_add2 = tk.Button(self, text='Удалить зиз дневника питания')
        btn_add2.place(x=900, y=770)

        label_txtMealWeight = tk.Label(self, text='Дневник питания', font='Arial 15 bold')
        label_txtMealWeight.place(x=710, y=0)

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

