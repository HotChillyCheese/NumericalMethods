import numpy as np
from numpy import linalg as LA
from numpy.linalg import matrix_power

def dotMethod(M):
    l = len(M)
    X=np.ones(l)#*1/(l)**1/2
    Zk=M.dot(X)
    print(X)
    print(Zk)
    MaxEigenI=0
    MaxEigenINext=np.dot(Zk,X)/np.dot(X,X)
    XNext=Zk/LA.norm(Zk)
    print(MaxEigenINext)
    print(XNext)
    n=1
    while(abs(MaxEigenI-MaxEigenINext)>10**-4):
        X=XNext
        Zk=M.dot(XNext)
        MaxEigenI=MaxEigenINext
        MaxEigenINext = np.dot(Zk,X)/np.dot(X,X)
        XNext=Zk/LA.norm(Zk)
        print(XNext)
        n+=1
    EigenVector=XNext/MaxEigenINext
    return MaxEigenINext,EigenVector,n

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
    

#Метод скалярних добутків з точністю epsillon=10^-4 знайти максимальне та мінімальне за модулем власні значення та власні вектори
#A = np.array([[1.,0.5, 1./3],[0.5,1./3,0.25],[1./3,0.25,0.2]])
A = np.array([[2.2,1.,0.5,2.],[1.,1.3,2.,1.],[0.5,2.,0.5,1.6],[2.,1.,1.6,2.]])
l = len(A)
MaxEv,EigVec,r=dotMethod(A)#отримаємо максимальне за модулем власне значення та його вектор
inv=Inverse(A)

MaxEv1,EigVecM,n=dotMethod(inv)#максимальне для оберненої матриці та кількість ітерацій
MinEv=1/MaxEv1#мінімальне за модулем власне значення
X=np.ones(l)#*1/(l)**1/2
EigVecM=matrix_power(inv,n).dot(X)
print(MaxEv,EigVec)
print(MinEv,EigVecM/LA.norm(EigVecM))