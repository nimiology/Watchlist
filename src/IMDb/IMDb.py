import requests
from bs4 import BeautifulSoup
from imdb import IMDb

info = {}

def saverposter(link, DIRCOVER):
    response = requests.get(link)
    file = open(DIRCOVER, "wb")
    file.write(response.content)
    file.close()



def imdb(LINK):

    req = requests.get(LINK).text
    BS= BeautifulSoup(req,"lxml")
    try:
        SERIEORFILM = BS.find_all(class_='button_panel navigation_panel')
        SERIEORFILM = SERIEORFILM[0]
        Series = True
    except:
        Series = False


    info['Series'] = Series

    LINK = LINK[LINK.find("title"):]
    ID = LINK[LINK.find("tt")+2:]
    ID = ID[:ID.find("/")]

    imdb = IMDb()
    film = imdb.get_movie(ID)

    for i in sorted(film.keys()):
        #print(f"{i} = {film[i]}")
        info[i] = []
        listname = info[i]
        try:
            for name in film[i]:
                listname.append(name['name'])
        except:
            listname.append(str(film[i]))

    COVER_DIR = f'Statics/Covers/{ID}.jpg'
    saverposter(film['full-size cover url'], COVER_DIR)
    info['COVER'] = COVER_DIR


    return info