from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon([(0,0), (10,0), (15,15), (-5,10)])
    field = Field(zone)
    tools.json(field, './json_outputs/field.json')
