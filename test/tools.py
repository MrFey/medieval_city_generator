from shapely.geometry import mapping
from collections import Iterable
import fiona

def json_write(obj,stream_writer):
    print(obj,isinstance(obj,Iterable),"\n")
    if (not isinstance(obj,Iterable)): #on peut plus iterer = c'est un polygon
        stream_writer.write({
            'geometry': mapping(obj._polygon),
            'properties': {'category': obj._category.value},
        })
    else:
        for co in obj:
            json_write(co,stream_writer)

def json(what, filename):
    schema = {
        'geometry': 'Polygon',
        'properties': {'category': 'int'},
    }
    with fiona.open(filename, 'w', 'GeoJSON', schema) as c:
        json_write(what.components(),c)
