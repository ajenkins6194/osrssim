import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from classes.skill import skill
from classes.interpreter import interpreter

class LayoutApp:


    def __init__(self, master=None):
        # build ui
        self.osrssim = tk.LabelFrame(master, name="osrssim")
        self.osrssim.configure(
            background="#2d2d2d",
            height=600,
            text='OSRS Sim',
            width=900)

        self.skillList = ["Attack", "Hitpoints", "Mining", "Strength", "Agility", "Smithing", "Defense", "Herblore", "Fishing", "Ranged", "Thievery", "Cooking", "Prayer", "Crafting", "Firemaking", "Magic", "Fletching", "Woodcutting", "Runecrafting", "Slayer", "Farming", "Construction", "Hunter", "Total level"]

        self.levels = []
        self.skills = []

        for x in range(0, 24):
            skillX = skill(100 + x, self.skillList[x])
            self.skills.append(skillX)
            self.levels.append(tk.IntVar())
            self.levels[x].set(skillX.level)
        
        self.levels[1].set(10)
        self.skills[1].level = 10

        self.total_level = 0
        self.updateTotal()
        self.levels[23].set(self.total_level)


        self.osrssim = tk.LabelFrame(master, name="osrssim")
        self.osrssim.configure(
            background="#2d2d2d",
            height=600,
            text='OSRS Sim',
            width=900)
        
        words = open("csv.txt", 'r').read()
        interp = interpreter(words)


        panedwindow7 = tk.PanedWindow(self.osrssim, orient="vertical")
        panedwindow7.configure(
            background="#2d2d2d",
            borderwidth=10,
            height=600,
            opaqueresize=True,
            proxyrelief="flat",
            relief="flat",
            sashcursor="arrow",
            width=900)
        panedwindow7.grid(column=0, row=0)
        tkinterscrolledtext2 = ScrolledText(self.osrssim)
        tkinterscrolledtext2.place(
            anchor="nw",
            height=450,
            relx=.01,
            rely=.01,
            x=0,
            y=0)

        spins = []

        ## create spinboxes and set level         

        count = 0
        for t in range(0, 8):
            for i in range(0, 3):
                spinX = tk.Spinbox(self.osrssim, from_=0, to=99, increment=1, textvariable=self.levels[count])
                spinX.place(
                    anchor="nw",
                    height=40,
                    relx=.76,
                    rely=.01,
                    width=40,
                    x=(i * 75),
                    y=(t * 75) + 20)
                spins.append(spinX)
                count += 1
                      
        texts = []

        count = 0
        for t in range(0, 8):
            for i in range(0, 3):
                textX = tk.Text(self.osrssim, font=("Arial", 7))
                textX.configure(height=10, width=50)
                textX.place(anchor="nw", height=15, relx=0.76, width=40, x=(i * 75), y=(t * 75))
                textX.insert(1.0, self.skills[count].getName())
                textX.config(state=DISABLED)
                count += 1
                texts.append(textX)
        
        line_var = tk.StringVar()

        def submit():
            

            line = line_var.get()
            tkinterscrolledtext2.insert(tk.INSERT, ("( %s )\n" % (line)))

            entry3.delete(0, 'end')

            req = req_button_val.get()


            cmd = interp.interpret(line, req)

            msg = self.skills[cmd[0]].processCmd(cmd)
            self.levels[cmd[0]].set(self.skills[cmd[0]].level)

            self.updateTotal()
            self.levels[23].set(self.total_level)

            tkinterscrolledtext2.insert(tk.INSERT, msg)

        self.osrssim.bind('<Return>', self.enter_press)        

        sub_btn = tk.Button(self.osrssim, text = 'Submit', command = submit)
        sub_btn.bind('<Button-1>', self.enter_press)
        sub_btn.place(anchor="nw", x=300, y=525)

         

        entry3 = tk.Entry(self.osrssim, textvariable=line_var)
        entry3.place(anchor="nw", relx=.01, rely=0.8, width=650, x=0, y=0)
        entry3.focus_set()

        req_button_val = IntVar()
        req_button = tk.Checkbutton(self.osrssim, text= "Check Lvl Requirements",
                                    variable = req_button_val,
                                    onvalue = 1,
                                    offvalue = 0)

        req_button.place(anchor="nw",
                         x=375,
                         y=525)

        self.osrssim.pack(side="top")

        # Main widget
        self.mainwindow = self.osrssim

    def updateTotal(self):
        self.total_level = 0
        for x in range (0,23):
            self.total_level += self.skills[x].level

    def enter_press(self, event):
        print("enter")

    def run(self):
        self.mainwindow.mainloop()



if __name__ == "__main__":

    root = tk.Tk()
    app = LayoutApp(root)
    app.run()