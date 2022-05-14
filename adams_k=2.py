import matplotlib.pyplot as plt
import math

a, b = 0, 1
y0 = 3
N = [10, 20, 30]


def f(x, y):
    return 1 / (x + 1)


def y_precise(x):
    return math.log(abs(x + 1), math.e) + 3


def runge_kutta(x, y, h):
    k1 = h * f(x, y)
    k2 = h * f(x + h / 2, y + k1 / 2)
    k3 = h * f(x + h / 2, y + k2 / 2)
    k4 = h * f(x + h, y + k3)
    return y + (k1 + 2 * k2 + 2 * k3 + k4) / 6


def adams(n):
    x_res = [a]
    y_res = [y0]
    h = (b - a) / n
    y_res.append(runge_kutta(x_res[0], y_res[0], h))
    x_res.append(a + h)
    x = a + h
    for i in range(1, n):
        y = y_res[i] + h / 12 * (5 * f(x + h, None) + 8 * f(x, None) - f(x - h, None))
        y_res.append(y)
        x += h
        x_res.append(x)
    return x_res, y_res


for n in N:
    x, y = adams(n)
    plt.plot(x, y, label=f"N={n}")

x_data = [a + i * (b - a) / 300 for i in range(301)]
y_data = list(map(y_precise, x_data))
plt.plot(x_data, y_data, label="y(x)")
plt.legend()
plt.show()
