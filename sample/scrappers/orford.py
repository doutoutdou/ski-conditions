import requests
from bs4 import BeautifulSoup

from models.trails import Trails

__url = "https://montorford.com/en-ca/winter/conditions-ski"


def parse_orford():
    orford_conditions = Trails('orford')
    page = requests.get(__url)
    content = BeautifulSoup(page.content, "html.parser")

    trails_root = (content.find("span", string="Trails")
                   .parent
                   .find("span", class_="values")
                   )

    orford_conditions.set_opened_trails(trails_root.find("span", class_="opened").get_text())
    orford_conditions.set_total_trails(trails_root.find("span", class_="total").get_text().split("/ ")[1])

    lifts_root = (content.find("span", string="Chairlifts")
                  .parent
                  .find("span", class_="values")
                  )

    orford_conditions.set_opened_chair_lifts(lifts_root.find("span", class_="opened").get_text())
    orford_conditions.set_total_chair_lifts(lifts_root.find("span", class_="total").get_text().split("/ ")[1])

    return vars(orford_conditions)
