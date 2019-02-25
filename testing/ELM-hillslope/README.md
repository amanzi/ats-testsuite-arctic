# ELM Hillslope test
This test is devoted to the simplified hillslope exmaple that can be generilized for the ELM model parametrization

1. Create hillslope_2D.exo by follwoing steps in the [hillslope_mesh.ipynb](https://github.com/amanzi/ats-testsuite-arctic/blob/master/testing/ELM-hillslope/mesh/hillslope_mesh.ipynb) ipython notebook file
2. To partition the mesh use [mesh_partition.sh](https://github.com/amanzi/ats-testsuite-arctic/blob/master/testing/ELM-hillslope/mesh/mesh_partition.sh) script. Before running the scipt create folder '4'.
3. First we create 1D column using script from Step 1. 
4. To convert xml files from previous ATS version use the corresponding xml sciprt from https://github.com/amanzi/ats/tree/master/tools/input_converters. For example to convert 0.86 file to 0.87 type: python $ATS_SRC_DIR/tools/input_converters/xml-0.86-0.87.py file1 -o file2
5. tests in 1D folder allows to build a 1D input file (subsurface tter table, temperature distribution, and SEB) for 2D and 3D problems.


