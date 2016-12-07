#!/bin/bash
#!/bin/sh
file_in=tri_exp1_2D.exo
file_out=4/tri_exp1_2D.par
mpiexec -n 4 $AMANZI_TPLS_DIR/bin/meshconvert --classify=1 --partition=y --partition-method=2 $file_in $file_out
