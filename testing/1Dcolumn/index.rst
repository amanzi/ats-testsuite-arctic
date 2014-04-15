1D Column
=========

Tests
------------------

Input files required to run the tests include the XML provided on each test page and the :download:`mesh <../../testing/1Dcolumn/mesh/mesh_fsets.exo>`. You may have to modify the mesh location specified in the XML file based on your folder configuration. 

.. toctree::
   :maxdepth: 1

   test0
   test1
   test2
   test4
   test7
   
Exodus mesh: :download:`mesh_fsets.exo <../../testing/1Dcolumn/mesh/mesh_fsets.exo>`

Cases
------------------

In each test, multiple cases are evaluated. The cases solve the same physical system, but with increasing numbers of physical processes involved. One or more of the following cases are evaluated for each test:

i) constant specified density, viscosity, no temperature

ii) constant specified temperature, EOS for density, viscosity

iii) adds energy equation, but with no flux bcs, constant initial temp (nearly isothermal)

iv) variation on (iii) which sets a surface rel perm to mimic the coupled surf/subsurf without surf

v) fully coupled surf/subsurf cases

Model
-----

Mesh
----


Schematic
---------

References
----------

About
-----

* Directory: testing/1Dcolumn

* Authors:  Ethan Coon and Dylan Harp

* Maintainer(s): 

Status
------
Add notes here about the status of the test.  

.. todo:: Documentation:
