import requests
from bs4 import BeautifulSoup
from imdb import IMDb

info = {}
def saverposter(link):
    response = requests.get(link)
    DIRCOVER = "searcher/poster.jpg"
    file = open(DIRCOVER, "wb")
    file.write(response.content)
    file.close()

def poster(BS):
    POSTER = BS.find_all(class_='poster')
    POSTER = POSTER[0].a.get("href")
    POSTER = f"https://www.imdb.com/{POSTER}"
    POSTERSITE = requests.get(POSTER).text
    POSTERBS = BeautifulSoup(POSTERSITE, 'lxml')
    POSTER = POSTERBS.find_all(class_='MediaViewerImagestyles__PortraitImage-sc-1qk433p-0 bnaOri')
    POSTER = POSTER[0].get("src")
    return POSTER



def imdb(LINK):

    req = requests.get(LINK).text
    BS= BeautifulSoup(req,"lxml")
    POSTER = poster(BS)
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
    saverposter(POSTER)
    return info