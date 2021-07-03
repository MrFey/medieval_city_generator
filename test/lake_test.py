from config import *

if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon((2 * np.random.random((8,2)) - 1) * 20 ).convex_hull.buffer(20//2)
    lake = Lake(zone)
    tools.json(lake, './json_outputs/lake.json')
