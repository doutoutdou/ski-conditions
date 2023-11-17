import requests
from bs4 import BeautifulSoup

from trails import Trails

__url = "https://montsutton.com/en/the-mountain/ski-conditions/"


def parse_sutton():
    sutton_conditions = Trails()
    page = requests.get(__url)
    content = BeautifulSoup(page.content, "html.parser")

    trails = content.find("div", class_="icon_btn icon_track")
    # print(trails)

    for elt in trails.parent:
        # example : <h3>0/60</h3>
        if str(elt).startswith('<h3>'):
            trail_information = elt.get_text().strip().split("/")
            print(trail_information[0])
            print(trail_information[1])
        #     print(elt, end="\n" * 2)



    # print()
    # for trails in tracks:
    #     print(trails, end="\n" * 2)

