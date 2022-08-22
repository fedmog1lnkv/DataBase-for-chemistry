from tkinter import *
from tkinter import Text
from tkinter import ttk
from tkinter.ttk import Combobox
import tkinter.filedialog as fd
import tkinter.messagebox as mb

from parser import Parser

bg = "#FFFFFF"
bgTable = "#FFFFFF"


class app:

    def __init__(self, master):
        self.master = master
        self.start()

    def start(self):
        self.master.geometry("700x200")

        with open("files/config.txt", "r") as f:
            s = f.readline()
            if s != "":
                self.filePath = s
            else:
                self.filePath = "Выберите файл"

        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=700, height=200, background=bg)
        self.frame1.place(relx=0, rely=0)


        self.text = Label(self.frame1, text="Автоматизированная информационная система\nпо выбору конструкционных материалов,\nиспользуемых в процессах химии и нефтехимии", font=("Geneva", 14), background=bg)
        self.text.place(relx=0.20, rely=0.15)

        self.fileFromConfig = Label(self.frame1, text=self.filePath, font=("Geneva", 12), background=bg)
        self.fileFromConfig.place(relx=0.10, rely=0.60)

        if self.filePath == "Выберите файл":
            self.choose_btn = Button(self.frame1, text="Выбрать", background="#6200EE", foreground="#FFFFFF", bd=1,
                                     font=("Geneva", 10),
                                     command=self.choose_file)
            self.choose_btn.place(relx=0.11, rely=0.75)

            self.exit_btn = Button(self.frame1, text="Выход", background="#6200EE", foreground="#FFFFFF", bd=1,
                                   font=("Geneva", 10),
                                   command=self.close_app)
            self.exit_btn.place(relx=0.70, rely=0.75)

        else:

            self.next_btn = Button(self.frame1, text="Начать", background="#6200EE", foreground="#FFFFFF", bd=1,
                                   font=("Geneva", 10),
                                   command=self.page_1)
            self.next_btn.place(relx=0.11, rely=0.75)

            self.choose_btn = Button(self.frame1, text="Другой файл", background="#6200EE", foreground="#FFFFFF", bd=1,
                                     font=("Geneva", 10),
                                     command=self.choose_file)
            self.choose_btn.place(relx=0.21, rely=0.75)

            self.exit_btn = Button(self.frame1, text="Выход", background="#6200EE", foreground="#FFFFFF", bd=1,
                                   font=("Geneva", 10),
                                   command=self.close_app)
            self.exit_btn.place(relx=0.70, rely=0.75)

    def page_1(self):
        try:
            self.Excel = Parser(self.filePath)
        except:
            self.error()
            self.start()
        finally:
            self.Excel = Parser(self.filePath)

        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master, width=700, height=200, background=bg)
        self.frame2.place(relx=0, rely=0)

        self.text = ttk.Label(self.frame2, text="Выберите вещество", font=("Geneva", 14), background=bg)
        self.text.place(relx=0.10, rely=0.15)

        self.choice_substance = Combobox(self.frame2, font=("Geneva", 10), width=25,
                                         values=self.Excel.parse_substance())
        self.choice_substance.place(relx=0.11, rely=0.30)

        self.next_btn = Button(self.frame2, text="Далее", background="#6200EE", foreground="#FFFFFF", bd=1,
                               font=("Geneva", 10),
                               command=self.page_2)
        self.next_btn.place(relx=0.75, rely=0.75)

    def page_2(self):
        self.choice_substance = self.choice_substance.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame3 = Frame(self.master, width=700, height=200, background=bg)
        self.frame3.place(relx=0, rely=0)

        if not (self.choice_substance in self.Excel.parse_substance()):
            self.text = ttk.Label(self.frame3, text="Вещество не найдено", font=("Geneva", 14), background=bg)
            self.text.place(relx=0.10, rely=0.15)

            self.reboot_btn = Button(self.frame3, text="Вернуться в начало", background="#6200EE", foreground="#FFFFFF",
                                     bd=1,
                                     font=("Geneva", 10), command=self.start)
            self.reboot_btn.place(relx=0.75, rely=0.75)
        else:
            self.text = ttk.Label(self.frame3, text="Выберите среду", font=("Geneva", 14), background=bg)
            self.text.place(relx=0.10, rely=0.15)

            self.lvl1 = ttk.Label(self.frame3, text=".\n├──" + self.choice_substance, font=("Geneva", 9), background=bg)
            self.lvl1.place(relx=0.60, rely=0.20)

            self.choice_env = ttk.Combobox(self.frame3, width=25, values=self.Excel.parse_env(self.choice_substance))
            self.choice_env.place(relx=0.11, rely=0.30)

            self.next_btn = Button(self.frame3, text="Далее", background="#6200EE", foreground="#FFFFFF", bd=1,
                                   font=("Geneva", 10),
                                   command=self.page_3)
            self.next_btn.place(relx=0.75, rely=0.75)

    def page_3(self):
        self.choice_env = self.choice_env.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame4 = Frame(self.master, width=700, height=200, background=bg)
        self.frame4.place(relx=0, rely=0)

        self.text = ttk.Label(self.frame4, text="Выберите температуру", font=("Geneva", 14), background=bg)
        self.text.place(relx=0.10, rely=0.15)

        self.lvl1 = ttk.Label(self.frame4, text=".\n├──" + self.choice_substance, font=("Geneva", 9), background=bg)
        self.lvl1.place(relx=0.60, rely=0.20)
        self.lvl2 = ttk.Label(self.frame4, text="└──" + self.choice_env, font=("Geneva", 9), background=bg)
        self.lvl2.place(relx=0.65, rely=0.35)

        self.choice_temp = ttk.Combobox(self.frame4, width=25, values=self.Excel.parse_temp(self.choice_env))
        self.choice_temp.place(relx=0.11, rely=0.30)

        self.next_btn = Button(self.frame4, text="Далее", background="#6200EE", foreground="#FFFFFF", bd=1,
                               font=("Geneva", 10),
                               command=self.page_4)
        self.next_btn.place(relx=0.75, rely=0.75)

    def page_4(self):
        self.choice_temp = self.choice_temp.get()

        for i in self.master.winfo_children():
            i.destroy()
        self.frame5 = Frame(self.master, width=700, height=200, background=bg)
        self.frame5.pack()

        self.text = ttk.Label(self.frame5, text="Выберите давление", font=("Geneva", 14), background=bg)
        self.text.place(relx=0.10, rely=0.15)

        self.lvl1 = ttk.Label(self.frame5, text=".\n├──" + self.choice_substance, font=("Geneva", 9), background=bg)
        self.lvl1.place(relx=0.60, rely=0.20)
        self.lvl2 = ttk.Label(self.frame5, text="└──" + self.choice_env, font=("Geneva", 9), background=bg)
        self.lvl2.place(relx=0.65, rely=0.35)
        self.lvl3 = ttk.Label(self.frame5, text="└──" + self.choice_temp, font=("Geneva", 9), background=bg)
        self.lvl3.place(relx=0.70, rely=0.44)

        self.choice_press = ttk.Combobox(self.frame5, width=25, values=self.Excel.parse_press(self.choice_temp))
        self.choice_press.place(relx=0.11, rely=0.30)

        self.next_btn = Button(self.frame5, text="Далее", background="#6200EE", foreground="#FFFFFF", bd=1,
                               font=("Geneva", 10),
                               command=self.page_5)
        self.next_btn.place(relx=0.75, rely=0.75)

    def page_5(self):
        self.choice_press = self.choice_press.get()

        for i in self.master.winfo_children():
            i.destroy()

        self.frame6 = Frame(self.master, width=700, height=200, background=bg)
        self.frame6.pack()

        self.text = ttk.Label(self.frame6, text="Выберите концентрацию", font=("Geneva", 14), background=bg)
        self.text.place(relx=0.10, rely=0.15)

        self.lvl1 = ttk.Label(self.frame6, text=".\n├──" + self.choice_substance, font=("Geneva", 9), background=bg)
        self.lvl1.place(relx=0.60, rely=0.20)
        self.lvl2 = ttk.Label(self.frame6, text="└──" + self.choice_env, font=("Geneva", 9), background=bg)
        self.lvl2.place(relx=0.65, rely=0.35)
        self.lvl3 = ttk.Label(self.frame6, text="└──" + self.choice_temp, font=("Geneva", 9), background=bg)
        self.lvl3.place(relx=0.70, rely=0.44)
        self.lvl4 = ttk.Label(self.frame6, text="└──" + self.choice_press, font=("Geneva", 9), background=bg)
        self.lvl4.place(relx=0.75, rely=0.51)

        self.choice_conc = ttk.Combobox(self.frame6, width=25, values=self.Excel.parse_conc(self.choice_press))
        self.choice_conc.place(relx=0.11, rely=0.30)

        self.next_btn = Button(self.frame6, text="Далее", background="#6200EE", foreground="#FFFFFF", bd=1,
                               font=("Geneva", 10),
                               command=self.page_6)
        self.next_btn.place(relx=0.75, rely=0.75)

    def page_6(self):
        self.master.geometry("1050x175")
        self.choice_conc = self.choice_conc.get()
        for i in self.master.winfo_children():
            i.destroy()

        self.frame = Frame(self.master, width=700, height=200, background=bgTable)
        self.frame.pack()

        widthText = 15

        self.out = self.Excel.output_table(self.choice_conc)

        self.substance_head = ttk.Label(self.frame, text="Вещество", font=("Geneva", 12), background=bg)
        self.substance_out = Text(self.frame,
                                  font=("Geneva", 12), height=5, width=25, wrap=WORD)
        self.substance_out.tag_configure("center", justify="center")
        self.substance_out.insert("1.0", self.out[0])
        self.substance_out.tag_add("center", "1.0", "end")
        self.substance_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                                     selectforeground="Black", cursor="arrow", relief="groove")
        self.substance_head.grid(row=0, column=0, ipady=3)
        self.substance_out.grid(row=1, column=0)

        self.env_head = ttk.Label(self.frame, text="Среда", font=("Geneva", 12), background=bg)
        self.env_out = Text(self.frame,
                            font=("Geneva", 12), height=5, width=widthText, wrap=WORD)
        self.env_out.tag_configure("center", justify="center")
        self.env_out.insert("1.0", self.out[1])
        self.env_out.tag_add("center", "1.0", "end")
        self.env_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                               selectforeground="Black", cursor="arrow", relief="groove")
        self.env_head.grid(row=0, column=1)
        self.env_out.grid(row=1, column=1)

        self.temp_head = ttk.Label(self.frame, text="Температура\n        °С", font=("Geneva", 12), background=bg)
        self.temp_out = Text(self.frame,
                             font=("Geneva", 12), height=5, width=widthText, wrap=WORD)
        self.temp_out.tag_configure("center", justify="center")
        self.temp_out.insert("1.0", self.out[2])
        self.temp_out.tag_add("center", "1.0", "end")
        self.temp_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                                selectforeground="Black", cursor="arrow", relief="groove")
        self.temp_head.grid(row=0, column=2)
        self.temp_out.grid(row=1, column=2)

        self.press_head = ttk.Label(self.frame, text="Давление\n    МПа", font=("Geneva", 12), background=bg)
        self.press_out = Text(self.frame,
                              font=("Geneva", 12), height=5, width=widthText, wrap=WORD)
        self.press_out.tag_configure("center", justify="center")
        self.press_out.insert("1.0", self.out[3])
        self.press_out.tag_add("center", "1.0", "end")
        self.press_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                                 selectforeground="Black", cursor="arrow", relief="groove")
        self.press_head.grid(row=0, column=3)
        self.press_out.grid(row=1, column=3)

        self.conc_head = ttk.Label(self.frame, text="Концентрация\n          %", font=("Geneva", 12), background=bg)
        self.conc_out = Text(self.frame,
                             font=("Geneva", 12), height=5, width=widthText, wrap=WORD)
        self.conc_out.tag_configure("center", justify="center")
        self.conc_out.insert("1.0", self.out[4])
        self.conc_out.tag_add("center", "1.0", "end")
        self.conc_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                                selectforeground="Black", cursor="arrow", relief="groove")
        self.conc_head.grid(row=0, column=4)
        self.conc_out.grid(row=1, column=4)

        self.materials_head = ttk.Label(self.frame, text="Материалы", font=("Geneva", 12), background=bg)
        self.materials_out = Text(self.frame,
                                  font=("Geneva", 12), height=5, width=25, wrap=WORD)
        self.materials_out.insert(INSERT, self.Excel.materials_text(str(self.out[5])))
        self.materials_out.configure(state='disabled', background=bgTable, selectbackground="#FFFFFF",
                                     selectforeground="Black", cursor="arrow", relief="groove")
        self.materials_head.grid(row=0, column=5)
        self.materials_out.grid(row=1, column=5)

        self.frameBtn = Frame(self.frame, width=700, height=50, background=bgTable)
        self.frameBtn.grid(row=2, columnspan=6)

        self.reboot_btn = Button(self.frameBtn, text="Вернуться в начало", background="#6200EE", foreground="#FFFFFF",
                                 bd=1,
                                 font=("Geneva", 10), command=self.start)
        self.reboot_btn.place(relx=0.65, rely=0.1)

        self.exit_btn = Button(self.frameBtn, text="Выход", background="#6200EE", foreground="#FFFFFF", bd=1,
                               font=("Geneva", 10),
                               command=self.close_app)
        self.exit_btn.place(relx=0.90, rely=0.1)

    def error(self):
        msg = "Файл не подходит"
        mb.showerror("Ошибка", msg)

    def choose_file(self):
        self.filename = fd.askopenfilename(title="Открыть файл")
        if self.filename:
            with open("files/config.txt", "w+") as f:
                f.write(str(self.filename))
            self.start()

    def close_app(self):
        window.destroy()


window = Tk()
window.configure(background=bg)
window.title("Database")
photo = PhotoImage(file="files/icon_database.png")
window.iconphoto(False, photo)

app(window)
window.mainloop()
