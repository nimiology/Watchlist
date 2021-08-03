import os

def mkdir(Directory, Name, Seasons, icon=''):
    Parent_Folder = f"{Directory}/{Name}"
    try:
        os.mkdir(Parent_Folder)
    except:
        print(f"[Error] '{Name}' already exists!")
    for i in range(Seasons):
        Child_Folder = f'{Parent_Folder}/{Name} {i + 1}'
        try:
            os.mkdir(Child_Folder)
        except:
            print(f"[Error] '{Name}/{Name} {i + 1}' already exists!")