from area import *
import random as r

class land():

    """
    Land class
    Args:
        polygon: shapely.geometry.Polygon, that describe the lands's shape
    """
    
    def __init__(self,polygon):
        
        self._polygon = polygon
        self._area = Area(self._polygon, Category.LAND)

    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

