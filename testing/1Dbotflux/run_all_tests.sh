#!/bin/bash
#!/bin/sh

#functions
delete_folder() {
  if [ -d "$1" ]; then
    echo "Deleting" $1
    rm -rf $1
  else
    echo $1 "DOES NOT EXIST"
  fi
}

copy_last_checkpoint_2_restart() {
  cd $1
  chfile=$(ls -t checkpoint* | head -1)
  echo $chfile
  cp $chfile ../../restarts/"$2"_checkpoint.h5
  cd ../../../
}

#main
dir=$(pwd)
cd ../
test0=$dir/test0/test0-organic.regression.gold
test2=$dir/test2/test2-organic.regression.gold
test7=$dir/test7/test7-organic.regression.gold
test8=$dir/test8/test8.regression

# if we want to start new simulation, we need to delete old folders 
delete_folder $test0
delete_folder $test2
delete_folder $test7
delete_folder $test8

echo "Running test0..."
python regression_tests.py -e $ATS_DIR/bin/ats -n $dir/test0/test0.cfg

echo "Running test2..."
python regression_tests.py -e $ATS_DIR/bin/ats -n $dir/test2/test2.cfg

copy_last_checkpoint_2_restart $test2 test2

#echo "Running test7.. "
#python regression_tests.py -m `which mpiexec` -e $ATS_DIR/bin/ats -n $dir/test7/test7.cfg

#copy_last_checkpoint_2_restart $test7 test7

#echo "Running test8.. "
#cd $dir/test8
#mkdir test8.regression
#cd test8.regression
#$ATS_DIR/bin/ats --xml_file='../test8-organic.xml' > teststd.out

cd $dir
#exit 1
