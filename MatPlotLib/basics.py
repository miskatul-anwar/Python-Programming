import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig = plt.figure()
fig, ax = plt.subplots()
fig, ax = plt.subplots(2, 2)
fig, axs = plt.subplot_mosaic([["left", "right_top"], ["left", "right_bottom"]])
plt.show()
