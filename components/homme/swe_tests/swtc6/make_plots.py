import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import sys

DS_new = xr.open_dataset('run-new-' + sys.argv[1] + '/swtc61.nc')
DS_orig = xr.open_dataset('run-orig-' + sys.argv[1] + '/swtc61.nc')

geop_new = DS_new.geop
geop_orig = DS_orig.geop

u_new = DS_new.u
u_orig = DS_orig.u

v_new = DS_new.v
v_orig = DS_orig.v

zeta_new = DS_new.zeta
zeta_orig = DS_orig.zeta

div_new = DS_new.div
div_orig = DS_orig.div

def plot_3Dvar(newvar, origvar, name, level, i):
    plt.figure(figsize=(10,8))
    plt.contourf(newvar.isel(time=i,lev=level))
    plt.colorbar()
    plt.contour(newvar.isel(time=i,lev=level))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'new.png')
    plt.close('all')

    plt.figure(figsize=(10,8))
    plt.contourf(origvar.isel(time=i,lev=level))
    plt.colorbar()
    plt.contour(origvar.isel(time=i,lev=level))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'orig.png')
    plt.close('all')

    plt.figure(figsize=(10,8))
    plt.contourf(newvar.isel(time=i,lev=level) - origvar.isel(time=i,lev=level))
    plt.colorbar()
    plt.contour(newvar.isel(time=i,lev=level) - origvar.isel(time=i,lev=level))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'diff.png')
    plt.close('all')

def plot_2Dvar(newvar, origvar, name, i):
    plt.figure(figsize=(10,8))
    plt.contourf(newvar.isel(time=i))
    plt.colorbar()
    plt.contour(newvar.isel(time=i))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'new.png')
    plt.close('all')

    plt.figure(figsize=(10,8))
    plt.contourf(origvar.isel(time=i))
    plt.colorbar()
    plt.contour(origvar.isel(time=i))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'orig.png')
    plt.close('all')

    plt.figure(figsize=(10,8))
    plt.contourf(newvar.isel(time=i) - origvar.isel(time=i))
    plt.colorbar()
    plt.contour(newvar.isel(time=i) - origvar.isel(time=i))
    plt.ylabel('lat')
    plt.xlabel('lon')
    plt.savefig(name+str(i)+'diff.png')
    plt.close('all')
#STATS PLOTTING

plot_3Dvar(geop_new, geop_orig, 'geop', 0, 14)
plot_3Dvar(u_new, u_orig, 'u', 0, 14)
plot_3Dvar(v_new, v_orig, 'v', 0, 14)
plot_3Dvar(zeta_new, zeta_orig, 'zeta', 0, 14)
plot_3Dvar(div_new, div_orig, 'div', 0, 14)
