import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-1,1,50)

plt.figure(num=1)
y=x**2
plt.plot(x,y)
plt.figure(num=2)
y1=3*x+2
plt.plot(x,y1,color='green',linewidth=2,linestyle='--')

plt.show()
