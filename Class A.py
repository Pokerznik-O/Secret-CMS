def phi(x):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

y0 = 1

def y(h, mini, maxi):
    y = y0
    n = int((maxi - mini)/h)
    for i in range(n):
        y = y + phi(i*h)*h
        print(y)

y(0.5, 0, 4)

import numpy as np
import matplotlib.pyplot as plt

def phi(x):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def function(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

y0 = 1

def y(h, mini, maxi):
    y = y0
    n = int((maxi - mini)/h)
    solutions_app = []
    solutions = []
    x = []
    for i in range(n):
        solutions_app.append(y)
        y = y + phi(i*h)*h
        #print(y)
        true = function(i*h)
        solutions.append(true)
        x.append(i*h)
        #print(true)
        #error = ((abs(true - y))/true)*100
        #print(error)
    return solutions_app, solutions, x

out = y(0.1, 0, 4)

plt.plot(out[2], out[0])
plt.plot(out[2], out[1])

import matplotlib.pyplot as plt


def function(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
    
def phi(x):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

y0 = 1

def y(h, mini, maxi):
    y = y0
    y2 = y0
    n = int((maxi - mini)/h)
    solutions_app = []
    solutions_app_2 = []
    #solutions_app_2.append(y)
    solutions = []
    x = []
    for i in range(n):
        solutions_app.append(y)
        solutions_app_2.append(y2)
        y = y + phi(i*h)*h
        true = function(i*h)
        solutions.append(true)
        x.append(i*h)
        k1 = phi(i*h)
        k2 = phi(i*h + (3/4)*h)
        y2 = y2 + ((1/3)*k1 + (2/3)*k2)*h
    return solutions, solutions_app, solutions_app_2, x

out = y(0.5, 0, 4)

plt.plot(out[3], out[0])
plt.plot(out[3], out[1])
plt.plot(out[3], out[2])
