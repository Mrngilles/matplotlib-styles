import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style

import test_functions as t

matplotlib.style.use('../layout/presentation.mplstyle')

#fig, ax = t.sinplot()
#fig, ax = t.bessel_plot()
#fig, ax = t.fill_plot()
fig, ax = t.exp_mx(4)
ax.grid()
ax.legend()

fig.tight_layout()

plt.show()
