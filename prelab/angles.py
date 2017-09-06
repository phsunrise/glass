'''
Calculates: solid angle, wavelength, detector (half) opening angle
'''
import numpy as np

E = float(input("Energy (keV): "))
a0 = float(input("Resolution at detector edge (Angstrom): "))
a = float(input("Probing resolution (Angstrom): "))
b = float(input("Longest range (Angstrom): "))
Mphi = 40
print("Assuming 40 angular bins")
print('\n')

wl = 12.3984/E
print("Wavelength = %f Angstrom" % (wl))

tth_edge = 2.*np.arcsin(wl/a0/2.)
print("Detector half opening angle = %f deg" % (tth_edge/np.pi*180.))

tth_hi = 2.*np.arcsin(wl * (1./a + 1./b/2) / 2.)
tth_lo = 2.*np.arcsin(wl * (1./a - 1./b/2) / 2.)

s = 2.*np.pi*(np.cos(tth_lo) - np.cos(tth_hi)) / Mphi
print("Solid angle = %f" % (s))
