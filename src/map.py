from district import *
from castle   import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


def _partition_polygon00(poly, nb_district):
        """Split a Polygon into sub polygons

           param: poly: polygon that delimits the area
           type: Polygon

           param: nb_district: number of districts we want
           type: int
        """
        (min_x,min_y,max_x,max_y) = poly.bounds
        nb = 0
        points = []
        (min_x,min_y,max_x,max_y) = (round(min_x), round(min_y),round(max_x), round(max_y))
        while(nb < (nb_district * 2) + 3):
            x = r.randint(min_x, max_x)
            y = r.randint(min_y, max_y)
            if (poly.contains(Point(x,y))):
                points.append((x,y))
                nb+=1
        return points

def _get_sub_region00(vor, poly):
    """retrieve regions from voronoi result
    param: vor: voronoi result
    type: vor: list

    param: poly: polygon that delimits the area
    type: Polygon
    """
    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]
    return [poly.intersection(r) for r in regions]


class Map():
    """map class

          Args:
             population: int, determine the density and the size of the map
             has_walls: boolean, specify if the map has walls or not
             has_castle: boolean, specify if the map has a castle or not (one for the whole map)
             has_lake: boolean, specify if the map has a lake or not (one per district)
             has_land: boolean, specify if the map has lands instead of only fields
             has_street: boolean, specify if the map has streets (streets are between districts)
             verbose: prompt infos during construction

    """
    #private:

    def __init__(self, population=5000, has_walls=False, has_castle=False, has_lake=False, has_land=False, has_street=False, verbose=False):
        #TODO: ajuster en fonction du nombre d'habitants
        radius = 100

        self._has_walls = has_walls
        self._has_castle = has_castle
        self._has_lake = has_lake
        self._has_land = has_land
        self._has_street = has_street

        self._walls      = []
        self._population = 0
        self._districts_list = []
        self._polygon = Polygon((2 * np.random.random((8,2)) - 1) * radius ).convex_hull.buffer(radius//2)

        self._nb_districts = (population // 1500) + 1

        self.district_partition(verbose=verbose)

    def district_partition(self,verbose=False):
        """"split the map into districts

        param: verbose: prompt infos or not

        type: verbose: boolean, optional

        """
        points = _partition_polygon00(self._polygon, self._nb_districts)
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
                    self._districts_list.append(District(region,
                                                         verbose=verbose,
                                                         has_castle=True,
                                                         has_lake=self._has_lake,
                                                         has_street=self._has_street,
                                                         has_land=self._has_land))
                    already_a_castle = True
                else:
                    self._districts_list.insert(-1,District(region,
                                                            verbose=verbose,
                                                            has_lake=self._has_lake,
                                                            has_land=self._has_land,
                                                            has_street=self._has_street,
                                                            has_castle=False))

    def components(self):
        """Calls all districts components"""
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
