import numpy as np
from random import uniform

#1 
#过两天我自己都看不懂了
#[-1]取累积和式的最后一项
def p(x,coeff): return((((np.zeros(len(coeff))+x).cumprod()*coeff).cumsum())[-1])

#2
def sample(q):
    from  random import uniform
    U = uniform(0,1)
    f = (np.zeros(len(q))+q).cumsum()
    return np.searchsorted(f,U)

class discreteRV:
    def __init__(self, q):
        self.q = q
    def draw(self):
        U = uniform(0,1)
        f = (np.zeros(len(self.q))+self.q).cumsum()
        return np.searchsorted(f,U)
		
#3
class ECDF:
    def __init__(self, obs):
        self.obs = obs
    def __call__(self, x):
        return sum(1 - np.searchsorted([x],self.obs))/len(self.obs)
    def plots(self, a, b):
        return self(b)-self(a)
