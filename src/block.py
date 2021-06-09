from house import *


class Block():

    #private:
    _polygon = None
    _house_list = []


    def __init__(self,polygon):
        self._polygon = polygon
        house_partition() # Réparti la liste des maisons en fonction du polygone




    def house_partition(self, polygon):


    def components(self):
        if len(self._house_list) > 0:
            return [house.components() for house in _house_list]
        else:
            return []
