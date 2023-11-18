from bromont import parse_bromont
from owlhead import parse_owl_head
from sutton import parse_sutton


def conditions():
    return [parse_sutton(), parse_bromont(), parse_owl_head()]
