#!/bin/bash
#!/bin/sh
file_in=test_organic.exo
file_out=4/test_organic.par
mpiexec -n 4 $AMANZI_TPLS_DIR/bin/meshconvert --classify=1 --partition=y --partition-method=2 $file_in $file_out
