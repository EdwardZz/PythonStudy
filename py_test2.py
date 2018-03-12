#Program : this is used to learn a fast way to build network
#History : 2018-3-12   zhuyongjie
import torch
from torch.autograd import Variable as V
import torch.nn.functional as F
import matplotlib.pyplot as plt

x = torch.unsqueeze( torch.linspace(-1,1,100),dim=1)
y = x.pow(2)+0.2*torch.rand(x.size())

x,y=V(x),V(y)

#plt.scatter(x.data.numpy(),y.data.numpy())
#plt.show()

net = torch.nn.Sequential(
	torch.nn.Linear(1,10),
	torch.nn.ReLU(),
torch.nn.Linear(10,1)
) 

print(net)

plt.ion()
plt.show()

optimizer = torch.optim.SGD(net.parameters(),lr=0.5)
loss_func = torch.nn.MSELoss()

for t in range(100):
	prediction = net(x)
	loss = loss_func(prediction,y)

	optimizer.zero_grad()
	loss.backward()
	optimizer.step()
	if t%5 ==0:
		plt.cla()
		plt.scatter(x.data.numpy(),y.data.numpy())
		plt.plot(x.data.numpy(),prediction.data.numpy(),'r-',lw=5)
		plt.text(0.5,0,'loss=%.4f' % loss.data[0],fontdict={'size':20,'color':'red'})
		plt.pause(0.1)
plt.ioff()
plt.show()
