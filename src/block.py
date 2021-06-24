from house import *
from land import *
from field import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


HOUSES_MAX = 61

def _partition_polygon(poly):
        (min_x,min_y,max_x,max_y) = poly.bounds
        nb = 0
        points = []
        while(nb < HOUSES_MAX):
            x = r.randint(round(min_x), round(max_x))
            y = r.randint(round(min_y), round(max_y))
            if (poly.contains(Point(x,y))):
                points.append((x,y))
                nb+=1
        return points

def _get_sub_region(vor, poly):
    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]
    return [poly.intersection(r) for r in regions]


class Block():

    #private:
    _polygon = None
    _sub_block_list = []
    _has_field = False
    _has_land = False



    def __init__(self,polygon,has_field=False, has_land=False, verbose=False):
        self._polygon = polygon
        self._has_field = has_field
        self._has_land = has_land
        self.house_partition(verbose) # Réparti la liste des maisons en fonction du polygone

    def house_partition(self,verbose=False):
        points = _partition_polygon(self._polygon)
        vor = Voronoi(points)
        regions = _get_sub_region(vor,self._polygon)

        #Pour le moment toutes les maisons ont un jardin
        index = 0
        for region in regions:
            if (verbose):
                print("[+] New House")
            if self._has_field and index % 2 == 0:
                self._sub_block_list.append(Field(region))
            else:
                region = region.buffer(-0.5).exterior.buffer(0.3)
                self._sub_block_list.append(House(region, False, 180))
            index += 1
        if (self._has_land):
            self._sub_block_list.insert(0,land(self._polygon))

        else:
            self._sub_block_list.insert(0,Field(self._polygon))


    def components(self):
        if len(self._sub_block_list) > 0:
            return [house.components() for house in self._sub_block_list]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    shape = Polygon([(0,0), (400,0), (150,150), (-50,100)])
    block = Block(shape,has_land=True)
    tools.json(block, '/tmp/block.json')
