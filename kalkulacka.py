import tkinter as tk
from tkinter import ANCHOR, Frame, messagebox, Listbox, END, ACTIVE
from os.path import basename, splitext
import math



class Application(tk.Tk):

    nazev = basename(splitext(basename(__file__.capitalize()))[0])
    nazev = "Kalkulačka absolut"
    


    def __init__(self):

        super().__init__(className=self.nazev)

        self.title(self.nazev)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)        
        self.bind("<Return>", self.insert)


        self.var_field = tk.Variable()


        self.entry_field = tk.Entry(self, textvariable = self.var_field, width = 40)
        self.entry_field.grid(row = 1, column=1, columnspan = 4)
        
        self.listbox = Listbox(self, width = 30)
        self.listbox.grid(row = 2, column = 1, pady = 25, columnspan = 4)
        

        self.frame = Frame(self)
        self.frame.grid(row = 2, column = 5)

        self.btn_up = tk.Button(self.frame, text = "↑", command = self.up, width = 12, border = 5, background = "#555555")
        self.btn_up.pack()

        self.btn_down = tk.Button(self.frame, text = "↓", command = self.down, width = 12, border = 5, background = "#555555")
        self.btn_down.pack()


        self.btn_del = tk.Button(self, text = "Smazat", command = self.del_zasobnik, width = 17, border = 5, background = "#FFFF00")
        self.btn_del.grid(row = 4, column = 3)
        
        self.btn_quit = tk.Button(self, text = "Zavřít", command = self.quit, width = 17, border = 5, background = "#FF0000")
        self.btn_quit.grid(row = 4, column = 4)


        self.zasobnik = []
        self.dvoj_op = {}
        self.dvoj_op["+"] = lambda a, b: a + b
        self.dvoj_op["-"] = lambda a, b: a - b
        self.dvoj_op["*"] = lambda a, b: a * b
        self.dvoj_op["/"] = lambda a, b: a / b
        self.dvoj_op["//"] = lambda a, b: a // b
        self.dvoj_op["**"] = lambda a, b: a ** b

        self.op = {}
        self.op["sin"] = math.sin
        self.op["cos"] = math.cos
        self.op["tg"] = math.tan
        self.op["tan"] = math.tan



    def insert(self, event = None):
        
        raw = self.var_field.get().split()

        if len(raw) == 0:
            pocet = 1

        else:
            pocet = len(raw)

        for i in range(0, pocet):

            if len(raw) == 0:
                messagebox.showerror("Error", "Něco je špatně")

            else:
                polozka = raw[i]

                if polozka == "":
                    messagebox.showerror("Error", "Něco je špatně")

                try:
                    self.zasobnik.append(float(polozka))

                except:
                    pass

                if polozka.upper() == "Q":
                    self.quit()

                if polozka.upper() == "PI":
                    self.listbox.insert(END, math.pi)
                    self.zasobnik.append(math.pi)

                if polozka in self.dvoj_op.keys():

                    if len(self.zasobnik) >= 2:

                        b = self.zasobnik.pop()
                        a = self.zasobnik.pop()
                        self.zasobnik.append(self.dvoj_op[polozka](a, b))
                        self.listbox.insert(END, self.dvoj_op[polozka](a, b))

                    

    def up(self, event = None):

        if self.listbox.get(ACTIVE) != "":

            polozka = self.listbox.curselection()[0]
            self.zasobnik[polozka], self.zasobnik[polozka - 1] = self.zasobnik[polozka - 1], self.zasobnik[polozka]
            self.listbox_reload()
          
            self.listbox.selection_set(polozka - 1)
            self.listbox.activate(polozka - 1)

        else:
            messagebox.showerror("Volba", "Musíte něco vybrat")



    def down(self, event = None):

        if self.listbox.get(ACTIVE) != "":

            polozka = self.listbox.curselection()[0]
            self.zasobnik[polozka], self.zasobnik[polozka + 1] = self.zasobnik[polozka + 1], self.zasobnik[polozka]
            self.listbox_reload()
          
            self.listbox.selection_set(polozka + 1)
            self.listbox.activate(polozka + 1) 

        else:
            messagebox.showerror("Volba", "Musítě něco vybrat")           



    def listbox_reload(self):

        self.var_field.set("")
        self.listbox.delete(0, END)

        for polozka in self.zasobnik:
            self.listbox.insert(END, polozka)

    

    def del_zasobnik(self):

        if self.listbox.get(ANCHOR) != "":

            polozka = self.listbox.curselection()[0]
            self.zasobnik.pop(polozka)
            self.listbox_reload()
        
        else:
            messagebox.showerror("Výběr", "Musíte něco vybrat")



    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()