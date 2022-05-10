import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc

rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

SMALL_SIZE = 16
MEDIUM_SIZE = 18
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
x_an = [0, (1-0.1)*np.sqrt(2)/2, (1-0.1)*np.sqrt(2)/2, (1+0.1)*np.sqrt(2)/2, (1+0.1)*np.sqrt(2)/2, np.sqrt(2)]
y_an = [0, 0, 1, 1, 0, 0]
plt.plot(x_an,y_an, label="analytical")

schemes = ["linear", "QUICK", "SuperBee", "MUSCL", "linearUpwind_gradU"]

for i in schemes:
    my_data = np.genfromtxt("line1_T_"+i+'.xy', delimiter=' ')
    plt.plot(my_data[:,0],my_data[:,1],label=i)
    plt.xlabel("$x$-coordinate")
    plt.ylabel("$T$")
plt.legend()
plt.grid()
plt.show()