'''
Calculates: solid angle, wavelength, detector (half) opening angle
'''
import numpy as np

E = input("Energy (keV): ")
a0 = input("Resolution at detector edge (Angstrom): ")
a = input("Probing resolution (Angstrom): ")
b = input("Longest range (Angstrom): ")
Nphi = input("Number of azimuthal bins: ")
print('\n')

wl = 12.3984/E
print("Wavelength = %f Angstrom" % (wl))

tth_edge = 2.*np.arcsin(wl/a0/2.)
print("Detector half opening angle = %f deg" % (tth_edge/np.pi*180.))

tth_hi = 2.*np.arcsin(wl * (1./a + 1./b/2) / 2.)
tth_lo = 2.*np.arcsin(wl * (1./a - 1./b/2) / 2.)

s = 2.*np.pi*(np.cos(tth_lo) - np.cos(tth_hi)) / Nphi
print("Solid angle = %f" % (s))
