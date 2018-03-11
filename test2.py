#Program: this  program is used to test the matplotlib of python
#History: 2018-3-10   zhuyongjie     first release


import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(-2,2,50)
y1 = x**2+1
y2 = x**3+1
l1, = plt.plot(x,y1,color='red',linewidth=2,linestyle="--")
l2, = plt.plot(x,y2,linewidth=1.5)

plt.xlim(-1,1)
plt.ylim(-1,9)
new_ticks=np.linspace(-1,2,5)
plt.xticks(new_ticks)
plt.yticks([-1,1,3,5,7],
['$a$','$b$','c','d','e']
)

plt.legend(handles=[l1,l2,],labels=['red','blue'],loc='best')
plt.show() 
