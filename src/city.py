import tools
from map import *

class City():

    _map = None

    def __init__(self, population, density=10000, has_walls=False, has_castle=False, has_lake=False, has_land=False,has_street=False, verbose=False):

        self.population = population
        self.density = density   # 10 000 ha/km2 par dÃ©faut mais peut baisser Ã  2000 ha/km2 avec les champs et monter Ã  30000 ha/km2
        self.has_walls = has_walls
        self.has_castle = has_castle
        self.has_lake = has_lake
        self.has_land = has_land
        self.has_street = has_street

        while (1):
            try:
                self._map =  Map(population=population,
                              has_walls=has_walls,
                              has_castle=has_castle,
                              has_lake=has_lake,
                              has_land=has_land,
                              has_street=has_street,
                              verbose=verbose)
                if (len(self._map._districts_list) <= 0):
                    continue
                break
            except:
                if (verbose):
                    print("[-] Oops an error occured, retrying...")
                continue


    def components(self):
            return [self._map.components()]

if __name__ == "__main__":
    city = City(5000,verbose=True, has_walls=True, has_castle=True, has_lake=False, has_land=True, has_street=True)
    tools.json(city, '/tmp/city.json',verbose=True)
