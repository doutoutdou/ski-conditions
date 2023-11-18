import requests
from bs4 import BeautifulSoup

from trails import Trails

__url = "https://owlshead.com/conditions-de-ski/"


def parse_owl_head():
    owl_head_conditions = Trails('owl head')
    page = requests.get(__url)
    content = BeautifulSoup(page.content, "html.parser")

    trails = (content.find("h4", string="Pistes ouvertes")
              .parent
              .find("div", class_="text p-large")
              .get_text()
              .split("/"))

    owl_head_conditions.set_opened_trails(trails[0])
    owl_head_conditions.set_total_trails(trails[1])

    lifts = (content.find("h4", string="Télésièges ouverts")
             .parent
             .find("div", class_="text p-large")
             .get_text()
             .split("/"))

    owl_head_conditions.set_opened_trails(lifts[0])
    owl_head_conditions.set_total_trails(lifts[1])

    return vars(owl_head_conditions)
