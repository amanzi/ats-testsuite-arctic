#!/bin/bash
#!/bin/sh
dir=1Dbotflux_github_mod

cd ../
test0i=$dir/test0/test0-i.regression.gold
test0ii=$dir/test0/test0-ii.regression.gold
test2=$dir/test2/test2-iii.regression.gold
test7=$dir/test7/test7-v.regression.gold

if [ -d "$test0ii" ]; then
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
python regression_tests.py -e $ATS_DIR/bin/ats -n $dir/test0/test0.cfg

echo "Running test2..."
python regression_tests.py -e $ATS_DIR/bin/ats -n $dir/test2/test2.cfg

cd $dir/test2/test2-iii.regression.gold
chfile=$(ls -t checkpoint* | head -1)
echo $chfile
cp $chfile ../../restarts/test2_checkpoint.h5
cd ../../../

echo "Running test7.. "
python regression_tests.py -m `which mpiexec` -e $ATS_DIR/bin/ats -n $dir/test7/test7.cfg

cd $dir
