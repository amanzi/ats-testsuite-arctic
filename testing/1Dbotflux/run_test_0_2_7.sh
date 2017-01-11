#!/bin/bash
#!/bin/sh
# Before running this scrip make sure that all dependencies in initial conditions holds correctly

cd ../
test0i=1Dbotflux/test0/test0-i.regression.gold
test0ii=1Dbotflux/test0/test0-ii.regression.gold
test2=1Dbotflux/test2/test2-iii.regression.gold
test7=1Dbotflux/test7/test7-v.regression.gold

if [ -d "$test0ii" ]; then
  # Control will enter here if $DIRECTORY exists.
  echo "Deleting" $test0i "and" $test0ii
  rm -rf $test0i
  rm -rf $test0ii
fi
if [ -d "$test2" ]; then
  echo "Deleting" $test2
  rm -rf $test2
fi
if [ -d "$test7" ]; then
  echo "Deleting" $test7
  rm -rf $test7
fi

echo "Running test0..."
python regression_tests.py -e $ATS_DIR/bin/ats -n 1Dbotflux/test0/test0.cfg

echo "Copy intial file to the restarts"
cp 1Dbotflux/test0/test0-ii.regression.gold/checkpoint00001.h5 1Dbotflux/restarts/test0-ii_checkpoint00001.h5

echo "Running test2..."
python regression_tests.py -e $ATS_DIR/bin/ats -n 1Dbotflux/test2/test2.cfg

echo "Running test7.. "
python regression_tests.py -m `which mpiexec` -e $ATS_DIR/bin/ats -n 1Dbotflux/test7/test7.cfg

cd 1Dbotflux
