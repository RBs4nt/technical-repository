#Plotting line sine and cosine on the same graph

#Importing libraries
import pylab as pl
import numpy as np

#Obtaining data for sine and cosine function
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

#plotting the two on the same graph
pl.plot(X, C)
pl.plot(X, S)

#viewing
pl.show()