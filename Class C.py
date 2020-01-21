import numpy as np
import matplotlib.pyplot as plt


rng = np.random.RandomState(37)
mu, sigma = 10, 2
x = np.random.normal(mu, sigma, 100)
y = x + rng.randn(100)
#plt.scatter(x, y)

x2 = (x - np.mean(x))/(np.std(x))
y2 = (y - np.mean(y))/(np.std(y))
plt.scatter(x2, y2)

cov = np.cov(x, y)

v, w = np.linalg.eig(cov)

print(w)

print(np.dot(w[0], w[1]))

plt.plot((0, w[0][0]), (0, w[0][1]))
plt.plot((0, w[1][0]), (0, w[1][1]))
