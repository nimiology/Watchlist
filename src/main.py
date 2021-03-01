import json
import os
import tkinter
from tkinter import *

from kivy.config import Config
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.toast import toast
from tabulate import _table_formats, tabulate
from kivy.core.window import Window

direct1 = []
direct01 = []
MAINLIST = {}
listrer = []
my_listw = []

saveplace = "seriesguide.txt"
def LISTFORRUN():
    LISTFORRUN = []
    with open(saveplace, "r") as FILE:
        for line in FILE:
            LISTFORRUN.append(eval(line))
    print(len(LISTFORRUN))
    return LISTFORRUN[0]

try:
    MAINLIST.update(LISTFORRUN())
except:
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))

def save():
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))
    toast("SAVED", 7.5)



class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark" 
        Window.size = (500, 600)
        return Builder.load_file("UI.kv")
    def DIRECTORY(self):
        window = tkinter.Tk()
        window.geometry("620x70")
        window.resizable(False, False)
        window.title("Directory")
        label = Label(window, text="Type your series directory:")
        entryo = Entry(window, width="100")
        button = Button(window, text="Confrim")
        label.grid(row=0)
        button.place(x="560", y="25")
        entryo.place(x="5", y="30")

        def bind(event):
            di = entryo.get()
            direct1.append(di)
            print(direct1)
            we = 0
            for we in range(0, len(direct1)):
                pass
            my_list = os.listdir(direct1[we])
            for jojoj in range(0, len(my_list)):
                my_listw.append(my_list[jojoj])
            for emin in range(0, len(my_listw)):
                MAINLIST[my_listw[emin]] = 0
            save()


        button.bind("<ButtonRelease-1>", bind)

        window.mainloop()


    def EDIT(self):
        window1 = tkinter.Tk()
        window1.title("Edit")
        window1.geometry("920x670+20+5")
        lofi = []
        with open(saveplace, "r") as inf:
            for line in inf:
                lofi.append(eval(line))
        for mozi in range(0, (len(lofi))):
            pass
        lifii = lofi[mozi]
        lumpenn = []
        lumpen = []
        for key, value in lifii.items():
            lumpen.append(key)
            lumpenn.append(value)
        for kokoqe in range(0, len(lumpenn)):
            mo = Label(window1, text="[{0}]  {1}  ".format((kokoqe + 1), lumpen[kokoqe]))
            print(len(lifii))
            moz = "15"
            if (kokoqe > 21):
                moz = "500"
                aw = 10 + (kokoqe - 22) * 30
                if (kokoqe > 43):
                    aw = 10 + (kokoqe - 44) * 30
                    moz = "1000"
            else:
                aw = 10 + kokoqe * 30
            mo.place(x=moz, y=aw)
        buttone = Button(window1, text="Edit", width="10")
        buttone.place(x="820", y="620")
        button = Button(window1, text="Delete", width="10")
        button.place(x="730", y="620")

        def binda(event):
            windowq = tkinter.Tk()
            windowq.geometry("200x70")
            windowq.resizable(False, False)
            windowq.title("type")
            label = Label(windowq, text="Write series number:")
            entryoq = Entry(windowq, width="25")
            button = Button(windowq, text="Confrim")
            label.grid(row=0)
            button.place(x="140", y="25")
            entryoq.place(x="5", y="30")

            def edit(event):
                numserie= int(entryoq.get())-1
                windowedit = tkinter.Tk()
                windowedit.geometry("620x70")
                windowedit.resizable(False, False)
                windowedit.title("{0}".format(lumpen[numserie]))
                label = Label(windowedit, text="{0}.Season ".format(lumpen[numserie]))
                entryo = Entry(windowedit, width="100")
                buttonqq = Button(windowedit, text="Confrim")
                label.grid(row=0)
                buttonqq.place(x="560", y="25")
                entryo.place(x="5", y="30")
                def confrim(event):
                    numserie1 = numserie
                    seasonupdate = int(entryo.get())
                    MAINLIST[lumpen[numserie1]] = seasonupdate
                    print(MAINLIST)

                buttonqq.bind("<ButtonRelease-1>", confrim)
                windowedit.mainloop()

            button.bind("<ButtonRelease-1>", edit)

        def bindq(event):
            window = tkinter.Tk()
            window.geometry("620x70")
            window.resizable(False, False)
            window.title("Delete")
            label = Label(window, text="Type number of series which you want to delete(Example:1,2,10):")
            entryo = Entry(window, width="100")
            button = Button(window, text="Confrim")
            label.grid(row=0)
            button.place(x="560", y="25")
            entryo.place(x="5", y="30")

            def bind(event):
                die = entryo.get()
                jodakonnande=die.split(",")
                for deleter in jodakonnande:
                   del MAINLIST[lumpen[int(deleter) - 1]]

                   print (MAINLIST)
            button.bind("<ButtonRelease-1>", bind)

            window.mainloop()

        buttone.bind("<ButtonRelease-1>", binda)
        button.bind("<ButtonRelease-1>", bindq)

        window1.mainloop()

    def TABLE(self):

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
        WINDOW = tkinter.Tk()
        WINDOW.geometry("620x70")
        WINDOW.resizable(False, False)
        WINDOW.title("New serie")

        LABEL = Label(WINDOW, text="New series:")
        INPUT = Entry(WINDOW, width="100")
        BUTTON = Button(WINDOW, text="Confrim")
        LABEL.grid(row=0)
        BUTTON.place(x="560", y="25")
        INPUT.place(x="5", y="30")

        def bind(event):
            NAMESERIE = INPUT.get()
            MAINLIST[NAMESERIE] = 0
            save()

        BUTTON.bind("<ButtonRelease-1>", bind)
        WINDOW.mainloop()



MainApp().run()