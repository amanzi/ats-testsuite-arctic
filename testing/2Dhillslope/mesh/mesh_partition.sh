#!/bin/bash
#!/bin/sh
file_in=hillslope_organic_layerbyid2.exo
file_out=4/hillslope_organic_layerbyid2.par
mpiexec -n 4 $AMANZI_TPLS_DIR/bin/meshconvert --classify=1 --partition=y --partition-method=2 $file_in $file_out
