import numpy as np
import matplotlib.pyplot as plt
import math as m

def relaxation(f,Df, phi, Dphi,x0,epsilon, max_iter):
    xn=x0
    a = 0.5
    b =1.5
    m1 = Dphi(a)
    M1 = Dphi(b)
    tau = 2/(M1+m1)
    print(tau)
    for n in range (0,max_iter):
        fxn = f(xn)
        print("function f is", fxn)
        if abs(fxn) < epsilon:
            print('Found solution after', n ,'iterations')
            return xn
        xn = xn + tau*fxn # +/- depending on the derivative
    print("Exceeded maximum iterations")
    return None

f = lambda x: x**3 - 4*x**2-7*x+13
phi = lambda x: 4 + 7/x +13/(x**2)
Dphi = lambda x: 7  * (-1)/(x**2) + 13 *(1/x**3)
Df = lambda x: 3*x**2-4*2*x-7
x0=1.25
epsilon = 0.001 
approx = relaxation(f,Df,phi, Dphi, x0, epsilon, 5000)
print(approx)
z0 = abs(x0 - approx)
a = z0/epsilon
c = 0.5
d = 1.5
m1 = Dphi(c)
M1 = Dphi(d)
q = (M1-m1)/(m1+M1)
b = 1/abs(q)
Prior_evaluation = int(m.log(a)/m.log(b)) +1
print(Prior_evaluation)
x = np.linspace(-5, 5,1000)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, x**3 - 4*x**2-7*x+13)
plt.plot(x,np.linspace(0,0,1000))
plt.plot(approx,f(approx),'bo')
plt.show()