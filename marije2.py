#Gradient descent cost function 

import numpy as np 
import matplotlib.pyplot as plt 

rng = np.random.RandomState(42)
x = 10 * rng.rand(500)
y = 4*x**3 + 1 + 10*rng.randn(500)
plt.scatter(x,y)

def F(x, y, a, c):
    err = 0. 
    n = len(y)
    for i in range(n): 
        err = err + (y[i] - ((a*x**3)[i] + c))**2    
    E = err/(2*n)
    return E

F(x,y, 2, -1)
#check derivative 
def derivative(x,y,a,c):
    f = y - (a*x**3 + c)
    dfa = f * (-x**3)
    #dfb = f * (-x)
    #there is no b so we do not have to use this 
    dfc = f * (-1)
    return np.sum(dfa)/(len(y)), np.sum(dfc)/(len(y))
#np.sum(dfb)/(len(y))
derivative(x,y, 4, 1)

def GD(a,c):
    for i in range(10000):
        df = derivative(x, y, a, c)
        a = a - (0.0001 * df[0])
        #first derivative 
        #b = b - (0.0001 * df[1])
        #second derivative 
        c = c - (0.0001 * df[1])
        #third derivative 
    return a, c

GD(4, 1)

solution = GD(4, 1)
y2 = solution[0]*(x**3) + solution[1]

#ym = a*(x**3) + c
plt.scatter(x,y)
plt.scatter(x,y2)
