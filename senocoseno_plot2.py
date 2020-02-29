# Plot the sine cosine graph instantiating all settings
# Chart will be saved in png format

import pylab as pl
import numpy as np

# Creates a figure of size 8x6 points, 80 points per inch
pl.figure(figsize=(8, 6), dpi=80)

# Creates a new subplot from a 1x1 grid
pl.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Plot the cosine with a continuous blue line of thickness 1 (pixels)
pl.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

# Plot the sine with a continuous green line of thickness 1 (pixels)
pl.plot(X, S, color="green", linewidth=1.0, linestyle="-")

# Sets the limits on x
pl.xlim(-4.0, 4.0)

# Sets the x marks
pl.xticks(np.linspace(-4, 4, 9, endpoint=True))

# Defines the limits in y
pl.ylim(-1.0, 1.0)

# Sets the y-marks
pl.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Saves the figure using 72 dots per inch
pl.savefig("sencos.png", dpi=72)

# Shows the result on the screen
#pl.show()