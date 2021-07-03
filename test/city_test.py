from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    mycity = City(3000)
    tools.json(mycity, './json_outputs/city.json')


    mycity = City(3000, has_lake=True)
    tools.json(mycity, './json_outputs/city_lake.json')


    mycity = City(3000, has_street=True)
    tools.json(mycity, './json_outputs/city_street.json')


    mycity = City(3000, has_castle=True)
    tools.json(mycity, './json_outputs/city_castle.json')

    mycity = City(3000, has_land=True)
    tools.json(mycity, './json_outputs/city_land.json')


    mycity = City(3000, has_walls=True)
    tools.json(mycity, './json_outputs/city_walls.json')
