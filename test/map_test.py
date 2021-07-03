from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    mymap = Map(3000)
    tools.json(mymap, './json_outputs/map.json')


    mymap = Map(3000, has_lake=True)
    tools.json(mymap, './json_outputs/map_lake.json')


    mymap = Map(3000, has_street=True)
    tools.json(mymap, './json_outputs/map_street.json')


    mymap = Map(3000, has_castle=True)
    tools.json(mymap, './json_outputs/map_castle.json')

    mymap = Map(3000, has_land=True)
    tools.json(mymap, './json_outputs/map_land.json')


    mymap = Map(3000, has_walls=True)
    tools.json(mymap, './json_outputs/map_walls.json')


    mymap = Map(3000, has_walls=True,has_lake=True,has_castle=True, has_land=True)
    tools.json(mymap, './json_outputs/map_full.json')
