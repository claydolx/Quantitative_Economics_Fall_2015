#1
#P1
x_vals=[1,2,3]
y_vals=[3,4,5]
sum = 0
for x,y in zip(x_vals,y_vals):
    sum = sum + x*y  
print(sum)

#P2
f = lambda x: (x-x%2)/2
f(99)

#P3
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))
flag = 0
for element in pairs:
    x, y = element
    if x%2==0 and y%2==0:
        flag = flag + 1
print(flag)

#2
#幂的英语是power
def p(x,coeff):
    s = 0
    for power, coeff in enumerate(coeff):
        s = s + pow(x,power)*coeff
    return s

#3 坑：空格、换行符等
def ex3(string):    
    string2 = string.upper()
    s1 = 0
    s2 = 0
    for k in range(len(string)):
        if string[k]==string2[k]:
            s1 = s1+1
        if string[k]==' ' or string[k]=='\n': #并没有完全解决问题
            s2 = s2+1
    return s1-s2

#4
def ex4(seq_a,seq_b):
    for element in seq_a:
        if element not in seq_b:
            return False
    return True

#5 用了字典储存各点的值
def linapprox(f,a,b,n,x):
    value={}    
    step=(b-a)/(n-1)
    for k in range(n):
        tmp=a+step*k
        value[tmp]=f(tmp)
    for k in range(n):
        if x >= a+step*k and x <= a+step*(k+1):
            x0 = a+step*k
            x1 = a+step*(k+1)
            y0 = value[a+step*k]
            y1 = value[a+step*(k+1)]
            approx = y0+(y1-y0)*(x-x0)/(x1-x0)
    return approx
