import requests
from bs4 import BeautifulSoup

from trails import Trails
__url = "https://montsutton.com/en/the-mountain/ski-conditions/"


def parse_sutton():
    sutton_conditions = Trails('sutton')
    page = requests.get(__url)
    content = BeautifulSoup(page.content, "html.parser")

    trails = content.find("div", class_="icon_btn icon_track")

    for elt in trails.parent:
        # example : <h3>0/60</h3>
        if str(elt).startswith('<h3>'):
            trail_information = elt.get_text().strip().split("/")
            sutton_conditions.set_opened_trails(trail_information[0])
            sutton_conditions.set_total_trails(trail_information[1])
            break

    lifts = content.find("div", class_="icon_btn icon_lift")

    for elt in lifts.parent:
        # example : <h3>0/60</h3>
        if str(elt).startswith('<h3>'):
            lift_information = elt.get_text().strip().split("/")
            sutton_conditions.set_opened_chair_lifts(lift_information[0])
            sutton_conditions.set_total_chair_lifts(lift_information[1])
            break

    return vars(sutton_conditions)
