from area import *
import random as r

class Castle():

    def __init__(self,polygon):
        """
        Castle class
        Args:
            polygon: shapely.geometry.Polygon, that represents the castle's shape
        """
        self._polygon = polygon
        self._area = Area(self._polygon, Category.CASTLE)
        self._walls = Area(self._polygon.buffer(-0.3, join_style=2).exterior.buffer(0.3, join_style=2),Category.WALL)


    def components(self):
        return [self._area.components(), self._walls.components()]

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id


if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    shape = Polygon([(0,0), (10,0), (15,15), (-5,10)])
    castle = Castle(shape)
    tools.json(castle, '/tmp/castle.json')
