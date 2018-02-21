#!/bin/bash
#!/bin/sh
# This script creates the 1D column file that gets fed to test7
# Run this script in its saved folder (../init)
cur_dir=`pwd`
cd $ATS_SRC_DIR/tools/utils/
rm -rf *.h5
cp $ATS_BASE/ats-testsuite-arctic/testing/2Dhillslope/test2/run21_09Feb18/visdump_data.h5 .
cp $ATS_BASE/ats-testsuite-arctic/testing/2Dhillslope/test2/run21_09Feb18/visdump_mesh.h5 .
python column_data.py -t 0
cd $cur_dir
cp $ATS_SRC_DIR/tools/utils/column_data.h5 column_data_run21_09Feb18.h5
echo 'Exp1 Column h5 file successfully created'
