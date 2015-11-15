def bisect(f, a, b, tol=10e-5):
    if b-a < tol:
        return (a+b)/2
    elif f((a+b)/2) > 0:
        return bisect(f=f, a=a, b=(a+b)/2)
    else:
        return bisect(f=f, a=(a+b)/2, b=b)

#赠品
#矿工面试题：一句话（一行语句）给出计算Fibonacci第N项数值的函数定义（不能使用Closed Form公式）
Fibonacci = lambda n: 1 if n<3 else Fibonacci(n-1) + Fibonacci(n-2)
