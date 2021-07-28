import os
import time
import json
from tabulate import _table_formats, tabulate
from IMDb import IMDb

json_Dir = "seriesguide.json"

def LISTFORRUN():
    with open(json_Dir, "r") as FILE:
        return json.load(FILE)

def TABEl():
    data = [["Serie Name", "Season"]]
    DICT = LISTFORRUN()
    for key, value in DICT.items():
        data.append([key, value])
    TABLe = tabulate(data, headers='firstrow', showindex='always', tablefmt='fancy_grid')
    return TABLe

Command = '''
1.New
2.Edit
3.Delete
4.Import
5.Export
6.Make Direction

'''

STATUS = True
while STATUS:
    os.system('cls')
    print(TABEl())
    try:
        DO = int(input(Command))
        if DO == 1:
            print('Enter IMDb link: ')
            time.sleep(5)
            os.system('start https://imdb.com')
            Link_IMDb = input('')
            print(IMDb.imdb(Link_IMDb))
            break

        elif DO == 2:
            pass
        elif DO == 3:
            pass
        elif DO == 4:
            pass
        elif DO == 5:
            pass
        elif DO == 6:
            pass
    except:
        print('Just numbers acceptable!')