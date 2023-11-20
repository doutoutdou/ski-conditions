from helpers.scrapper_helper import get_html, default_value
from models.trails import Trails

__url = "https://www.bromontmontagne.com/en/detailed-conditions/"

def parse_bromont():
    bromont_conditions = Trails('bromont')

    content = get_html(__url)

    trail_root = content.find(id="recap-pistes").find("div", class_="etat")
    # take the first
    bromont_conditions.set_opened_trails(default_value(trail_root.find("span", class_="txt-data").get_text()))
    bromont_conditions.set_total_trails(default_value(trail_root.find("span", class_="total").get_text().split("/ ")[1]))

    lift_root = content.find(id="recap-remontes").find("div", class_="etat")
    # take the first
    bromont_conditions.set_opened_chair_lifts(default_value(lift_root.find("span", class_="txt-data").get_text()))
    bromont_conditions.set_total_chair_lifts(default_value(lift_root.find("span", class_="total").get_text().split("/ ")[1]))

    return vars(bromont_conditions)

