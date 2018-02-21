
import sys,os

sys.path.append(os.path.join(os.environ['ATS_SRC_DIR'],'tools','meshing_ats'))
sys.path.append('/home/u1/mo8557/ats/seacas/seacas_install/lib')
import meshing_ats

import numpy as np
from matplotlib import pyplot as plt

x_0 = 0
x_break = 150
x_max = 600
dx = 10
nx = np.round((x_max - x_0) / dx)

z_0 = 40
slope_1 = 0.02  # 2% slope
slope_2 = 0.1

# hopefully this doesn't change
x = np.linspace(x_0,x_max,nx+1) # domain 600 m long with 600 nodes (dx = 1m)
z1 = z_0 + np.arange(x_0, x_break+dx/2, dx) * slope_1
z2 = z1[-1] + np.arange(0, x_max-x_break+dx/2, dx) * slope_2

print len(z1), len(z2)
z = np.concatenate([z1,z2[1:]],axis=0)

print x, z
print len(x),len(z)
#plt.plot(x,z, 'b-x')

m2 = meshing_ats.Mesh2D.from_Transect(x,z)

#Changing organic layer thickness by defining a variable dz_layer1
def dz_layer1(s):
    if s<100: #RIP zone
        thickness=2 # meters
    elif ((100<=s)&(s<=200)): # transition zone
        thickness=2-0.018*(s-100) # meters, transitions from 2 m to 0.2 m
    else: #hillslope
        thickness=0.2 # meters
    return thickness

z_bottom_organic = z - np.array([dz_layer1(xs) for xs in x])
#plt.plot(x,z, 'b-x')
#plt.plot(x,z_bottom_organic, 'r-x')



# layer extrusion for 2D
layer_types = []
layer_data = []
layer_ncells = []
layer_mat_ids = []

# 50 x 2cm cells, labeled according to dz function
ncells1 = 50
dz1 = 0.02
ncells2 = 25
dz2 = 0.04

# need centroids for top 2m
centroid_depths1 = np.arange(dz1/2.0, ncells1*dz1, dz1)
centroid_depths2 = centroid_depths1[-1] + dz1/2 + np.arange(dz2/2.0, ncells2*dz2, dz2)
centroid_depths = np.concatenate([centroid_depths1, centroid_depths2], axis=0)
plt.scatter(np.zeros(centroid_depths1.shape), centroid_depths1, color='b')
plt.scatter(np.zeros(centroid_depths2.shape), centroid_depths2, color='r')
#plt.show()


# layer 1: top meter
for i in range(ncells1):
    layer_types.append('constant') #organic
    layer_data.append(dz1)
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
for i in range(ncells1,ncells1+ncells2):
	layer_types.append('constant') #mineral
	layer_data.append(dz2)
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

m3 = meshing_ats.Mesh3D.extruded_Mesh2D(m2, layer_types,layer_data, layer_ncells, layer_mat_ids)
m3.write_exodus("hillslope_organic_layerbyid.exo")
# $AMANZI_TPLS_DIR/bin/meshconvert ./hillslope_organic_layerbyid.exo hillslope_organic_layerbyid2.exo



# make a column doing the same thing
# --------------------------------------------------------------------------------
x = np.array([0,1])
z = np.array([0,0])
m2 = meshing_ats.Mesh2D.from_Transect(x,z)

# layer extrusion
layer_types = []
layer_data = []
layer_ncells = []
layer_mat_ids = []

layer_types.append("constant")
layer_data.append(0.5)
layer_ncells.append(25)
layer_mat_ids.append(1001)

layer_types.append("constant")
layer_data.append(0.5)
layer_ncells.append(25)
layer_mat_ids.append(1002)

layer_types.append("constant")
layer_data.append(1)
layer_ncells.append(25)
layer_mat_ids.append(1002)

# layer 3: expanding domain, all mineral
ncells = 15
dz = 0.04
for i in range(ncells):
    dz *= 1.2
    layer_types.append("constant")
    layer_data.append(dz)
    layer_ncells.append(1)
    layer_mat_ids.append(1002)

for i in range(4):
    dz *= 2
    layer_types.append("constant")
    layer_data.append(dz)
    layer_ncells.append(1)
    layer_mat_ids.append(1002)

layer_types.append('node')
layer_data.append(40 - sum(layer_data)) # total depth of domain is 40 m
layer_ncells.append(2)
layer_mat_ids.append(1002)

m3 = meshing_ats.Mesh3D.extruded_Mesh2D(m2, layer_types, 
                                        layer_data, 
                                        layer_ncells, 
                                        layer_mat_ids)
m3.write_exodus("hillslope_column.exo")
