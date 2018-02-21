
import sys,os

sys.path.append(os.path.join(os.environ['ATS_SRC_DIR'],'tools','meshing_ats'))
sys.path.append('/home/u1/mo8557/ats/seacas/seacas_install/lib')
import meshing_ats2

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
#matplotlib inline

# 600m long hillslope: shallow section 150m long at 2% slope, steep section 450m long at 10% slope
x = np.linspace(0,600,600) # domain 600 m long with 600 nodes (dx = 1m)
z1 = np.linspace(40,43,150) # domain 150 m long with 150 nodes (dx = 1m) where slope is 2%
z2 = np.linspace(43.1,88,450) # domain 450 m long with 450 nodes (dx = 1m) where slope is 10%
z = np.concatenate([z1,z2],axis=0) # concatenate the two sections of hillslope


print x, z
print len(x),len(z)
m2 = meshing_ats2.Mesh2D.from_Transect(x,z)

#Changing organic layer thickness by defining a variable dz_layer1
def dz_layer1(s):
    if s<100: #RIP zoe
        thickness=2 # meters
    elif ((100<=s)&(s<=200)): # transition zone
        thickness=-2-0.018*(s-100) # meters, transitions from 2 m to 0.2 m
    else: #hillslope
        thickness=0.2 # meters
    return thickness
	
# layer extrusion for 2D
layer_types = []
layer_data = []
layer_ncells = []
layer_mat_ids = []

# 50 x 2cm cells, labeled according to dz function
ncells = 50
dz = 0.02

centroid_depths = np.arange(dz/2.0, ncells*dz, dz)
# layer 1: top meter
for i in range(ncells):
    layer_types.append('constant') #organic
    layer_data.append(dz)
    layer_ncells.append(1)

    # labeling in the top meter varies across the domain
    layer_mat_ids1 = np.zeros((len(x)-1,),'d')
    for j in range(len(x)-1):
        if centroid_depths[i] < dz_layer1(x[j]):
            layer_mat_ids1[j] = 1001
        else:
            layer_mat_ids1[j] = 1002
    layer_mat_ids.append(layer_mat_ids1)

# layer 2: second meter
ncells = 25
dz = 0.04
for i in range(ncells):
	layer_types.append('constant') #mineral
	layer_data.append(dz)
	layer_ncells.append(1)
	
	# labeling varies within this domain as well
	layer_mat_ids2 = np.zeros((len(x)-1,),'d')
	for j in range(len(x)-1):
		if centroid_depths[i] < dz_layer1(x[j]):
			layer_mat_ids2[j] = 1001
		else:
			layer_mat_ids2[j] = 1002
	layer_mat_ids.append(layer_mat_ids2)

# layer 3: expanding domain, all mineral
ncells = 15
dz = 0.04
for i in range(ncells):
    dz *= 1.2
    layer_types.append("constant")
    layer_data.append(dz)
    layer_ncells.append(1)
    layer_mat_ids.append(1002*np.ones((len(x)-1,)))

for i in range(4):
    dz *= 2
    layer_types.append("constant")
    layer_data.append(dz)
    layer_ncells.append(1)
    layer_mat_ids.append(1002*np.ones((len(x)-1,)))
    
layer_types.append('node')
layer_data.append(40 - sum(layer_data)) # total depth of domain is 40 m
layer_ncells.append(2)
layer_mat_ids.append(1002*np.ones((len(x)-1,)))

#print layer_data
#print np.array([layer_data, np.cumsum(np.array(layer_data)), layer_mat_ids]).transpose()
#print layer_mat_ids
#print len(layer_mat_ids)
#print sum(layer_ncells)

m3 = meshing_ats2.Mesh3D.extruded_Mesh2D(m2, layer_types,layer_data, layer_ncells, layer_mat_ids)
m3.write_exodus("hockeystick_02Nov17.exo")
# $AMANZI_TPLS_DIR/bin/meshconvert ./hillslope_organic_layerbyid.exo hillslope_organic_layerbyid2.exo
