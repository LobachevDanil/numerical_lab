import matplotlib.pyplot as plt
import math

a, b = 0, 1
y0 = 3
N = [10, 20, 30]


def f(x, y):
    return 1 / (x + 1)


def y_precise(x):
    return math.log(abs(x + 1), math.e) + 3


def explicit_euler(n):
    x_res = [a]
    y_res = [y0]
    h = (b - a) / n
    x = a
    for i in range(n):
        y = y_res[i] + f(x, y_res[i]) * h
        y_res.append(y)
        x += h
        x_res.append(x)
    return x_res, y_res


for n in N:
    x, y = explicit_euler(n)
    plt.plot(x, y, label=f"N={n}")

x_data = [a + i * (b - a) / 300 for i in range(301)]
y_data = list(map(y_precise, x_data))
plt.plot(x_data, y_data, label="y(x)")
plt.legend()
plt.show()
