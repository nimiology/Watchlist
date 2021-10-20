import json
import os
import tkinter
from tkinter import *
from tabulate import _table_formats, tabulate
from pathlib import Path



DIRECT = []
direct01 = []
Main_Dict = {}
listrer = []
my_listw = []

saveplace = "seriesguide.json"
icon = "SeriesGuide.ico"

def LISTFORRUN():
    LISTFORRUN = []
    with open(saveplace, "r") as FILE:
        return json.load(FILE)


def save():
    with open(saveplace, "+w") as file:
        file.write(json.dumps(Main_Dict))


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
        Main_Dict[VALUE[numserie1]] = seasonupdate
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
           del Main_Dict[VALUE[int(deleter)]]
           print (Main_Dict)
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
            Main_Dict[emin] = 0
        save()
        setTextInput(TABEl())
    except:
        try:
            Main_Dict[TXT] = 0
            save()
            setTextInput(TABEl())
        except:
            pass


def setTextInput(text):
    entry_1.delete(1.0, "end")
    entry_1.insert(1.0, text)


try:
    Main_Dict.update(LISTFORRUN())
except:
    save()

#main page

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x400")
window.configure(bg = "#231F20")


canvas = Canvas(
    window,
    bg = "#231F20",
    height = 400,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    25.0,
    30.0,
    670.0,
    305.0,
    fill="#C03755",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png")
)
entry_bg_1 = canvas.create_image(
    352.0,
    162.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=33.0,
    y=25.0,
    width=638.0,
    height=273.0
)
entry_1.insert(tkinter.END, f"{TABEl()}")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    bg = "#231F20",
    highlightthickness=0,
    command=lambda: DELET(),
    relief="flat"
)
button_1.place(
    x=436.0,
    y=325.0,
    width=104.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    bg = "#231F20",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: EDIT(),
    relief="flat"
)
button_2.place(
    x=164.0,
    y=325.0,
    width=104.0,
    height=46.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    bg = "#231F20",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: NEW(),
    relief="flat"
)
button_3.place(
    x=303.0,
    y=325.0,
    width=104.0,
    height=46.0
)
window.resizable(False, False)
window.mainloop()

