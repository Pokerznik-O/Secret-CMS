import numpy as np
import matplotlib.pyplot as plt

def function(x):
    return x**4 + 2*x + 1
#bisection method
def root_bisection(xu, xl):
    if function(xu) * function(xl) > 0:
        return print("That's a bad guess.")
    else:
        for i in range(10):
            xn = (xu + xl)/2
            value = function(xn)
            if function(xl) * value < 0:
                xu = xn
            elif function(xu) * value < 0:
                xl = xn
            else:
                return xn
        return xn
    
#Homework: edit so that it exits when error is small enough

root_bisection(-1.2, -0.7)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 0.5, 100)
y = x**4 + 2*x + 1
#array with all elements = 0 with length of the array of x

plt.plot(x, y)
