import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

rng = np.random.default_rng()

x = 3
y = np.arange(1, 11)
z = [1,5,10.2,-54]
r = [1,1,1,2,3,4,1,1,5,6]

print(x)
print(y)
print(x + y)
print(y ** 2)

z[1] = z[3] * 2
print(z)

print([i for i in range(len(r)) if r[i] == 1])
for i in range(len(r)):
    if r[i] == 1:
        r[i] = 9
print(r)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(x * y)

print(x @ y)

def rcnorm(n, mean, sd, c):
    cnt = 0
    sam = []
    while True:
        x = rng.normal(mean, sd)
        if x > c:
            cnt += 1
            sam.append(x)
        if cnt == n:
            break
    return sam

print(rcnorm(10, 1, 2, 3))

plt.figure(figsize=(6, 4))
plt.hist(rng.normal(0, 1, 1000), bins=30, color='orange')
plt.show()

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    return (h / 2) * np.sum(y[:-1] + y[1:])

def monte_carlo_integration(f, a, b, n):
    x = rng.uniform(a, b, n)
    y = f(x)
    return (b - a) * np.mean(y)

def scipy_integration(f, a, b):
    return quad(f, a, b)[0]

print(trapezoidal_rule(np.sin, 0, 1, 100))
print(monte_carlo_integration(np.sin, 0, 1, 100))
print(scipy_integration(np.sin, 0, 1))
