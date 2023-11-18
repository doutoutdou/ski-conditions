from bromont import parse_bromont
from sutton import parse_sutton


def conditions():
    return [parse_sutton(), parse_bromont()]
