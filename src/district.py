from block import *
from field import *
from lake  import *
from street import *
from castle import *
from scipy.spatial import Voronoi, voronoi_plot_2d
from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
import numpy as np
import random as r


SUB_BLOCK_MAX =  35

def _partition_polygon0(poly):
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
        while(nb < SUB_BLOCK_MAX):
            x = r.randint(min_x, max_x)
            y = r.randint(min_y, max_y)
            if (poly.contains(Point(x,y))):
                points.append((x,y))
                nb+=1
        return points

def _get_sub_region0(vor, poly):
    """retrieve regions from voronoi result
    param: vor: voronoi result
    type: vor: list

    param: poly: polygon that delimits the area
    type: Polygon
    """
    regions = [r for r in vor.regions if -1 not in r and len(r) > 0]
    regions = [Polygon([vor.vertices[i] for i in r]) for r in regions]
    return [poly.intersection(r) for r in regions]


class District():
    """district class

        Args:
           polygon: shapely.geometry.Polygon, that describe the district's shape
           has_walls: boolean, specify if the district has walls or not
           has_castle: boolean, specify if the district has a castle or not (one for the whole district)
           has_lake: boolean, specify if the district has a lake or not (one per district)
           has_land: boolean, specify if the district has lands instead of only fields
           has_street: boolean, specify if the district has streets (streets are between districts)
           verbose: prompt infos during construction

    """
    #private:


    def __init__(self,polygon,verbose=False,has_castle=False, has_lake=False, has_land=False, has_street=False):


        self._polygon = polygon
        self._has_lake = has_lake
        self._has_land = has_land
        self._has_street = has_street
        self._has_castle = has_castle

        self._blocks_list = []
        self._lake_list   = []
        self._nb_fields   = 0

        self.block_partition(verbose)

    def block_partition(self,verbose=False):
        """
        Creates blocks inside the district
        """
        points = _partition_polygon0(self._polygon.buffer(-0.5))
        vor = Voronoi(points)
        regions = _get_sub_region0(vor,self._polygon.buffer(-0.5))

        #remplir les listes des différents types de blocks
        #lac: 1 lac une fois sur 3
        #field: 1/3 de champs
        #block: reste

        nb_regions = len(regions)
        already_a_lake        = False
        already_a_castle      = False
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
                if (self._has_castle and not already_a_castle):
                    self._blocks_list.append(Castle(region))
                    already_a_castle = True
                else:
                    put_land = self._has_land and ((index % 2) == 0)
                    self._blocks_list.insert(-1,Block(region, has_land=put_land, verbose=verbose))
            index += 1
        if (self._has_street):
            field  = Field(self._polygon.buffer(-0.5))
            street = Street(self._polygon.buffer(-0.5).exterior.buffer(0.5))
            self._blocks_list.insert(0, street)
            self._blocks_list.insert(0, field)
        else:
            self._blocks_list.insert(0, Field(self._polygon))

    def components(self):
        """Calls all block components"""
        if len(self._blocks_list) > 0:
            return [block.components() for block in self._blocks_list + self._lake_list ]
        else:
            return []




if __name__ == "__main__":
    from shapely.geometry import mapping, Polygon, Point, LineString, MultiPolygon
    import json

    zone = Polygon((2 * np.random.random((8,2)) - 1) * 20 ).convex_hull.buffer(20//2)
    district = District(zone,has_castle=True, has_land=True, has_street=True, verbose=True)
    tools.json(district, '/tmp/district.json')
