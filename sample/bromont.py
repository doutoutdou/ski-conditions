import requests
from bs4 import BeautifulSoup

from trails import Trails
__url = "https://www.bromontmontagne.com/en/detailed-conditions/"


def parse_bromont():
    bromont_conditions = Trails('bromont')
    page = requests.get(__url)
    content = BeautifulSoup(page.content, "html.parser")

    trail_root = content.find(id="recap-pistes")
    # take the first
    trails = trail_root.find("div", class_="etat")
    bromont_conditions.set_opened_trails(trails.find("span", class_="txt-data").get_text())
    bromont_conditions.set_total_trails(trails.find("span", class_="total").get_text().split("/ ")[1])

    lift_root = content.find(id="recap-remontes")
    # take the first
    lifts = lift_root.find("div", class_="etat")
    bromont_conditions.set_opened_chair_lifts(lifts.find("span", class_="txt-data").get_text())
    bromont_conditions.set_total_chair_lifts(lifts.find("span", class_="total").get_text().split("/ ")[1])

    return vars(bromont_conditions)

