import numpy as np
from scipy.optimize import root

def your_funcs(X):

    x, y, a, b = X

    f = [np.cos(x) / x - 0.21 * a - 0.41,
         np.cos(y) / y - 0.43 * b - 0.48,
         a + b - 1,
         0.93 * np.sinc(x) - 0.72 * np.sinc(y)]

    return f

sol2 = root(your_funcs, [0.13, 0.11, 0.29, 0.11])

print(sol2.x)
