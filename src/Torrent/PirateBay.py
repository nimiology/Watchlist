import requests
from bs4 import BeautifulSoup

JSON = {}
LIST = []
def GetDetail(LINK):
    LINK_TEXT = requests.get(LINK).text
    BS4 = BeautifulSoup(LINK_TEXT,'html.parser')
    NAME = BS4.find(id = "title").string
    TYPE = BS4.find(title = 'More from this category').string
    FILES = BS4.find(title='Files').string
    DETAIL = BS4.find(class_='col2').text
    UPLOADEDBY = DETAIL[DETAIL.find("By")+5:]
    UPLOADEDBY = UPLOADEDBY[:UPLOADEDBY.find("\n")]
    UPLOADEDDATE = DETAIL[DETAIL.find("Uploaded:") + 11:]
    UPLOADEDDATE = UPLOADEDDATE[:UPLOADEDDATE.find("By") - 1]
    SEEDERS = DETAIL[DETAIL.find("Seeders:") + 9:]
    SEEDERS = int(SEEDERS[:SEEDERS.find("\n")])
    LEECHERS = DETAIL[DETAIL.find("Leechers:") + 10:]
    LEECHERS = int(LEECHERS[:LEECHERS.find("\n")])
    INFOHASH = DETAIL[DETAIL.find("Info Hash:") + 11:]
    INFOHASH = INFOHASH.split()
    INFOHASH = INFOHASH[0]

    NUM = BS4.text.find('Size:')
    SIZE = BS4.text[NUM:NUM+40]
    SIZEE = SIZE.find("(")
    SIZE = SIZE[SIZE.find("Size"):SIZEE]
    SIZE = SIZE[SIZE.find(":")+2:]

    DES = BS4.find("pre").text
    TORRENT_LINK = BS4.find(title="Get this torrent").get("href")


    JSON_GETDETAIL = {"Link":LINK,"Name":NAME,"Type":TYPE,"Files":FILES,
                      "Size":SIZE,"Uploaded by":UPLOADEDBY,"Uploaded Date":UPLOADEDDATE,
                      "Seeders":SEEDERS,"Leechers":LEECHERS,"Info Hash":INFOHASH,"Description":DES,
                      "Magnet Link":TORRENT_LINK}

    LIST.append(JSON_GETDETAIL)

def FINDLINKS(INPUT,page):
    LINK_SEARCH = requests.get(f"https://thepiratebay10.org/search/{INPUT}/{page}/99/200").text
    BS4 = BeautifulSoup(LINK_SEARCH,'html.parser')
    FINDER = BS4.find_all(class_="detLink")
    for LINK in FINDER:
        GetDetail(LINK.get("href"))
    JSON["Links"] = LIST
    return JSON