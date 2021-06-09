import tools

class City:
    def __init__(self, population, density=10000, has_walls=False, has_castel=False, has_river=False):
        self.population = population
        self.density = density   # 10 000 ha/km2 par dÃ©faut mais peut baisser Ã  2000 ha/km2 avec les champs et monter Ã  30000 ha/km2
        self.has_walls = has_walls
        self.has_castel = has_castel
        self.has_river = has_river
        self.districts = []
        ...

if __name__ == "__main__":
    city = City(5000)
    tools.json(city, '/tmp/city.json')