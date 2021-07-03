from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon((2 * np.random.random((8,2)) - 1) * 20 ).convex_hull.buffer(20//2)
    district = District(zone)
    tools.json(district, './json_outputs/district.json')


    district = District(zone, has_lake=True)
    tools.json(district, './json_outputs/district_lake.json')


    district = District(zone, has_street=True)
    tools.json(district, './json_outputs/district_street.json')


    district = District(zone, has_castle=True)
    tools.json(district, './json_outputs/district_castle.json')
