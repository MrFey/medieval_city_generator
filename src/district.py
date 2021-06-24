from block import *
from field import *
from lake  import *
from street import *
from castle import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


SUB_BLOCK_MAX =  25

def _partition_polygon0(poly):
        (min_x,min_y,max_x,max_y) = poly.bounds
        nb = 0
        points = []
        (min_x,min_y,max_x,max_y) = (round(min_x), round(min_y),round(max_x), round(max_y))
        while(nb < SUB_BLOCK_MAX):
            x = r.randint(min_x, max_x)
            y = r.randint(min_y, max_y)
            if (poly.contains(Point(x,y))):
                points.append((x,y))
                nb+=1
        return points

def _get_sub_region0(vor, poly):
    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]
    return [poly.intersection(r) for r in regions]


class District():

    #private:
    _polygon = None
    _blocks_list = []
    _lake_list   = []
    _nb_fields   = 0
    _has_castle  = False
    _has_lake    = False
    _has_land  = False

    def __init__(self,polygon,verbose=False,has_castle=False, has_lake=False, has_land=False):
        self._polygon = polygon
        self._has_lake = has_lake
        self._has_land = has_land
        self.block_partition(verbose,has_castle=has_castle)

    def block_partition(self,verbose=False,has_castle=False):
        points = _partition_polygon0(self._polygon)
        vor = Voronoi(points)
        regions = _get_sub_region0(vor,self._polygon)

        #remplir les listes des différents types de blocks
        #lac: 1 lac une fois sur 3
        #field: 1/3 de champs
        #block: reste

        nb_regions = len(regions)
        already_a_lake = False
        already_enough_fields = True #If we want more field (normaly not useful)

        index = 0
        for region in regions:
            if not already_a_lake and self._has_lake:
                self._lake_list.append(Lake(region))
                already_a_lake = True

            elif not already_enough_fields:
                self._blocks_list.append(Block(region,has_field=True))
                self._nb_fields += 1
                if (self._nb_fields >= nb_regions//3):
                    already_enough_fields = True
            else:
                if (verbose):
                    print("[+] New Block")
                if (has_castle and not self._has_castle):
                    self._blocks_list.append(Castle(region))
                    self._has_castle = True
                else:
                    put_land = self._has_land and ((index % 2) == 0)
                    self._blocks_list.insert(-1,Block(region, has_land=put_land, verbose=verbose))
            index += 1
        self._blocks_list.insert(0, Field(self._polygon))

    def components(self):
        if len(self._blocks_list) > 0:
            return [block.components() for block in self._blocks_list + self._lake_list ]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon((2 * np.random.random((8,2)) - 1) * 20 ).convex_hull.buffer(20//2)
    district = District(zone,has_castle=True, has_land=True)
    tools.json(district, '/tmp/district.json')
