#1
def factorial(n):
    sum=1
    while(n>0):
        sum=sum*n
        n=n-1
    return sum

#2
def binomial_rv(n, p=0.5):
    from random import uniform
    flag = 0
    for i in range(n):
        tmp = uniform(0,1)
        if tmp < p:
            flag=flag+1
    return flag/n
	
#3
def MonteCarlo(n, r=1):
    from random import uniform
    from math import sqrt
    flag = 0
    for i in range(n):
        x = uniform(0,r)
        y = uniform(0,r)
        l = sqrt(x*x+y*y)
        if l < r:
            flag = flag + 1
    return flag/n*4
	
#4
def pay(result):
    flag=0
    for coin in result:
        if coin=='H':
            flag=flag+1
        else:
            flag=0
        if flag>2:
            return('pay one dollar')
    return('pay nothing')

def coin(n=10):
    from random import uniform
    result = []
    for i in range(n):
        a = uniform(0,1)
        if a < 0.5:
            result.append('H')
        else:
            result.append('T')
    #print(result)
    return(pay(result))
	
#5
def TimeSeries(T=200,alpha=0.9):
    import matplotlib.pyplot as plt
    from random import normalvariate
    ts = []
    ts.append(0)
    for i in range(T):
        tmp = ts[i]*alpha + normalvariate(0,1)
        ts.append(tmp)
    return(ts)
	
#6
from pylab import plot, show, legend
import matplotlib.pyplot as plt
from random import normalvariate

alpha=[0.0,0.8,0.98]
x = [TimeSeries(200, a) for a in alpha]

for i in range(3):
    plot(x[i], label="alpha = "+ str(alpha[i]))
          
legend()
show()
