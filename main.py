from tkinter import *
from tkinter import ttk

from parser import Parser


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("700x300")
        self.Ecxel = Parser()
        self.start()

    def start(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=300, height=300)
        self.frame1.pack()
        self.text = ttk.Label(self.frame1, text="Поиск веществ")
        self.text.pack()
        self.next_btn = ttk.Button(self.frame1, text="Начать", command=self.page_1)
        self.next_btn.pack()

    def page_1(self):
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()

        self.text = ttk.Label(self.frame2, text="Выберите вещество")
        self.text.pack()

        self.choice_substance = ttk.Combobox(self.frame2, values=self.Ecxel.parse_substance())
        self.choice_substance.pack()

        self.next_btn = ttk.Button(self.frame2, text="Далее", command=self.page_2)
        self.next_btn.pack()

    def page_2(self):
        self.choice_substance = self.choice_substance.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame3 = Frame(self.master, width=300, height=300)
        self.frame3.pack()

        self.text = ttk.Label(self.frame3, text="Выберите среду")
        self.text.pack()

        self.choice_env = ttk.Combobox(self.frame3, values=self.Ecxel.parse_env(self.choice_substance))
        self.choice_env.pack()

        self.next_btn = ttk.Button(self.frame3, text="Далее", command=self.page_3)
        self.next_btn.pack()

    def page_3(self):
        self.choice_env = self.choice_env.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame4 = Frame(self.master, width=300, height=300)
        self.frame4.pack()

        self.text = ttk.Label(self.frame4, text="Выберите температуру")
        self.text.pack()

        self.choice_temp = ttk.Combobox(self.frame4, values=self.Ecxel.parse_temp(self.choice_env))
        self.choice_temp.pack()

        self.next_btn = ttk.Button(self.frame4, text="Далее", command=self.page_4)
        self.next_btn.pack()

    def page_4(self):
        self.choice_temp = self.choice_temp.get()

        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=300, height=300)
        self.frame5.pack()

        self.text = ttk.Label(self.frame5, text="Выберите давление")
        self.text.pack()

        self.choice_press = ttk.Combobox(self.frame5, values=self.Ecxel.parse_press(self.choice_temp))
        self.choice_press.pack()

        self.next_btn = ttk.Button(self.frame5, text="Далее", command=self.page_5)
        self.next_btn.pack()

    def page_5(self):
        self.choice_press = self.choice_press.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame6 = Frame(self.master, width=300, height=300)
        self.frame6.pack()

        self.text = ttk.Label(self.frame6, text="Выберите концентрацию")
        self.text.pack()

        self.choice_conc = ttk.Combobox(self.frame6, values=self.Ecxel.parse_conc(self.choice_press))
        self.choice_conc.pack()

        self.next_btn = ttk.Button(self.frame6, text="Далее", command=self.page_6)
        self.next_btn.pack()

    def page_6(self):
        self.choice_conc = self.choice_conc.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame = Frame(self.master, width=300, height=300)
        self.frame.pack()

        self.out = self.Ecxel.output_table(self.choice_conc)

        self.text1 = ttk.Label(self.frame, text=self.out[0])
        self.text1.grid(row=0, column=0)

        self.text2 = ttk.Label(self.frame, text=self.out[1])
        self.text2.grid(row=0, column=1, padx=10)

        self.text3 = ttk.Label(self.frame, text=self.out[2])
        self.text3.grid(row=0, column=2, padx=10)

        self.text4 = ttk.Label(self.frame, text=self.out[3])
        self.text4.grid(row=0, column=3, padx=10)

        self.text5 = ttk.Label(self.frame, text=self.out[4])
        self.text5.grid(row=0, column=4, padx=10)

        self.text6 = ttk.Label(self.frame, text=self.out[5])
        self.text6.grid(row=0, column=5, padx=10)




window = Tk()
app(window)
window.mainloop()
