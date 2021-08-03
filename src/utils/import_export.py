from tkinter import filedialog
from tkinter import Tk
from zipfile import ZipFile
import os

class Export:
    def gui(self):
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        self.ZIP(folder_selected)
    def ZIP(self,dir):
        Obj = ZipFile(f'{dir}/Watchlist.zip', 'w')
        for dirname, subdirs, files in os.walk('Statics'):
            Obj.write(dirname)
            for filename in files:
                Obj.write(os.path.join(dirname, filename))
        Obj.close()
        Obj.write('Statics')
        Obj.close()


