# On EES-16 servers, make sure that an ats module is loaded to access these modules.
# Otherwise, add the tools/utils folder in your ats source directory to your PYTHONPATH environment variable
import sys,os
sys.path.insert(0, "/n/swdev/ats/ats/repos/dev/tools/utils")

import atsxml
import parse_ats
# On EES-16 servers, load the matk module: module load matk
# Otherwise, directions to obtain and install matk are at http://matk.lanl.gov/installation.html
from matk import matk
import numpy as np

# The model that MATK will provide parameters to as a dictionay in the argument (pars)
fnames = [d for d in os.listdir(".") if d.endswith(".xml")]

def model(pars,hostname,processor):
    filename = fnames[int(np.round(pars['fname']))]
    dirname = filename.strip(".xml").strip("test7-")
    with open("dirname.txt",'w') as fid:
        fid.write(dirname)

    # Modify base ats xml input file with pars dictionary and run ats
    m = atsxml.get_root('../%s'%fnames[int(pars['fname'])])
    atsxml.run(m,nproc=2,stdout='stdout.out',stderr='stdout.err',cpuset=processor)

    # Return simulated values of interest
    return 0

# Create host dictionary so that cpu sets can be explicitly defined for ats runs
# The host (dictionary key) 'dum' will be ignored in this case
# The list of strings will be used as the cpu sets for the runs
procs = ["%i,%i"%(i,i+1) for i in range(32,64,2)]
print procs
hosts = {'dum':procs}
# Create MATK object specifying the 'model' function above as the model
p = matk(model=model)

# Add some parameters
# Mineral soil porosity
p.add_par('fname',min=0, max=len(fnames)-1, value=0)

# Create parameter study where nvals indicats the number of values for each parameter
# Parameter values will be spaced evenly over parameter ranges
s = p.parstudy(nvals=[len(fnames)])

# Run sampleset in individual folders with base name 'run'
# logfile will contain results of sampling in progress, including error messages for failed runs
# outfile will be written at the end with samples in correct order
s.run(cpus=hosts,workdir_base='run',outfile='sample.out',logfile='sample.log')
