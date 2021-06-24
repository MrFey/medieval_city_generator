from district import *
from castle   import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


SUB_DISTRICT_MAX =  7

def _partition_polygon00(poly):
        (min_x,min_y,max_x,max_y) = poly.bounds
        nb = 0
        points = []
        (min_x,min_y,max_x,max_y) = (round(min_x), round(min_y),round(max_x), round(max_y))
        while(nb < SUB_DISTRICT_MAX):
            x = r.randint(min_x, max_x)
            y = r.randint(min_y, max_y)
            if (poly.contains(Point(x,y))):
                points.append((x,y))
                nb+=1
        return points

def _get_sub_region00(vor, poly):
    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]
    return [poly.intersection(r) for r in regions]


class Map():

    #private:
    _polygon    = None
    _districts_list = []
    _population = 0
    _has_castle = False
    _has_walls  = False
    _has_lake   = False
    _has_land = False
    _walls      = []

    def __init__(self, population=5000, has_walls=False, has_castle=False, has_lake=False, has_land=False, verbose=False):
        #TODO: ajuster en fonction du nombre d'habitants
        radius = 40

        self._has_walls = has_walls
        self._has_castle = has_castle
        self._has_lake = has_lake
        self._has_land = has_land

        self._polygon = Polygon((2 * np.random.random((8,2)) - 1) * radius ).convex_hull.buffer(radius//2)
        self.district_partition(verbose=verbose)

    def district_partition(self,verbose=False):
        points = _partition_polygon00(self._polygon)
        print(points)
        vor = Voronoi(points)
        regions = _get_sub_region00(vor,self._polygon)

        nb_regions = len(regions)
        already_a_lake = False
        already_enough_fields = False


        if (self._has_walls):
            self._walls = Area(MultiPolygon(regions).buffer(1, join_style=4),Category.WALL)

        already_a_castle = False
        for region in regions:
            if (verbose):
                print("[+] New District")
                if (self._has_castle and not already_a_castle):
                    self._districts_list.append(District(region,verbose=verbose,has_castle=True, has_lake=self._has_lake))
                    already_a_castle = True
                else:
                    self._districts_list.insert(-1,District(region,verbose=verbose,has_lake=self._has_lake, has_land=self._has_land))

    def components(self):
        if len(self._districts_list) > 0:
            res = [district.components() for district in self._districts_list]
            if (self._has_walls):
                res = [self._walls.components()] + res
            return res
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    my_map = Map(3000,has_walls=True,has_lake=True,verbose=True,has_castle=True, has_land=True)
    tools.json(my_map, '/tmp/map.json')
    print("There are %d districts" %len(my_map._districts_list))
