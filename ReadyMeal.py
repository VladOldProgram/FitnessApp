import tkinter as tk
from tkinter import ttk  
from tkinter import messagebox as mb
from PIL import ImageTk, Image


class Example(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.init_ui()

    def init_ui(self): # Хранение и инициализация всех объектов графического интерфейса
        btn_add = tk.Button(self, text='Очистить таблицу', command=self.delete_all)
        btn_add.place(x=750, y=770)
        btn_add2 = tk.Button(self, text='Удалить запись из таблицы')
        btn_add2.place(x=900, y=770)
        btn_add3 = tk.Button(self, text='Сохранить\n блюдо')
        btn_add3.place(x=400, y=750)
        self.searchbtn = tk.Button(self, text="Найти")
        self.searchbtn.place(x=380, y=10)

        # поисковая строка
        self.entry_txtNameProduct = tk.Entry(self, fg='Grey')
        entry_text2 = 'Поиск продуктов'
        self.entry_txtNameProduct.insert(0, entry_text2)
        self.entry_txtNameProduct.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry_txtNameProduct))
        self.entry_txtNameProduct.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry_txtNameProduct, entry_text2))
        self.entry_txtNameProduct.place(x=50, y=10, width=300)

        label_txtMealWeight = tk.Label(self, text='Введите вес готвого блюда в граммах')
        label_txtMealWeight.place(x=50, y=300)

        self.entry_txtMealWeight = ttk.Entry(self)
        self.entry_txtMealWeight.place(x=300, y=300, width=60)
        
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

        self.entry_txtNameMeal = tk.Entry(self, fg='Grey')
        entry_text = 'Введите название блюда'
        self.entry_txtNameMeal.insert(0, entry_text)
        self.entry_txtNameMeal.bind("<FocusIn>", lambda args: focus_in_entry_box(self.entry_txtNameMeal))
        self.entry_txtNameMeal.bind("<FocusOut>", lambda args: focus_out_entry_box(self.entry_txtNameMeal, entry_text))
        self.entry_txtNameMeal.place(x=50, y=760, width=300)

        frame = ttk.Frame(self)
        frame.place(x=510, y=0)

        self.tree = ttk.Treeview(frame, columns=('txtProductName', 'txtProductWeight', 'txtProductProteins', 'txtProductFats', 'txtProductCarbohydrates', 'txtProductCalories'), height=36, show='headings')

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
        self.scroll()

    def scroll(self):  
        scroll = tk.Scrollbar(command=self.tree.yview)  # Линейка прокрутки для списка
        self.tree.config(yscrollcommand=scroll.set)     
        scroll.place(x=1560, y=20, height=725)

    def delete_all(self):
        answer = mb.askyesno(message='Вы уверены, что хотите очистить таблицу?')

        if answer:
            #удалить все значения для конкретного блюда из json!
            self.db.delete_all()
            mb.showinfo(message='Таблица очищена')

    # def delete_by(self):

    #     # берем данные по нажатию на строку
    #     # удалить конкретный продукт из конкретного блюда из json!
    #     # self.db.search_by(self.search_dict[self.combobox_search.get()], self.enter_search.get())
    #     # fetch = self.db.c.fetchall()

    #     if not fetch:
    #         mb.showinfo('Удаление', 'Данные для удаления не найдены')
    #     else:
    #         answer = mb.askyesno(message='Вы уверены, что хотите удалить эти данные?')
    #         if answer:
    #             # удаляем по столбцам
    #             # self.db.delete_by(self.search_dict[self.combobox_search.get()], self.enter_search.get())
    #             mb.showinfo(message='Данные удалены')
    #             self.db.view_table()

    def on_select(self, val):
        sender = val.self
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)

    ##test
