#Program : this is used to learn pytorch
#History : 2018-3-11    zhuyongjie     first release

import torch 
from torch.autograd import Variable as V

tensor = torch.FloatTensor([[1,2],[3,4]])
variable = V(tensor,requires_grad = True)

t_out = torch.mean(tensor*tensor)
v_out = torch.mean(variable*variable)

v_out.backward()
print(variable.grad) 
