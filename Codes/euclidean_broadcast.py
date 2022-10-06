import numpy as np
from memory_profiler import profile

@profile
def euclidean_broadcast(x, y):
    """Euclidean square distance matrix.
    
    Inputs:
    x: (N, m) numpy array
    y: (N, m) numpy array
    
    Ouput:
    (N, N) Euclidean square distance matrix:
    r_ij = (
    """

    diff = x[:, np.newaxis, :] - y[np.newaxis, :, :]
    
    return (diff*diff).sum(axis=2)

if __name__ == "__main__":
    nsampel = 2000
    nfeature = 50

    rng = np.random.default_rng()
    x = 10. * rng.random((nsampel, nfeature))

    euclidean_broadcast(x,x)
