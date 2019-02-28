#!/bin/bash
#!/bin/sh
# This script creates the 1D column file that gets fed to 2Dhillslope model
cur_dir=`pwd`
cd $ATS_SRC_DIR/tools/utils/
rm -rf *.h5

cp full-path-to-the-folder/1D/test7/test.default.regression/visdump_data.h5 .
cp full-path-to-the-folder/1D/test7/test.default.regression/visdump_mesh.h5 .

python column_data.py -t 0
cd $cur_dir
cp $ATS_SRC_DIR/tools/utils/column_data.h5 new_column.h5
echo 'Column for 2Dhillslope was successfully created'
