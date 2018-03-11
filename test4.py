#Program : made for pytorch learning
#History : 2018-3-11    zhuyongjie    first release

import torch 
import torch.nn.functional as F
from torch.autograd import Variable as V
import matplotlib.pyplot as plt

# fake data 
x = torch.linspace(-5,5,200)  
x = V(x)
x_np=x.data.numpy()

y_relu = F.relu(x).data.numpy()
y_sigmoid = F.sigmoid(x).data.numpy()
y_tanh = F.tanh(x).data.numpy()
y_softplus = F.softplus(x).data.numpy()

# make figure
plt.figure()
plt.subplot(221)
plt.plot(x_np,y_relu,color='red',label='relu')
plt.ylim(-1,5)
plt.legend(loc='best')

plt.subplot(222)
plt.plot(x_np,y_sigmoid,color='red',label='sigmoid')
plt.ylim(-0.2,1.2)
plt.legend(loc='best')

plt.subplot(223)
plt.plot(x_np,y_tanh,color='red',label='tanh')
plt.ylim(-1.2,1.2)
plt.legend(loc='best')

plt.subplot(224)
plt.plot(x_np,y_softplus,color='red',label='softplus')
plt.ylim(0,5)
plt.legend(loc='best')

plt.show()
