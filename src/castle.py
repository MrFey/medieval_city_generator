from area import *
import random as r

class Castle():

    #private:
    _polygon = None
    _area = None
    _walls = None

    #public:

    def __init__(self,polygon):
        self._polygon = polygon
        self._area = Area(self._polygon, Category.CASTLE)
        self._walls = Area(self._polygon.buffer(1, join_style=4),Category.WALL)


    def components(self):
        return [self._walls.components(), self._area.components()]

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

