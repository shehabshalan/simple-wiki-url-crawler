from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from urllib.error import URLError, HTTPError
import sys


def urlFetcher():
    url = sys.argv[1]
    mylist = []
    urlList = []
    try:
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        mylist.append(soup.title.text)
        links = soup.find("div", {"id": "bodyContent"}).findAll(
            "a", href=re.compile(r"[A-Za-z0-9:_()-–.]+"))
        print("================================================")
        print(
            f"YOU ARE NOW CRAWLING | {soup.title.text}")
        for link in links:
            urlList.append(link['href'])
    except HTTPError as err:
        if err.code == 404:
            print("WE HIT 404")
        else:
            raise
    with open('urls.txt', 'w', encoding="utf-8") as urlfile:
        for url in urlList:
            urlfile.write('%s\n' % url)


urlFetcher()
