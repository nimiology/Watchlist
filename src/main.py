import json
import os
import tkinter
from tkinter import *

from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from tabulate import _table_formats, tabulate
from kivy.core.window import Window

DIRECT = []
direct01 = []
MAINLIST = {}
listrer = []
my_listw = []

saveplace = "seriesguide.json"


def LISTFORRUN():
    LISTFORRUN = []
    with open(saveplace, "r") as FILE:
        for line in FILE:
            LISTFORRUN.append(eval(line))
    return LISTFORRUN[len(LISTFORRUN)-1]

try:
    MAINLIST.update(LISTFORRUN())
except:
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))

def save():
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))

def TKINTERSMALL(geometry,title,label,inputwidth,buttontext,X,Y):
    #add name of folders from directory folder
    WINDOW = tkinter.Tk()
    WINDOW.geometry(geometry)
    WINDOW.resizable(False, False)
    WINDOW.title(title)
    LABEL = Label(WINDOW, text=label)
    INPUT = Entry(WINDOW, width=inputwidth)
    BUTTON = Button(WINDOW, text=buttontext)
    LABEL.grid(row=0)
    BUTTON.place(x=X, y=Y)
    INPUT.place(x="5", y="30")

    def bind(event):
        global TXTBIND
        TXTBIND = INPUT.get()
        WINDOW.destroy()

    BUTTON.bind("<ButtonRelease-1>", bind)

    WINDOW.mainloop()
    return TXTBIND

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Lime"
        self.theme_cls.theme_style = "Dark" 
        Window.size = (500, 600)
        return Builder.load_file("UI.kv")

    def DIRECTORY(self):
        #in here we give directory after that this will get
        #name of folders in directory
        TXT = TKINTERSMALL("620x70","Directory","Type your series directory:","100","Confrim","560","25")
        print(TXT)
        DIRECT.append(TXT)
        my_list = os.listdir(DIRECT[len(DIRECT)-1])

        for jojoj in my_list:
            my_listw.append(jojoj)
        for emin in my_listw:
            MAINLIST[emin] = 0
        save()

    def EDIT(self):
        #edit serie
        WINDOW = tkinter.Tk()
        WINDOW.title("Edit")
        WINDOW.geometry("920x670+20+5")

        LISTRUN = LISTFORRUN()
        KEY = []
        VALUE = []

        for key, value in LISTRUN.items():
            VALUE.append(key)
            KEY.append(value)

        for NUMKEY in range(0, len(KEY)):
            LABEL = Label(WINDOW, text="[{0}]  {1}  ".format((NUMKEY + 1), VALUE[NUMKEY]))
            X = "15"
            if (NUMKEY > 21):
                X = "500"
                Y = 10 + (NUMKEY - 22) * 30
                if (NUMKEY > 43):
                    Y = 10 + (NUMKEY - 44) * 30
                    X = "1000"
            else:
                Y = 10 + NUMKEY * 30
            LABEL.place(x=X, y=Y)
        BUTTON1 = Button(WINDOW, text="Edit", width="10")
        BUTTON1.place(x="820", y="620")

        BUTTON2 = Button(WINDOW, text="Delete", width="10")
        BUTTON2.place(x="730", y="620")

        def EDIT(event):
            WINDOW = tkinter.Tk()
            WINDOW.geometry("200x70")
            WINDOW.resizable(False, False)
            WINDOW.title("type")
            LABEL = Label(WINDOW, text="Write series number:")
            INPUT = Entry(WINDOW, width="25")
            BUTTON = Button(WINDOW, text="Confrim")
            LABEL.grid(row=0)
            BUTTON.place(x="140", y="25")
            INPUT.place(x="5", y="30")

            def edit(event):
                NUMSERIE = int(INPUT.get())-1
                numserie1 = NUMSERIE
                seasonupdate = int(TKINTERSMALL("620x70",f"{VALUE[NUMSERIE]}",
                                                f"{VALUE[NUMSERIE]} Season ",
                                                "100","Confrim","560","25"))
                MAINLIST[VALUE[numserie1]] = seasonupdate
                save()


            BUTTON.bind("<ButtonRelease-1>", edit)

        def DELET(event):

            TEXT = NAMESERIE = TKINTERSMALL("620x70","Delete",
                                            "Type number of series which you want to delete(Example:1,2,10):",
                                            "100","Confrim","560","25")
            SPLITER = TEXT.split(",")
            for deleter in SPLITER:
               del MAINLIST[VALUE[int(deleter) - 1]]
               print (MAINLIST)
            save()


        BUTTON1.bind("<ButtonRelease-1>", EDIT)
        BUTTON2.bind("<ButtonRelease-1>", DELET)

        WINDOW.mainloop()

    def TABLE(self):
        #show table
        WINDOW = tkinter.Tk()
        WINDOW.title("Tabel")
        WINDOW.geometry("600x670+5+5")
        data = [["Serie Name", "Season"]]

        DICT=LISTFORRUN()

        for key, value in DICT.items():
            data.append([key,value])

        TABLE=tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid')
        TEXT = tkinter.Text(WINDOW, height=100, width=1000)
        TEXT.pack()
        TEXT.insert(tkinter.END, "{0}".format(TABLE))
        tkinter.mainloop()
        WINDOW.mainloop()

    def NEW(self):
        #in here we add new serie to the table
        NAMESERIE = TKINTERSMALL("620x70","Directory","New series:","100","Confrim","560","25")
        MAINLIST[NAMESERIE] = 0
        save()


MainApp().run()
