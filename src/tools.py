from shapely.geometry import mapping
from collections import Iterable
import fiona
import os
def json_write(obj,stream_writer):
    if (not isinstance(obj,Iterable)): #on peut plus iterer = c'est un polygon
        stream_writer.write({
            'geometry': mapping(obj._polygon),
            'properties': {'category': obj._category.value},
        })
    else:
        for co in obj:
            json_write(co,stream_writer)

def json(what, filename,verbose=False):
    """
    Export in the json format any class that has a components() method
    """
    if os.path.exists(filename):
        os.remove(filename)
    if (verbose):
        print("[*] exporting json...")
    schema = {
        'geometry': 'Polygon',
        'properties': {'category': 'int'},
    }
    with fiona.open(filename, 'w', 'GeoJSON', schema) as c:
        json_write(what.components(),c)
