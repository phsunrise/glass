'''
This script uses degrees for angles 
'''

import numpy as np
import matplotlib.pyplot as plt

## settings
add_poisson = True # Poisson noise in photon counting 
N = 1 # number of particles per snapshot
N_s = 100 # number of snapshots
M_phi = 72 # number of azimuthal bins
print "# particles = %d, # snapshots = %d" % (N, N_s)

## simulate the snapshots
snapshots = [] # array of snapshots
for i_s in range(N_s):
    d = np.random.random_sample([N,])*360. # generating particles
    hist1, bin_edges = np.histogram(d, bins=M_phi, range=(0., 360.))
    d1 = d + 72. # for now assumes angular correlation is exactly a delta function at 72 deg
    d1[d1>=360.] -= 360.
    hist2, bin_edges = np.histogram(d1, bins=M_phi, range=(0., 360.))
    snapshot = hist1 + hist2
    if add_poisson:
        snapshot1 = np.random.poisson(lam=snapshot)
        snapshot = np.copy(snapshot1)
    snapshots.append(snapshot)

bin_centers = 0.5*(bin_edges[:-1]+bin_edges[1:])

snapshots = np.array(snapshots)
shot_ave = np.mean(snapshots, axis=0)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

ax.plot(bin_centers, shot_ave)
ax.axhline(y=2.*N/M_phi, c='r', ls='--')
#ymin, ymax = ax.get_ylim()
#ax.set_ylim(0., ymax)

plt.show()

## now calculate the correlation
snapshots = snapshots - shot_ave
shot_corr = np.zeros(M_phi)
for i_s in range(N_s):
    snapshot = snapshots[i_s]
    shot_corr += np.correlate(snapshot, np.hstack((snapshot[1:], snapshot)), mode='valid')

plt.plot(bin_centers, shot_corr)
plt.show()
