from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    city = City(5000, has_walls=True, has_castle=True, has_lake=False, has_land=True, has_street=True)
    tools.json(city, './json_outputs/city_final.json',verbose=False)


