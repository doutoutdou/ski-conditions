from .bromont import parse_bromont
from .orford import parse_orford
from .owlhead import parse_owl_head
from .sutton import parse_sutton

_conditions = []


# retrieve conditions for every mountain and save it
def scrap():
    global _conditions
    _conditions = [parse_bromont(), parse_orford(), parse_owl_head(), parse_sutton()]


# return conditions previously retrieved
def get_conditions():
    return _conditions
