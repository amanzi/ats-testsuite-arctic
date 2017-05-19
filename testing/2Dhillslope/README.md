2Dhillslope TESTS
=================

This is a series of tests that used to test an idelized slope using 36 yr driver data from Nome, Alaska, NGEE-Arctic.

Here we outline the order required to simulate non-vegetated and vegetated 2Dhillslope. 

NOTE, to start running these tests we need to produce a 1Dcolumn profile using ats_meshing tools and output from 1Dbotflux/test7. The ../init/hillslope_column_test7_1.h5 is column file that produced from 1Dbotflux test. 

Steps:
------------------

Non-vegetated hillslope
1. Run test7 by initializing pressuwres and tempratures from 1D colunm and copying them over entire slope 
2. The test7_seepage uses spinup results from test7 as an initial condition. This test is a transient test that runs using meteorological data from Nome.

Vegetated hillslope <br>
3. When Step 1 is finished go to restarts folder and run make 'make_veg_data.py'. <br>
4. Setting vegetation parameters: when run Test10 using produced during Step3 file as input. <br>
5. Running test7 coupled with vegetation: when Test10 is completed, run Test11. <br>

