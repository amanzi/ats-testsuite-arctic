Arctic Testsuite
=================

This is a series of tests that were developed for Arctic applications, most notably NGEE-Arctic.

Note that these tests are physically relevant, and not necessarily fast.  The 1D tests take approximately 5m on a Mac laptop, the 2D tests take multiple hours on 4 cores on a workstation.

These tests are also the first source of demonstration problems for researchers looking to use ATS for Artic (or just plain freezing) applications.

Running the tests:
------------------

Note that you must have an ATS installation either in your path or with an environment variable defined:
```
$> which ats  # (returns valid ats) OR
$> echo $ATS_DIR  # (returns path to valid ats installation)
```

To run the testsuite for the first time:

```
cd testing
python regression_tests.py -n [TESTSUITE/DIRECTORY]
```

For instance, we recommend you run the 1D tests first through:

```
python regression_tests.py -n 1Dcolumn
```

Afterwards, once all tests have been run with the "-n" (or "new") option, you can re-run and compare to these intial results without any flags:

```
python regression_tests.py 1Dcolumn
```

Individual tests can be run by specifying the full path to the configure file:

```
python regression_tests.py 1Dcolumn/test0/test0.cfg
```

See also:

```
python regression_tests.py --help
```


Testsuite Description
----------------------

Tests are a combination of testX-Y, where X is the test number and Y is a Roman numeral describing the physics of the series.  Note that all tests that share a number should be physically equivalent, though may not be exactly numerically equivalent.

* i) constant specified density, viscosity, no temperature
* ii) constant specified temperature, EOS for density, viscosity
* iii) adds energy equation, but with no flux bcs, constant initial temp (nearly isothermal)
* iv) variation on (iii) which sets a surface rel perm to mimic the coupled surf/subsurf without surf
* v) fully coupled surf/subsurf cases

* test0: steady state, water only
* test1: water source, water only (ic = test0)
* test2: freeze from below, subsurface only (ic = test0)
* test3: cyclic temperature, constant gas saturation BC, subsurface only (ic = test2)
* test4: coupled surface/subsurface, (subsurf ic = test2, surf ic is ponded ice layer), heat surface, melting surface ice, infiltrate into subsurf
* test7: coupled surface/subsurface + SEB

This series is consistent with how Arctic problems are typically run (i.e. Atchley et al GMD 2015).

1. A steady state problem is run to establish a water table (no ice), i.e. test0
2. This water table is frozen from below to establish a totally frozen ice table (i.e. test2).  Steps 1 & 2 are iterated until the frozen ice table is sufficiently close to the surface for the location.
3. Dynamic runs with prescribed MET data are run (test7).