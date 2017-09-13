'''
This script uses degrees for angles 
'''

import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='serif', size=12)
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

'''
N = number of particles per shot
N_s = number of snapshots
M_phi = number of azimuthal bins
add_poisson = whether to add poisson noise
'''
def get_lineout(N=1, N_s=100, M_phi=72, add_poisson=True):
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

    ## now calculate the correlation
    snapshots = snapshots - shot_ave
    shot_corr = np.zeros(M_phi)
    for i_s in range(N_s):
        snapshot = snapshots[i_s]
        shot_corr += np.correlate(snapshot, np.hstack((snapshot[1:], snapshot)), mode='valid')

    return bin_centers, shot_corr*1./N_s


if __name__ == "__main__":
    add_poisson = True # Poisson noise in photon counting 
    #N = 100 # number of particles per snapshot
    N_s = 100 # number of snapshots
    M_phi = 72 # number of azimuthal bins

    N_array = [1, 10, 10**2, 10**4, 10**6]
    plt.figure(figsize=(7,7))
    for i_N, N in enumerate(N_array):
        bin_centers, shot_corr = get_lineout(N=N, N_s=N_s, M_phi=M_phi, add_poisson=add_poisson)
        shot_corr[0] = 0
        label = ("N=%d"%N if N <= 100 else "N=%.0e"%N)
        plt.plot(bin_centers, shot_corr*1./N+1.*i_N, label=label)
        print "Done N=%d" % (N)

    plt.xlabel(r"$\Delta\phi$ (deg)")
    plt.ylabel(r"$\left<\int_\phi (I(\phi)-\bar{I})(I(\phi+\Delta\phi)-\bar{I})\right>$")
    plt.legend()
    plt.title("# exposures = %d" % N_s)
    plt.savefig("plots/Fixed_Ns.pdf")
    plt.show()
