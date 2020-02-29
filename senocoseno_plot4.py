# Moving the axes and adding a caption to the cosine sine grap

import pylab as pl
import numpy as np

# Creates a figure of size 10x6 points, 80 points per inch
# Changing figure to make it more horizontal
pl.figure(figsize=(10, 6), dpi=80)

# Creates a new subplot from a 1x1 grid
pl.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

# Cosine in blue, sine in red both with thicker lines and definition of names for each line in the graph
pl.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
pl.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

# Subtitle
pl.legend(loc='upper left')

# Sets the limits on x
pl.xlim(-4.0, 4.0)

# # moving the secondary axes
ax = pl.gca()  
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Sets the x marks
pl.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$']) 
          # Marker x showing only explicit essential values

# Defines the limits in y
#pl.ylim(-1.0, 1.0)

# Sets the y-marks
pl.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])
          # Marker y showing only explicit essential values

# Saves the figure using 72 dots per inch
#pl.savefig("sencos.png", dpi=72)

# Shows the result on the screen
pl.show()