import sys,os
import matplotlib
sys.path.append(os.path.join(os.environ['ATS_SRC_DIR'],'tools', 'utils'))
import parse_xmf
import column_data
import colors
import numpy as np
from matplotlib import pyplot as plt

def getFigs(inset, is_temp, is_seb):
    fig = plt.figure(figsize=(8,3))
    axs = []
    if is_temp:
        axs.append(fig.add_subplot(131))
        axs.append(fig.add_subplot(132))
        axs.append(fig.add_subplot(133))
        if inset:
            axs.append(fig.add_axes([0.6,0.5,0.25, 0.25]))
    else:
        axs.append(fig.add_subplot(121))
        axs.append(fig.add_subplot(122))
        if inset:
            axs.append(fig.add_axes([0.86,0.67,0.1, 0.25]))
    return fig,axs

# collect data, determine control for plots
keys, times, dat = parse_xmf.readATS()
try:
    skeys, stimes, sdat = parse_xmf.readATS(base="visdump_surface_data.h5")
except IOError:
    inset = False
    is_seb = False
else:
    inset = True
    is_seb = "snow_depth.cell.0" in sdat.keys()

is_temp = "temperature.cell.0" in dat.keys()
is_ice = "saturation_ice.cell.0" in dat.keys()

# sort the data
to_get = ["pressure"]
if is_temp:
    to_get.append("temperature")
to_get.append("saturation_liquid")
if is_ice:
    to_get.append("saturation_ice")
to_get.append("saturation_gas")
dat = column_data.column_data(to_get)

# convert times to days
times = [time*365.25 for time in times]

# create subsurface coordinate
z = dat[0,0,:]

# get colors
ice = colors.cm_mapper(-10, times[-1], colors.ice_cmap())
water = colors.cm_mapper(-10, times[-1], colors.water_cmap())
gas = colors.cm_mapper(-10, times[-1], colors.gas_cmap())

# create figures
fig, axs = getFigs(inset, is_temp, is_seb)

# plot
for i,time in enumerate(times):
    if is_temp:
        j = 3
    else:
        j = 2

    axs[0].plot(dat[j,i,:],z,color=water(time))
    j = j + 1
    if is_ice:
        axs[0].plot(dat[j,i,:],z,color=ice(time))
        j = j + 1

    axs[0].plot(dat[j,i,:],z,color=gas(time))

axs[0].set_xlim([-.1,1.1])
axs[0].set_xlabel('saturation [-]')
axs[0].set_ylabel('z-coordinate [m]')

for i,time in enumerate(times):
    axs[1].plot(dat[1,i,:],z,color=water(time))

axs[1].set_xlabel('head [m]')
axs[1].set_ylabel('z-coordinate [m]')
axs[1].ticklabel_format(style='sci', axis='x', scilimits=(0,0))

if inset:
    pd = parse_xmf.getSurfaceData(keys, sdat, 'ponded_depth.cell.0')
    axs[-1].plot(times, pd, 'b')
    axs[-1].set_xlabel('time [d]')
    axs[-1].set_ylabel('ponded depth [m]')
    axs[-1].set_ylim([-.1*pd.max(), pd.max()])
    axs[-1].set_xticks([0,100])

    if is_seb:
        snow = parse_xmf.getSurfaceData(keys, sdat, 'snow_depth.cell.0')
        snow = snow + pd
        axs[-1].plot(times, snow, 'c')
        axs[-1].set_ylabel('ponded (b) and snow (c) depth [m]')
        axs[-1].set_ylim([-.1*snow.max(), snow.max()])

    if is_temp:
        try:
            sdat["surface_temperature.cell.0"]
        except KeyError:
            Tkey = "surface-temperature.cell.0"
        else:
            Tkey = "surface_temperature.cell.0"
        surf_T = parse_xmf.getSurfaceData(keys, sdat, Tkey)
        twinax = axs[-1].twinx()

        twinax.plot(times, surf_T, 'r')
        twinax.set_ylabel('surface T [K]')
        
        if is_seb:
            snow_T = parse_xmf.getSurfaceData(keys, sdat, 'snow_temperature.cell.0')
            snow_T[0] = 273.15 # by default this is 0...
            twinax.plot(times, snow_T, 'm')
            twinax.set_ylabel('surface (r) and snow (m) T [K]')



if is_temp:
    for i,time in enumerate(times):
        axs[2].plot(dat[2,i,:],z,color=gas(time))

    axs[2].set_xlabel('temperature [K]')
    axs[2].set_ylabel('z-coordinate [m]')


plt.tight_layout()
#plt.savefig('soln_temp.pdf')
plt.show()
