from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon([(0,0), (10,0), (15,15), (-5,10)])
    zone = zone.buffer(-1).exterior.buffer(1)
    house = House(zone, False, 0)
    tools.json(house, './json_outputs/house.json')
