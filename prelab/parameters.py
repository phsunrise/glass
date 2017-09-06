import numpy as np

re = 2.81794e-6 # classical electron radius in nm

R = float(input("SNR: "))
f = float(input("Form factor: "))
Mphi = 40
print("Assuming 40 angular bins")
Nph = float(input("Flux/area (ph/s/nm^2): "))
s = float(input("Solid angle: "))

print('\n')

t = 1 # exposure time
Nshots = R**2*1./Mphi/f**4/(Nph*t)**2/re**4/s**2
print("%f sec exposures: %e shots" % (t, Nshots))
print("  = %e mins = %e hrs = %e days\n" % (\
        Nshots/60., Nshots/3600., Nshots/86400.))


while t > 0:
    t = float(input("Enter exposure time (s) (enter <=0 to exit): "))
    Nshots = R**2*1./Mphi/f**4/(Nph*t)**2/re**4/s**2
    print("%f sec exposures: %e shots\n" % (t, Nshots))
    print("  = %e mins = %e hrs = %e days" % (\
            Nshots/60., Nshots/3600., Nshots/86400.))
