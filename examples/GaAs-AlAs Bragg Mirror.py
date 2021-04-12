#!/usr/bin/env python
# coding: utf-8

# # GaAs-AlAs Bragg Mirror
# A simple bragg mirror in the near infrared.

# --------------------- importing libraries ---------------------
import numpy as np # numpy
import matplotlib.pyplot as plt # matplotlib pyplot
import sys                  # sys to add the library to the path

# adding folder containing 1DPyHC to path
sys.path.append('../')
import pyhc as phc # importing 1DPyHC

# useful parameters
f_size=20;



# --------------------- Defining input paramaters ---------------------
# Below are all the input variables of the 
# dielectric mirror. Play around with 
# them and see what happens

# ref indexes
n2 = 3.49 # GaAs
n1 = 2.95 # AlAs
n_inc = 1.0 # Incident medium
n_sub = 1.45 # Substrate

# wavelength
wl = 1064 # Bragg mirror working wavelength

# plotting wavelengths
n_wl = 500
v_wl = np.linspace(950,1200,n_wl)

# layers thickness in nm
b = wl/(4 * n2)
a = wl/(4 * n1)

# number of periods of the photonic crystal
N=20



# --------------------- Perform the computation ---------------------
# computation of the reflectance of the 1D photonic crystal
v_R = np.array([phc.rN(b, a, n2, n1, n_inc, n_sub, N, phc.f_omega(l), 0.0) for l in v_wl])



# --------------------- Plot the result and compare it with tabulated data ---------------------
# reference data computed from simple t-matrix approach
ref_data = np.loadtxt('gaas_alas_tmatrix.spt')
v_wl_ref = ref_data[:,0]
v_R_ref = ref_data[:,1]



# Here we plot the data using [matplotlib](http://matplotlib.org/) and [pyplot](http://matplotlib.org/api/pyplot_api.html).

# result plot
plt.figure(figsize=(12,10))
plt.plot(v_wl_ref,v_R_ref,'ro',
         v_wl,v_R,'k',linewidth=2.0)

# ticks and labels
plt.xticks(fontsize=f_size)
plt.yticks(fontsize=f_size)
plt.xlabel("Wavelength (nm)", fontsize=f_size)
plt.ylabel("R", fontsize=f_size)

# legend
plt.legend(('tmatrix reference','PythonicCrystal'),frameon=False,fontsize=f_size-5,loc='lower center')
plt.show()
