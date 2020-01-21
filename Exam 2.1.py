import math

def f(x):
    return math.log(x, math.e)

def inter(x, x0, x1):
    fx0 = f(x0)
    fx1 = f(x1)
    fx = fx0 + ((fx1 + fx0)/(x1 - x0))*(x - x0)
    return fx

inter(2, 1, 2.5)
#interpolation
