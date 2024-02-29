import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from skillClass import skill

class LayoutApp:


    def __init__(self, master=None):
        # build ui
        self.osrssim = tk.LabelFrame(master, name="osrssim")
        self.osrssim.configure(
            background="#2d2d2d",
            height=600,
            text='OSRS Sim',
            width=900)

        skillList = ["Attack", "Hitpoints", "Mining", "Strength", "Agility", "Smithing", "Defense", "Herblore", "Fishing", "Ranged", "Thievery", "Cooking", "Prayer", "Crafting", "Firemaking", "Magic", "Fletching", "Woodcutting", "Runecrafting", "Slayer", "Farming", "Construction", "Hunter", "Total level"]

        levels = []
        skills = []

        for x in range(0, 24):
            skillX = skill(100 + x, skillList[x])
            skills.append(skillX)
            levels.append(tk.IntVar())
            levels[x].set(skillX.getLvl())


        self.osrssim = tk.LabelFrame(master, name="osrssim")
        self.osrssim.configure(
            background="#2d2d2d",
            height=600,
            text='OSRS Sim',
            width=900)
        
        

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
                spinX = tk.Spinbox(self.osrssim, from_=0, to=99, increment=1, textvariable=levels[count])
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
                textX.insert(1.0, skills[count].getName())
                textX.config(state=DISABLED)
                count += 1
                texts.append(textX)
        
        line_var = tk.StringVar()

        def submit():
            
            line = line_var.get()
            tkinterscrolledtext2.insert(tk.INSERT, line)

        sub_btn = tk.Button(self.osrssim, text = 'Submit', command = submit)
        sub_btn.place(anchor="nw", x=300, y=525)    

        entry3 = tk.Entry(self.osrssim, textvariable=line_var)
        entry3.place(anchor="nw", relx=.01, rely=0.8, width=650, x=0, y=0)
        entry3.focus_set()


        self.osrssim.pack(side="top")

        # Main widget
        self.mainwindow = self.osrssim

    def run(self):
        self.mainwindow.mainloop()

if __name__ == "__main__":

    root = tk.Tk()
    app = LayoutApp(root)
    app.run()