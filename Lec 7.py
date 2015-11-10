def bisect(f, a, b, tol=10e-5):
    if b-a < tol:
        return (a+b)/2
    elif f((a+b)/2) > 0:
        return bisect(f=f, a=a, b=(a+b)/2)
    else:
        return bisect(f=f, a=(a+b)/2, b=b)
