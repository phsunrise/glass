import numpy as np
import matplotlib.pyplot as plt

a = np.random.poisson(lam=[10, 20], size=(1000, 2))

plt.hist(a[:,0], bins=100, range=(0., 100.))
plt.hist(a[:,1], bins=100, range=(0., 100.))
plt.show()
