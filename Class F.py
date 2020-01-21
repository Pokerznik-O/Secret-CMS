v = lambda x: 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)
exact = 1.640533

def trapezoid(f, a, b):
    h = b - a
    trapezoid = h * (f(a) + f(b))/2
    return trapezoid

I = trapezoid(v, 0, 0.8)
print("Calculated value: %f" %I)

def multi_trapezoid(f, a, b, n):
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

I2 = multi_trapezoid(v, 0, 0.8, 10)
error = abs(exact - I2)*100/exact
print("Calculated value: %f" %I2)
print(error)

def simpson13(f, a, b):
    return (b-a)/6 * (f(a) + 4*f((b+a)/2) + f(b))

I3 = simpson13(v, 0, 0.8)
print("Calculated value: %f" %I3)

def multi_simpson13(f, a, b, n):
    h = (b-a)/n
    k = 0
    x = a + h
    for i in range(1, int(n/2) + 1):
        k += 4*f(x)
        x += 2*h
    x = a + 2*h
    for i in range(1, int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a) + f(b) + k)

I4 = multi_simpson13(v, 0, 0.8, 4)
print("Calculated value: %f" %I4)

def simpson38(f, a, b):
    h = (b - a)/3
    n = (b - a)/h
    sum_ = f(a) + f(b)
    sum_ = sum_ + 3*(f(a+h))
    sum_ = sum_ + 3*(f(a + 2*h))
    return ((float(3*h)/8) * sum_)

I5 = simpson38(v, 0, 0.8)
print("Calculated value: %f" %I5)
