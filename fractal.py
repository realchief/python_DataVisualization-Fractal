import numpy as np
import time
import matplotlib
from matplotlib import colors
import matplotlib.pyplot as plt
from mandelbrot import Mandelbrot


class Graphical(object):

    def show_graphical(self):

        xmin, xmax, xn = -2.25, +0.75, 3000 / 2
        ymin, ymax, yn = -1.25, +1.25, 2500 / 2
        maxiter = 200
        horizon = 2.0 ** 40
        log_horizon = np.log(np.log(horizon)) / np.log(2)
        Z, N = Mandelbrot.mandelbrot_set(self, xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)

        with np.errstate(invalid='ignore'):
            M = np.nan_to_num(N + 1 -
                              np.log(np.log(abs(Z))) / np.log(2) +
                              log_horizon)

        dpi = 72
        width = 10
        height = 10 * yn / xn
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        ax = fig.add_axes([0.0, 0.0, 1.0, 1.0], frameon=False, aspect=1)

        light = colors.LightSource(azdeg=315, altdeg=10)
        M = light.shade(M, cmap=plt.cm.hot, vert_exag=1.5,
                        norm=colors.PowerNorm(0.3), blend_mode='hsv')
        plt.imshow(M, extent=[xmin, xmax, ymin, ymax], interpolation="bicubic")
        ax.set_xticks([])
        ax.set_yticks([])

        text = "The Mandelbrot fractal"
        ax.text(xmin + .025, ymin + .025, text, color="white", fontsize=12, alpha=0.5)

        plt.show()


if __name__ == '__main__':
    graphical = Graphical()
    graphical.show_graphical()