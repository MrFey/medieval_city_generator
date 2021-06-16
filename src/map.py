from district import *
from castle   import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


SUB_DISTRICT_MAX =  8

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
    _polygon = None
    _districts_list = []
    _castle = None
    _population = 0
    _has_castle = False;

    def __init__(self,population,verbose=False):
        #TODO: ajuster en fonction du nombre d'habitants
        radius = 200

        self._polygon = Polygon((2 * np.random.random((8,2)) - 1) * 40 ).convex_hull.buffer(40//2)
        self.district_partition(verbose)

    def district_partition(self,verbose=False):
        points = _partition_polygon00(self._polygon)
        print(points)
        vor = Voronoi(points)
        regions = _get_sub_region00(vor,self._polygon)

        nb_regions = len(regions)
        already_a_lake = False
        already_enough_fields = False


        for region in regions:
                if (verbose):
                    print("[+] New District")
                if (not self._has_castle):
                    self._districts_list.append(District(region,verbose=verbose,has_castle=True))
                    self._has_castle = True
                else:
                    self._districts_list.append(District(region,verbose=verbose))

    def components(self):
        if len(self._districts_list) > 0:
            return [district.components() for district in self._districts_list]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    my_map = Map(3000,verbose=True)
    tools.json(my_map, '/tmp/map.json')
