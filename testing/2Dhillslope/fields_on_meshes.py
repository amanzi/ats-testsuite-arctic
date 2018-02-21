
# coding: utf-8

# In[1]:


import os,sys
sys.path.append("S:/mo8557/ats/repos/ats-dev/tools/utils")

import matplotlib

import numpy as np
from matplotlib import pyplot as plt
import h5py

import parse_ats 
import transect_data
import mesh

# run something on your mesh
#
# - must be the same mesh
# - must be the same partitioning
#  (mpiexec -n YY meshconvert --partition --partition-method=2 --classify ...)
# - must be the same stratigraphy

xyz = mesh.meshElemCentroids(directory="./test7/run16_11Oct17")
print xyz

# 3100 cells by 3 dimensions (x,y,z)
xyz.shape
print xyz[0,:]
print xyz[1,:]

dat, map = transect_data.transect_data(["base_porosity",], keys=0, directory="./test7/run16_11Oct17", return_map=True)
keys, times, dataset = parse_ats.readATS(directory="./test7/run16_11Oct17")

print dat.shape # (2 + # of varaiables, # of timesteps, NX, NZ)
NX = dat.shape[2]
NZ = dat.shape[3]
x = dat[0,0,:,:]
z = dat[1,0,:,:]

# plot to see what is going on
#fig, ax = plt.subplots(1,1)
#transect_data.plot(dataset['base_porosity.cell.0']['0'][:][0,:], ax, directory="./test7/run16_11Oct17")
#plt.show()

# depth coordinate
# z of the top surface elevation
z_surface = z[:,-1] + 0.01

depth = np.expand_dims(z_surface,1) - z
print "%8.16e"%z[0,-2]
print z[0,:]
print z_surface[0]
print depth[0,:]

porosity = np.zeros((NX,NZ),'d')
porosity_mapped = np.zeros((NX*NZ,),'d')
for i in range(NX):
    for j in range(NZ):
        if abs(dat[2,0,i,j] - 0.65) < 1.e-6:
            porosity[i,j] = 0.75
        elif abs(dat[2,0,i,j] - 0.45) < 1.e-6:
            pass
        # elif abs(dat[2,0,i,j] - 0.75) < 1.e-6: # do for each material type       
        else:
            raise RuntimeError("you screwed up your if statements")
        
# map the data back into unstructured order
for i in range(NX):
    for j in range(NZ):
        porosity_mapped[map[i,j]] = porosity[i,j]

# write this data into a file for use with ATS
#
# times : array of times [s] on which the data is defined
# ['base_porosity.cell.0'], ['permeability.cell.0'], ....  (key part is .cell.0, but prefer to use our names)
# within each data, ['0'], ['1'], ... ['LEN_TIMES-1'] : data groups
with h5py.File("soil_params.h5", 'w') as soil_h5:
    times = np.array([0.,],'d')
    soil_h5.create_dataset('time', data=times)
    poro = soil_h5.create_group("base_porosity.cell.0")
    poro.create_dataset('0', data=porosity_mapped)
#    perm = soil_h5.create_group("permeability.cell.0")
 #   perm.create_dataset('0', data=perm_mapped)

    
    


#       <ParameterList name="base_porosity" type="ParameterList">
#         <Parameter name="field evaluator type" type="string" value="independent variable from file" />
#         <Parameter name="filename" type="string" value="soil_params.h5" />
#         <Parameter name="variable name" type="string" value="base_porosity" />
#         <Parameter name="constant in time" type="bool" value="true" />
#       </ParameterList>
