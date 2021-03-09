from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import re
import os


def StartSerch():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search/", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("img", {"class": "mimg"})

    for item in links:
        try:
            img_obj = requests.get(item.attrs['src'])
            title = item.attrs['src'].split('/')[-1]
            title = re.sub('[/\,.?=:()""]', '', title)
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./" + dir_name + "/" + title + '.jpeg', img.format)
            except:
                print('Could not save image.')
        except:
            print("Could not request image.")
