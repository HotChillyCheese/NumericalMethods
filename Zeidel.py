import numpy as np

def Inverse(M):
    l=len(M[0])
    Temp=np.zeros((l,2*l))
    for i in range(l):
        for j in range(l):
            Temp[i,j]=M[i][j]
    for i in range(l):
        Temp[i,i+l]=1
    #Forward
    for j in range(l):
        if(Temp[j][j]!=0):
            for i in range(j+1,l):
                Temp[i]=Temp[i]-Temp[j]*Temp[i][j]/Temp[j][j]
    #Backward
    for j in range(l):
        Temp[j]=Temp[j]/Temp[j][j]
    for j in range(l-1,0,-1):
        mult=Temp[j]
        for i in range(j-1,-1,-1):
            Temp[i]=Temp[i]-Temp[i][j]*mult
    for i in range(l):
        for j in range(2*l):
            Temp[i,j]=round(Temp[i][j],3)
    Res=np.empty((l,l))
    for i in range(l):
        for j in range(l):
            Res[i,j]=Temp[i][l+j]
    return Res

def seidel(a, x ,b,epsilon): 
    temp = [0,0,0]
    for k in range(0,100):  
        n = len(a)                    
        # for loop for 3 times as to calculate x, y , z 
        for j in range(0, n):         
            # temp variable d to store b[j] 
            d = b[j]                   
            
            # to calculate respective xi, yi, zi 
            for i in range(0, n):      
                if(j != i): 
                    d-=a[j][i] * x[i] 
            # updating the value of our solution         
            x[j] = d / a[j][j] 
            # returning our updated solution
        print(k,x)
        Conv = [0,0,0]
        for u in range(3):
            Conv[u] = abs(x[u]-temp[u])
        conv = max(Conv)
        temp = x[:]
        if (conv<epsilon):
            return x
    return x     
# int(input())input as number of variable to be solved                 
n = 3                              
a = []                             
b = []         
# initial solution depending on n(here n=3)                      
x = [0, 0, 0]                         
a = [[3, -1, 1],[-1, 2, 0.5],[1, 0.5, 3]] 
b = [1,1.75,2.5] 
epsilon = 0.0001
print(x)
#loop run for m times depending on m the error value 
# for i in range(0, 10):             
#     x = seidel(a, x, b) 
#     print(i,x)
print(seidel(a,x,b,epsilon))
invA= Inverse(a)
print("Inverse Matrix")
print(invA)
normA = [0,0,0]
normInvA = [0,0,0]
# for j in range(n):
#     normA+=max(a[j][0:n])
#     normInvA+=max(invA[j][0:n])
for j in range(n):
    for i in range(n):
        normA[j]+=abs(a[i][j])
        normInvA[j] += abs(invA[i][j])
normreg = max(normA)
norminv = max(normInvA)
print("Conditional Number", normreg*norminv)
# cond=normA*normInvA
#print(cond)
# print("Conditional Number", np.linalg.cond(a))
print("Determinant", np.linalg.det(a))