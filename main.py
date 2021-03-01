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
listprinti = {}
listrer = []
my_listw = []
lofi = []

saveplace = "seriesguide.txt"

try:
    with open(saveplace, "r") as inf:
        for line in inf:
            lofi.append(eval(line))
        for olp in range(0, (len(lofi))):
            pass
        listprinti.update(lofi[olp])
except:
    with open(saveplace, "+w") as file:
        file.write(json.dumps(listprinti))




class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.theme_style = "Dark" 
        Window.size = (500, 600)
        return Builder.load_file("UI.kv")

    def save(self):
        with open(saveplace, "+w") as file:
            file.write(json.dumps(listprinti))
        toast("SAVED", 7.5)



    class shashooo():
        def goh(self):
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
                    listprinti[my_listw[emin]] = 0

            button.bind("<ButtonRelease-1>", bind)

            window.mainloop()

    class scanning():
        def ab(self):
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
                        listprinti[lumpen[numserie1]] = seasonupdate
                        print(listprinti)

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
                       del listprinti[lumpen[int(deleter)-1]]
                       
                       print (listprinti)
                button.bind("<ButtonRelease-1>", bind)

                window.mainloop()

            buttone.bind("<ButtonRelease-1>", binda)
            button.bind("<ButtonRelease-1>", bindq)

            window1.mainloop()

    class table():
        def joi(self):
            data=[["Serie Name","Season"]]
            window1 = tkinter.Tk()
            window1.title("Tabel")
            window1.geometry("600x670+5+5")
            lofi=[]
            with open(saveplace,"r") as inf:
              for line in inf:
                   lofi.append(eval(line))  
            for olp in range(0,(len(lofi))):
                pass
            lifii=lofi[olp]
            for key, value in lifii.items():
                data.append([key,value])
            x=tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid')
            T = tkinter.Text(window1, height=100, width=1000)
            T.pack()
            T.insert(tkinter.END, "{0}".format(x))
            tkinter.mainloop()
            window1.mainloop()

    class new():
        def obi(self):
            window = tkinter.Tk()
            window.geometry("620x70")
            window.resizable(False, False)
            window.title("New serie")
            label = Label(window, text="New series:")
            entryo = Entry(window, width="100")
            button = Button(window, text="Confrim")
            label.grid(row=0)
            button.place(x="560", y="25")
            entryo.place(x="5", y="30")

            def bind(event):
                di = entryo.get()
                listprinti[di] = 0

            button.bind("<ButtonRelease-1>", bind)
            window.mainloop()



MainApp().run()