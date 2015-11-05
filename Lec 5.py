#1
class ECDF:
    def __init__(self, obs):
        self.observations = obs
    def __call__(self,x):
        n = len(self.observations)
        #print(self.observations)
        flag = 0
        for Xi in self.observations:
            if Xi<=x:
                flag = flag + 1
        return flag/n


#2
class Polynomial:
    def __init__(self,coeff):
        self.coeff = coeff
    def p(self,x):
        s = 0
        for power, coeff in enumerate(self.coeff):
            s = s + pow(x,power)*coeff
        return s
    def diff(self):
        tmp=[]
        for power, coeff in enumerate(self.coeff):
            coeff = power*coeff
            tmp.append(coeff)
        tmp.pop(0)
        self.coeff=tmp
        return self.coeff
