from area import *
import random as r

class House():

    #public:

    def __init__(self,polygon,has_garden,direction=0):
        """
        house class

        Args:
            polygon: shapely.geometry.Polygon, that describe the house's shape
            has_garden: boolean that specify either the house has a garden or not
            direction: int that specify the house's orientation

        """

        self._polygon = polygon
        self._has_garden = has_garden
        self._area = Area(self._polygon, Category.HOUSE)
        self._population = r.randint(1,6) # on suppose un nombre aleatoire du nombre d'habitant entre 1 et 6
        self._direction = direction % 360

        if (self._has_garden):
            self._area.split((r.randint(6, 9)) / 10.0, direction)


    def components(self):
        return self._area.components()

    def get_area(self):
        return self._area


    @staticmethod
    def get_id():
        return Area._last_id




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    shape = Polygon([(0,0), (10,0), (15,15), (-5,10)])
    house = House(shape, True, 180)
    tools.json(house, '/tmp/house_class.json')


