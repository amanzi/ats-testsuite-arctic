# ELM Hillslope test
This test is devoted to the simplified hillslope exmaple that can be generilized for the ELM model parametrization

1. Create hillslope_2D.exo by follwoing steps in the [hillslope_mesh.ipynb](https://github.com/amanzi/ats-testsuite-arctic/blob/master/testing/ELM-hillslope/mesh/hillslope_mesh.ipynb) ipython notebook file
2. To partition the mesh use [mesh_partition.sh](https://github.com/amanzi/ats-testsuite-arctic/blob/master/testing/ELM-hillslope/mesh/mesh_partition.sh) script. Before running the scipt create folder '4'.
3. First we create 1D column using script from Step 1. 
4. To convert xml files from previous ATS version use the corresponding xml sciprt from [tools/input_converter](https://github.com/amanzi/ats/tree/master/tools/input_converters). For example to convert 0.86 file to 0.87 type: python $ATS_SRC_DIR/tools/input_converters/xml-0.86-0.87.py file1 -o file2
5. tests in 1D folder allows to build a 1D input file (subsurface water table, temperature distribution, and SEB) for 2D and 3D problems.

### 1D column runs
6. <strong>test0</strong> sets the water table depth that can be maupulted by changing the lower boundary pressure (Richards only). Navigate to 1D folder, create a folder "test0.regression", cd into that folder and run ATS: `$ATS_DIR/bin/ats --xml_file="../test0_0.88.xml"`
7. <strong>test2</strong> runs coupled hydrothermal condition. Here the temperature boundary conditions can be manipulated. In addition, freezing conditions force water table to move up (i.e. re-establishing water table). Note, that initial conditions come from test0.  
8. <strong>test7</strong> runs coupled hydrothermal condition with surface energy balance (SEB). Again, initial conditions come from test2. 
9. Once test7 is finished use the conversion script 1D/make-column-for-2D.sh to create a 1D column file. Created 1D column stored in 2D/init. 

### 2D hillslope runs
10. Column h5 file from init/ folder used to initilize 2D hillslope model. To equilibrate subsurface conditions for the 2D case we spinup the model using simplified meteoroligical data from Step 8. To run paraller version of the model create spin.regression folder, `cd` to it and type: `mpirun -n 4 $ATS_DIR/bin/ats --xml_file="../hillslope.xml"` 
