#!/bin/bash
#!/bin/sh
cd ../
test0i=2Dhillslope/test0/test0-i.regression.gold
test0ii=2Dhillslope/test0/test0-ii.regression.gold
test2=2Dhillslope/test2/test2-iii.regression.gold
if [ -d "$test0ii" ]; then
  # Control will enter here if $DIRECTORY exists.
  echo "Deleting" $test0i "and" $test0ii
  rm -rf $test0i
  rm -rf $test0ii
fi
if [ -d "$test2" ]; then
  # Control will enter here if $DIRECTORY exists.
  echo "Deleting" $test2
  rm -rf $test2
fi

echo "Running test0..."
python regression_tests.py -e $ATS_DIR/bin/ats -n 2Dhillslope/test0/test0.cfg

echo "Copy intial file to the restarts"
cp 2Dhillslope/test0/test0-ii.regression.gold/checkpoint00001.h5 2Dhillslope/restarts/test0-ii_checkpoint00001.h5

echo "Running test2..."
python regression_tests.py -e $ATS_DIR/bin/ats -n 2Dhillslope/test2/test2.cfg

cd 2Dhillslope
