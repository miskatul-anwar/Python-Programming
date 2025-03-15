import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-100,100,201)
y1 = 0.5*x**2+2*x
y2 = np.sin(x)*2000
y3 = np.log(x)*2000
plt.plot(x,y1,'r*')
plt.plot(x,y2,'g--')
plt.plot(x,y3,'b')
plt.show()
