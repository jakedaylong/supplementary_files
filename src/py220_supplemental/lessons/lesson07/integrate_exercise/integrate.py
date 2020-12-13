def f(x):
    return x**2

def integrate(f, a, b, N):
    s = 0
    dx = (b-a)/N
    for i in xrange(N):
        s += f(a+i*dx)
    return s * dx
