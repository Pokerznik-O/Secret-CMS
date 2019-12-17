def true(x):
    return (-0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1)

y0 = 1

import numpy as np
import matplotlib.pyplot as plt 


def f(x):
    return (-2*x**3 + 12*x**2 - 20*x + 8.5)

def y_2(low, high, step):
    y = y0
    y2 = y0
    n = int((high - low)/step) #this is een float, so you need to make it an integer 
    true_list = []
    approximation_list = []
    new_list = []
    #new value = old value + slope times the step 
    for i in range(n):
        k1 = f(i*step)
        k2 = f(i*step + (step/2))
        k3 = f(i*step + step)
        #there is no y dependence so you don't have to add the change of the y variable 
        approximation_list.append(y)
        y = y + (1/6)*((k1 + 4*k2 + k3)*step)
        #y2 = (1/3)*y + (2/3)*y(i*h + (3/4)*h, y + (3/4)*y)
        true_value = true(i*step)
        true_list.append(true_value)
        #print(true_value)
        error = ((abs(true_value - y))/true_value)
        #print(error)
    return approximation_list, true_list, error


y_2(0., 4., 0.5)

