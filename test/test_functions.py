import numpy as np
import matplotlib.pyplot as plt
import scipy.special as spsp

PTS_NUM = 200
def sinplot(num = 5):
    fig, ax = plt.subplots()
    x = np.linspace(0, 14, PTS_NUM)
    for i in xrange(1, num):
        ax.plot(x, np.sin(x + 0.5*i)*(num-i), 'o-', label="i = {}".format(i))
    ax.set_title("Modified sinus function")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    return fig, ax

def bessel_plot(num=5):
    fig, ax = plt.subplots()
    x = np.linspace(0, 20, PTS_NUM)
    for v in xrange(1, num):
        y = spsp.jv(v, x)
        plt.plot(x, y, 'o-', label=r"$J_{}$".format(v))
    ax.set_title("Bessel functions")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    return fig, ax

def fill_plot():
    fig, ax = plt.subplots()
    x = np.linspace(0, 20, PTS_NUM)
    y1 = np.sin(x)+(x/2.)
    y2 = np.sin(x)+x
    plt.fill_between(x, y1, y2, label="Filled")
    ax.set_title("Filled between")
    ax.set_xlabel("x label")
    ax.set_ylabel("y label")
    return fig, ax
