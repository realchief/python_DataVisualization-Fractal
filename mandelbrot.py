import numpy as np
from complex import Complex
import time
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt


class Mandelbrot(object):

    def mandelbrot_set(self, xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon=2.0):
        X = np.linspace(xmin, xmax, xn, dtype=np.float32)
        Y = np.linspace(ymin, ymax, yn, dtype=np.float32)
        C = X + Y[:, None]*1j
        N = np.zeros(C.shape, dtype=int)
        Z = np.zeros(C.shape, np.complex64)
        for n in range(maxiter):
            I = np.less(abs(Z), horizon)
            N[I] = n
            Z[I] = Z[I]**2 + C[I]
        N[N == maxiter-1] = 0
        return Z, N


if __name__ == '__main__':
    mandelbrot = Mandelbrot()



