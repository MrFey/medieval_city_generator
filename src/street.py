from area import *
import random as r

class Street():

    #private:
    _polygon = None
    _area = None

    #public:

    def __init__(self,polygon):
        self._polygon = polygon
        self._area = Area(self._polygon, Category.STREET)

    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id

