import numpy as np
from memory_profiler import profile

@profile
def euclidean_trick(x, y):

    x2 = np.einsum('ij,ij->i', x, x)[:, np.newaxis]
    y2 = np.einsum('ij,ij->i', y, y)[np.newaxis, :]

    xy = x @ y.T

    return np.abs(x2 + y2 - 2. * xy)

if __name__ == "__main__":
    nsampel = 2000
    nfeature = 50

    rng = np.random.default_rng()
    x = 10. * rng.random((nsampel, nfeature))

    euclidean_trick(x,x)
