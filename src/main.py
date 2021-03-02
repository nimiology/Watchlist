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
icon = "SeriesGuide.ico"

def LISTFORRUN():
    LISTFORRUN = []
    with open(saveplace, "r") as FILE:
        for line in FILE:
            LISTFORRUN.append(eval(line))
    return LISTFORRUN[len(LISTFORRUN)-1]

def save():
    with open(saveplace, "+w") as file:
        file.write(json.dumps(MAINLIST))

def TKINTERSMALL(geometry,title,label,inputwidth,buttontext,X,Y):
    #Tkinter for str
    windoww = tkinter.Tk()
    windoww.wm_iconbitmap(icon)
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


def EDIT():
    #split key and value
    LISTRUN = LISTFORRUN()
    KEY = []
    VALUE = []
    for key, value in LISTRUN.items():
        VALUE.append(key)
        KEY.append(value)
    #gui
    WINDOWEDIT = tkinter.Tk()
    WINDOWEDIT.geometry("225x70")
    WINDOWEDIT.resizable(False, False)
    WINDOWEDIT.wm_iconbitmap(icon)
    WINDOWEDIT.title("Edit")
    LABEL = Label(WINDOWEDIT, text="Type series number:")
    INPUT = Entry(WINDOWEDIT, width="35")
    LABEL.grid(row=0)
    INPUT.place(x="5", y="30")
    def edit():
        NUMSERIE = int(INPUT.get())
        numserie1 = NUMSERIE

        seasonupdate = int(TKINTERSMALL("620x70",f"{VALUE[NUMSERIE]}",
                                        f"{VALUE[NUMSERIE]} Season ",
                                        "100","Confrim","555","27"))
        MAINLIST[VALUE[numserie1]] = seasonupdate
        WINDOWEDIT.destroy()
        save()
        setTextInput(TABEl())

    BUTTON = Button(WINDOWEDIT, text="Confrim",command=edit)
    BUTTON.place(x="163", y="27")




def DELET():
    LISTRUN = LISTFORRUN()
    KEY = []
    VALUE = []
    for key, value in LISTRUN.items():
        VALUE.append(key)
        KEY.append(value)
    try:
        TEXT = TKINTERSMALL("620x70","Delete",
                                "Type number of series which you want to delete(Example:1,2,10):",
                                "100","Confrim","555","27")
        SPLITER = TEXT.split(",")
        for deleter in SPLITER:
           del MAINLIST[VALUE[int(deleter) ]]
           print (MAINLIST)
        save()
        setTextInput(TABEl())
    except:
        pass

def TABEl():
    data = [["Serie Name", "Season"]]
    DICT = LISTFORRUN()
    for key, value in DICT.items():
        data.append([key, value])
    TABLe = tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid')
    return TABLe

def NEW():
    #in here we add new serie to the table
    TXT = TKINTERSMALL("620x70", "New serie", "New series:"
                       , "100", "Confrim", "555", "27")
    try:
        DIRECT.append(TXT)
        my_list = os.listdir(DIRECT[len(DIRECT)-1])

        for jojoj in my_list:
            my_listw.append(jojoj)
        for emin in my_listw:
            MAINLIST[emin] = 0
        save()
        setTextInput(TABEl())
    except:
        try:
            MAINLIST[TXT] = 0
            save()
            setTextInput(TABEl())
        except:
            pass

def setTextInput(text):
    TEXTTABLE.delete(1.0, "end")
    TEXTTABLE.insert(1.0, text)


try:
    MAINLIST.update(LISTFORRUN())
except:
    save()

#main page
WINDOW = tkinter.Tk()
WINDOW.wm_iconbitmap(icon)
WINDOW.resizable(False, False)
WINDOW.geometry('1100x650')
WINDOW.title("Tabel")
TEXTTABLE = tkinter.Text(WINDOW,height=40.4, width=70)
TEXTTABLE.grid(column=0)
TEXTTABLE.insert(tkinter.END, f"{TABEl()}")
BUTTON0 = Button(WINDOW, text="New" ,height=12, width=70,command=NEW)
BUTTON1 = Button(WINDOW, text='Edit',height=12, width=70,command=EDIT)
BUTTON2 = Button(WINDOW, text='Delet',height=12, width=70,command=DELET)
BUTTON0.place(x=580,y=16)
BUTTON1.place(x=580,y=226)
BUTTON2.place(x=580,y=431)
WINDOW.mainloop()
