from block import *
from field import *
from lake  import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


SUB_BLOCK_MAX =  20

def _partition_polygon0(poly):
        (min_x,min_y,max_x,max_y) = poly.bounds
        nb = 0
        points = []
        (min_x,min_y,max_x,max_y) = (round(min_x), round(min_y),round(max_x), round(max_y))
        while(nb < HOUSES_MAX):
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

    def __init__(self,polygon):
        self._polygon = polygon
        self.block_partition()

    def block_partition(self):
        points = _partition_polygon0(self._polygon)
        vor = Voronoi(points)
        regions = _get_sub_region0(vor,self._polygon)

        #remplir les listes des différents types de blocks
        #lac: 1 lac une fois sur 3
        #field: 1/3 de champs
        #block: reste

        nb_regions = len(regions)
        already_a_lake = False
        already_enough_fields = False

        for region in regions:
            if not already_a_lake and r.randint(0,3 * nb_regions) == 0:
                self._lake_list.append(Lake(region))
                already_a_lake = True

            elif not already_enough_fields:
                self._blocks_list.append(Block(region,has_field=True))
                self._nb_fields += 1
                if (self._nb_fields >= nb_regions//3):
                    already_enough_fields = True
            else:
                self._blocks_list.append(Block(region))

    def components(self):
        if len(self._blocks_list) > 0:
            return [block.components() for block in self._blocks_list + self._lake_list ]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon((2 * np.random.random((8,2)) - 1) * 20 ).convex_hull.buffer(20//2)
    district = District(zone)
    tools.json(district, '/tmp/district.json')
