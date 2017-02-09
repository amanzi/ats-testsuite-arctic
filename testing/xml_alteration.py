"""
USAGE:

from amanzi_xml.utils import io
test2iii = io.fromFile("1Dbotflux/test2/test2-iii.xml")
test2iii_m = xml_alteration.gen_empty(test2iii)
for k in test2iii_m.keys():
    test2iii_m[k][:] = soil[k][:]
io.toFile(test2iii, "1Dbotflux/test2/test2-organic.xml")
"""


import sys,os
sys.path.append(os.path.join(os.environ['AMANZI_SRC_DIR'],'tools','amanzi_xml'))

from amanzi_xml.utils import search

to_get = [  ("wrm", "water retention evaluator/WRM parameters"),
            ("base_porosity", "base_porosity/function"),
            ("porosity", "porosity/compressible porosity model parameters"),
            ("permeability", "permeability/function"),
            ("thermal_conductivity", "thermal conductivity evaluator/thermal conductivity parameters"),
            ("density_rock", "density_rock/function"),
         ]


def get_masters(xml):
    """Gets the top level lists of a given xml"""
    masters = dict()
    for key,item in to_get:
        try:
            masters[key] = search.generateElementByNamePath(xml, item).next()
        except StopIteration:
            pass

    return masters

def gen_empty(xml):
    masters = get_masters(xml)
    for key,item in to_get:
        if masters.has_key(key):
            masters[key][:] = list()
    return masters


                

