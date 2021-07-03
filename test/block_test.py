from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon([(0,0), (10,0), (15,15), (-5,10)])
    block = Block(zone)
    tools.json(block, './json_outputs/block.json')


    block = Block(zone, has_field=True)
    tools.json(block, './json_outputs/block_field.json')


    block = Block(zone, has_land=True)
    tools.json(block, './json_outputs/block_land.json')
