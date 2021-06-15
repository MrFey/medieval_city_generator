from house import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


HOUSES_MAX = 40

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
    return [r for r in regions if poly.contains(r) ]


class Block():

    #private:
    _polygon = None
    _house_list = []



    def __init__(self,polygon):
        self._polygon = polygon
        self.house_partition() # Réparti la liste des maisons en fonction du polygone

    def house_partition(self):
        points = _partition_polygon(self._polygon)
        vor = Voronoi(points)
        regions = _get_sub_region(vor,self._polygon)

        #Pour le moment toutes les maisons ont un jardin
        self._house_list = [House(region, False, 180) for region in regions]


    def components(self):
        if len(self._house_list) > 0:
            return [house.components() for house in self._house_list]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    shape = Polygon([(0,0), (400,0), (150,150), (-50,100)])
    block = Block(shape)
    print(block.components())
    tools.json(block, '/tmp/block.json')
