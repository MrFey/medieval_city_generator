from area import *
import random as r

class Field():

    #private:
    _polygon = None
    _area = None

    #public:

    def __init__(self,polygon):
        self._polygon = polygon
        self._area = Area(self._polygon, Category.FIELD)

    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

