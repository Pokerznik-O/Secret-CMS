import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(42)
x = 10 * rng.rand(500)
y = 4*x**3 + 1 + 10*rng.randn(500)
plt.scatter(x, y)
#plt.plot(x, 2*x**2 + 10*x - 1)

def F(x, y, a, c):
    e = 0.
    for i in range(len(y)):
        e = e + (y[i] - ((a*x**3)[i] + c))**2
    return e/(2*(len(y)))

F(x, y, 4, 1)

def derivative(x, y, a, c):
    f = y - (a*x**3 + c)
    dfa = f*(-x**3)
    dfc = f*(-1)
    return np.sum(dfa)/len(y), np.sum(dfc)/len(y)

print(derivative(x, y, 4, 1))

def gradient_descent(x, y, a, c):
    function = []
    for i in range(100000):
        df = derivative(x, y, a, c)
        a = a - 0.00001*df[0] 
        c = c - 0.00001*df[1]
        f = a*x**3 + c
        function.append(f)
    return round(a), round(c), function

solution = gradient_descent(x, y, 4, 1)
y2 = solution[0]*(x**3) + solution[1]

plt.scatter(x, y2)
