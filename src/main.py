import json
import os
import tkinter
from tkinter import *
from tabulate import _table_formats, tabulate


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

def save():
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))


try:
    MAINLIST.update(LISTFORRUN())
except:
    save()



def TKINTERSMALL(geometry,title,label,inputwidth,buttontext,X,Y):
    #Tkinter for str
    windoww = tkinter.Tk()
    windoww.geometry(geometry)
    windoww.resizable(False, False)
    windoww.title(title)
    LABEL = Label(windoww, text=label)
    INPUT = Entry(windoww, width=inputwidth)
    BUTTON = Button(windoww, text=buttontext)
    LABEL.grid(row=0)
    BUTTON.place(x=X, y=Y)
    INPUT.place(x="5", y="30")

    def bind(event):
        global TXTBIND
        TXTBIND = INPUT.get()
        windoww.quit()
        windoww.destroy()

    BUTTON.bind("<ButtonRelease-1>", bind)

    windoww.mainloop()
    return TXTBIND

def DIRECTORY():
    #in here we give directory after that this will get
    #name of folders in directory
    try:
        TXT = TKINTERSMALL("620x70","Directory","Type your series directory:"
                           ,"100","Confrim","555","27")
        print(TXT)
        DIRECT.append(TXT)
        my_list = os.listdir(DIRECT[len(DIRECT)-1])

        for jojoj in my_list:
            my_listw.append(jojoj)
        for emin in my_listw:
            MAINLIST[emin] = 0
        save()
    except:
        pass

def EDIT():
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
            try:
                seasonupdate = int(TKINTERSMALL("620x70",f"{VALUE[NUMSERIE]}",
                                                f"{VALUE[NUMSERIE]} Season ",
                                                "100","Confrim","555","27"))
                MAINLIST[VALUE[numserie1]] = seasonupdate
                save()
            except:
                pass


        BUTTON.bind("<ButtonRelease-1>", edit)

    def DELET(event):
        try:
            TEXT = NAMESERIE = TKINTERSMALL("620x70","Delete",
                                            "Type number of series which you want to delete(Example:1,2,10):",
                                            "100","Confrim","555","27")
            SPLITER = TEXT.split(",")
            for deleter in SPLITER:
               del MAINLIST[VALUE[int(deleter) - 1]]
               print (MAINLIST)
            save()
        except:
            pass


    BUTTON1.bind("<ButtonRelease-1>", EDIT)
    BUTTON2.bind("<ButtonRelease-1>", DELET)

    WINDOW.mainloop()
def TABEl():
    data = [["Serie Name", "Season"]]
    DICT = LISTFORRUN()
    for key, value in DICT.items():
        data.append([key, value])
    TABLe = tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid')
    return TABLe
def NEW():
    #in here we add new serie to the table
    try:
        NAMESERIE = TKINTERSMALL("620x70","Directory","New series:"
                                 ,"100","Confrim","555","27")
        MAINLIST[NAMESERIE] = 0
        save()
        print("fuck error")
    except:
        pass

def TABEL():
    def setTextInput(text):
        TEXT.delete(1.0, "end")
        TEXT.insert(1.0, text)
    #show table
    WINDOW = tkinter.Tk()
    WINDOW.resizable(False, False)
    WINDOW.geometry('1100x650')
    WINDOW.title("Tabel")
    TEXT = tkinter.Text(WINDOW,height=40, width=70)
    TEXT.grid(column=0)
    TEXT.insert(tkinter.END, f"{TABEl()}")
    BUTTON0 = Button(WINDOW, text="New" ,height=12, width=70,command=NEW)
    BUTTON1 = Button(WINDOW, text='Edit',height=12, width=70,command=lambda:setTextInput(TABEl()))
    BUTTON2 = Button(WINDOW, text='Delet',height=12, width=70)
    BUTTON0.place(x=580,y=15)
    BUTTON1.place(x=580,y=225)
    BUTTON2.place(x=580,y=425)
    WINDOW.mainloop()



TABEL()
