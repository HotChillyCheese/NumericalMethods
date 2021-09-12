import matplotlib.pyplot as plt
import numpy as np

def feval(funcName, *args):
    return eval(funcName)(*args)


def backwardEuler(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0])/h)

    x = x_range[0]
    y = yinit

    xsol = np.empty(0)
    xsol = np.append(xsol, x)

    ysol = np.empty(0)
    ysol = np.append(ysol, y)

    for i in range(n):
        yprime = feval(func, x+h, y)/(1+h)

        for j in range(m):
            y[j] = y[j] + h*yprime[j]

        x += h
        xsol = np.append(xsol, x)

        for r in range(len(y)):
            ysol = np.append(ysol, y[r])  # Saves all new y's

    return [xsol, ysol]


def myFunc(x, y):
    '''
    We define our ODEs in this function.
    '''
    # dy = np.zeros((len(y)))
    # dy[0] = 3*(1+x) - y[0]
    dy = np.zeros((len(y)))
    dy[0] = x+y[0]*y[1]
    dy[1] = x*y[1] + y[0]
    # a = 1; b = 5; c = 4; r = 1; y0 = 0; epsi = 0.1
    # dy[0] = ((a + b*y[0]**2)/(1 + y[0]**2 + r*y[1])) - y[0]
    # dy[1] = epsi*(c*y[0] + y0 - y[1])
    return dy


h = 0.2
x = np.array([5.0, 10.0])
yinit = np.array([1.0,1.0])


[ts, ys] = backwardEuler('myFunc', yinit, x, h)

ys1 = ys[0::2]
ys2 = ys[1::2]
print(ys1, ys2)
plt.plot(ts,ys1, 'r')
plt.plot(ts,ys2, 'b')
plt.xlim(x[0], x[1])
plt.legend(["y1", "y2"], loc=1)
plt.xlabel('X', fontsize=17)
plt.ylabel('Y', fontsize=17)
plt.title("Cauchy Problem")
plt.tight_layout()
plt.show()
# plt.plot(ts, ys, 'r')
# plt.plot(t, yexact, 'b')
# plt.xlim(x[0], x[1])
# plt.legend(["Backward Euler method",
#             "Exact solution"], loc=2)
# plt.xlabel('x', fontsize=17)
# plt.ylabel('y', fontsize=17)
# plt.tight_layout()
# plt.show()