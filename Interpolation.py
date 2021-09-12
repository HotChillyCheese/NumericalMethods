import numpy as np
import matplotlib.pyplot as plt
 
def proterm(i, value, x):  
    pro = 1  
    for j in range(i):  
        pro = pro * (value - x[j])  
    return pro  
  
def dividedDiffTable(x, y, n): 

    
    for i in range(1, n):  
        for j in range(n - i):  
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]))
    return y
  
 
def applyFormula(value, x, y, n):  
  
    sum = y[0][0]  
  
    for i in range(1, n): 
        sum = sum + (proterm(i, value, x) * y[0][i])
    coef = [ "" for j in range(n)]
    var = ["" for j in range(len(x))]
    for k in range(0,n):
        coef[k] = str(round(y[0][k],2))
        var[k] = str(x[k])
    pol = coef[0]
    for k in range(1,n):
        pol += "+(" + coef[k]+ ")"
        for m in range(k):
            pol += "*(x-(" + var[m] +"))"
    print("The polynomial looks like this: ", pol, "\n")
    # print("0.07 p^4 + 0.29 p^3 + 0.6 p^2 + 1.04 p + 0.99")
    p = np.linspace(x[0]-5,x[len(x)-1]+5,1000)  # Create a list of evenly-spaced numbers over the range
    plt.plot(p,0.01+(0.02)*(p-(-4))+(0.02)*(p-(-4))*(p-(-3))+(0.02)*(p-(-4))*(p-(-3))*(p-(-2))+(0.01)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))+(0.0)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))*(p-(0))+(0.0)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))*(p-(0))*(p-(1))+(0.0)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))*(p-(0))*(p-(1))*(p-(2))+(0.0)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))*(p-(0))*(p-(1))*(p-(2))*(p-(3))+(0.0)*(p-(-4))*(p-(-3))*(p-(-2))*(p-(-1))*(p-(0))*(p-(1))*(p-(2))*(p-(3))*(p-(4)))
    plt.plot(p,2/3*p**2+3/4*p +1)
    for k in range(n):
        plt.plot(x[k], y[k][0], 'bo')
    plt.show()
    return sum  
  
def printDiffTable(x, y, n):  
  
    for i in range(n):
        print("\n",x[i])  
        for j in range(n - i):  
            print(round(y[i][j], 4), "\t",  
                               end = " ")  
  
        print("")  
  
# Driver Code 
  
n = 10  
y = [[0 for i in range(20)]  
        for j in range(20)]  
f = lambda x: 3**x
x = [ -4,-3,-2,-1, 0, 1,2,3,4,5 ]  

for i in range(n):
    y[i][0] = f(x[i])  
# y[0][0] = 1  
# y[1][0] = -2  
# y[2][0] = 5  
# y[3][0] = 7 
# y[4][0] = -10
M= (3**x[len(x)-1])*np.log(3)**n
factorial = 1
for i in range(1,n+2):
    factorial*=i
print("!!!!!",factorial)
# r= M/factorial *    

y=dividedDiffTable(x, y, n)  
    
printDiffTable(x, y, n)  
print("\n\n")
  
value = 7  
  
print("\nValue at", value, "is", 
        round(applyFormula(value, x, y, n), 2)) 