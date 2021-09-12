import numpy as np
import matplotlib.pyplot as plt

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        print("function f is",fxn)
        if abs(fxn) < epsilon:
            print('Found solution after', n ,'iterations')
            return xn
        Dfx0=Df(x0)
        print("Derivative is ", Dfx0)
        if Dfx0 == 0:
            print('Zero derivative. No solutions can be found')
            return None
        xn = xn-fxn/Dfx0
    print('Exceeded maximum iterations. No solutions found')
    return None



f = lambda x: x**3 - 4*x**2-7*x+13
Df = lambda x: 3*x**2-4*2*x-7
approx = newton(f,Df, 1.1, 1e-10, 100)
print(approx)

x = np.linspace(-5, 5,1000)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, x**3 - 4*x**2-7*x+13)
# plt.plot(x,np.linspace(0,0,1000))
plt.plot(approx,f(approx),'bo')

plt.show()

#1.2461925945764534 - Newton
#1.246192594576251 - Modified Newton
#1.2462737671792723 - Relaxation