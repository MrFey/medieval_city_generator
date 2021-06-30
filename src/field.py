from area import *
import random as r

class Field():

    def __init__(self,polygon):
        """
         field class

         Args:
             polygon: shapely.geometry.Polygon, that describe the field's shape
         """
        self._polygon = polygon
        self._area = Area(self._polygon, Category.FIELD)

    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

