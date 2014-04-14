Steady State 1D Column
======================

Capabilties Tested
------------------
This tests a steady state solve with constant specified density, viscosity, no
temperature.

Background
----------
This file documents ATS code verification of flow simulations 
These codes were compiled using the gfortran compiler on the
Linux environment. 

Model
-----
Boundary Conditions:

1. Constant pressure of 6.21025e+05 Pa along bottome face (z=-45m)

Initial Conditions:

1. Uniform pressure of 6.21025e+05 Pa

Water Retention Model: van Genuchten

Problem Specification
---------------------

Links to download models files:

Input XML: :download:`test0-i.xml <test0-i.xml>`

Exodus mesh: :download:`mesh_fsets.exo <mesh_fsets.exo>`

Schematic
---------

.. figure:: schematic/test0.png
    :figclass: align-center
    :width: 1200 px

.. centered:: **Saturation, head, and temperature along column**

Variables
---------


Results and Comparison
----------------------


References
----------


About
-----

* Directory: testing/test0

* Authors:  Ethan Coon and Dylan Harp

* Maintainer(s): 

* Input Files:

Status
------
Add notes here about the status of the test.  

.. todo:: Documentation:
