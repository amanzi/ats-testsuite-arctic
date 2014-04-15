import sys
import matplotlib
#matplotlib.use('PDF')
sys.path.append('/lclscratch/ecoon/ats/ats-tests/utils')
import parse_output2
from matplotlib import pyplot as plt

with open("out.log",'r') as fid:
    dt = parse_output2.parse_file(fid)

plt.semilogy(dt[0][:,1], dt[0][:,2], 'b-x')
plt.ylabel("dt [days]")
plt.xlabel("t [days]")
plt.show()
