from tkinter import filedialog
from tkinter import Tk
from zipfile import ZipFile
import os


def gui():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected

def Export():
    Direction = gui()
    Obj = ZipFile(f'{Direction}/Watchlist.zip', 'w')
    for dirname, subdirs, files in os.walk('Statics'):
        Obj.write(dirname)
        for filename in files:
            Obj.write(os.path.join(dirname, filename))
    Obj.close()
    Obj.write('Statics')
    Obj.close()

def Import():
    root = Tk()
    root.withdraw()
    Direction = filedialog.askopenfilename()
    Obj =  ZipFile(Direction, 'r')
    Obj.extractall("")





