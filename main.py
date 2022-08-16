from tkinter import *
from tkinter import ttk
from parser import Parser

Ecxel = Parser()

print("выберите нужное вещество:", *(Ecxel.parse_substance()))

class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.login()

    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.text = ttk.Label(self.frame1, text='Поиск веществ')
        self.text.pack()
        self.next_btn = ttk.Button(self.frame1, text="Начать", command=self.register)
        self.next_btn.pack()

    def register(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.text = ttk.Label(self.frame2, text='Выберите вещество')
        self.text.pack()
        self.choice_substance = ttk.Combobox(self.frame2, values=Ecxel.parse_substance())
        self.choice_substance.pack()
        self.next_btn = ttk.Button(self.frame2, text="Далее", command=self.login)
        self.next_btn.pack()



window = Tk()
app(window)
window.mainloop()
