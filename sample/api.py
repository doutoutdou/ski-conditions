from scrappers.bromont import parse_bromont
from scrappers.owlhead import parse_owl_head
from scrappers.sutton import parse_sutton
from scrappers.orford import parse_orford


def conditions():
    return [parse_sutton(), parse_bromont(), parse_owl_head(), parse_orford()]

