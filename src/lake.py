from area import *
import random as r

class Lake():

    def __init__(self,polygon):
        polygon = polygon.buffer(0,join_style=3)
        self._polygon = polygon
        self._area = Area(self._polygon, Category.LAKE)

    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

