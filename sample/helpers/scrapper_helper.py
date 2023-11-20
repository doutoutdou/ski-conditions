import requests
from bs4 import BeautifulSoup


def get_html(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")


def default_value(value):
    return value or "0"
