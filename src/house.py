import area
import random as r


class House():

    #private:
    _population = 0
    _has_garden = False
    _polygon = None
    _area = None
    _direction = 0

    #public:

    def __init__(self,polygon,has_garden,direction=0):
        self._polygon = polygon
        self._has_garden = has_garden
        self._area = Area(self._polygon, Category.HOUSE)
        self._population = r.randint(1,6) # on suppose un nombre aleatoire du nombre d'habitant entre 1 et 6
        self._direction = direction % 360

        if (self._has_garden):
            self._area.split((r.random() % 0.4), direction)


    def components(self):
        return self._area.components()

    def get_id():
         return Area._last_id



