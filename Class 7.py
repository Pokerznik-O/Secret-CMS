import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(42)
x = 10 * rng.rand(500)
y = 2*x - 1 + rng.randn(500)
plt.scatter(x, y)
plt.plot(x, 2*x - 1)

def F(x, y, a, b):
    e = 0.
    for i in range(len(y)):
        e = e + (y[i] - (a*x[i] + b))**2
    return e/(2*(len(y)))

F(x, y, 2, -1)

def derivative(x, y, a, b):
    f = y - (a*x + b)
    dfa = f*(-x)
    dfb = f*(-1)
    return np.sum(dfa)/len(y), np.sum(dfb)/len(y)


print(derivative(x, y, 2, -1))

print((F(x, y, 2.0001, -1) - F(x, y, 2, -1))/0.0001) 
print((F(x, y, 2, -0.9999) - F(x, y, 2, -1))/0.0001)
    
