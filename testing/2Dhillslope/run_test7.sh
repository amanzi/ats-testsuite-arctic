#!/bin/bash
#!/bin/sh
cd ../

echo "Running Snow Distribution version 2Dhillslope/test7_SD "
python regression_tests.py -m `which mpiexec` -e $ATS_DIR/bin/ats -n 2Dhillslope/test7_SD/test7.cfg

#echo "Running Snow from file  version 2Dhillslope/test7 "
# this version is currently crashing
#python regression_tests.py -m `which mpiexec` -e $ATS_DIR/bin/ats -n 2Dhillslope/test7/test7.cfg

cd 2Dhillslope
