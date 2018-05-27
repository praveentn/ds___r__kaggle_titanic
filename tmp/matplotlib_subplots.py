# https://stackoverflow.com/questions/50550117/\
# create-subplots-from-output-a-singular-plot-of-a-function

import matplotlib.pyplot as plt
import numpy as np

#plot function with defined axis
def plot_subplot(ax, xdata, ydata, plotnr):
    ax.plot(xdata, ydata)
    ax.set_title("Plot {}".format(plotnr))
    return

#subplot grid 2 x 3 to illustrate the example for more than one row/column
fig, axes = plt.subplots(nrows = 2, ncols = 3, sharex = "all", figsize = (15,5), squeeze=False)
#reproducibility seed
np.random.seed(54321)
#loop over axes, we have to flatten the array "axes", if "fig" contains more than one row
for i, ax in enumerate(axes.flatten()):
    #generate random length for data
    lenx = np.random.randint(5, 30)
    #generate random data, provide information to subplot function
    plot_subplot(ax, np.arange(lenx), np.random.randint(1, 100, lenx), i)

plt.show()
