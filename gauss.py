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
    

#Gauss Method
A=np.array([[1.,-1.,1.,-1.,2.,1.,0.,0.,0.],[-1.,5.,-3.,3.,-4.,0.,1.,0.,0.],[1.,-3.,-7.,1.,-18.,0.,0.,1.,0.],[-1.,3.,1.,10.,-5.,0.,0.,0.,1.]])
Res,det,cond,normA,normInvA,st=A,1,0,0,0,''
a1 = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        a1[i,j] = A[i][j]
L=np.array([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]])
U=np.array([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]])
inv=np.zeros((4,4))

#Forward
n=0
for j in range(4):
    if(Res[j][j]!=0):
        det*=Res[j][j]
        for i in range(j+1,4):
            cof=Res[i][j]/Res[j][j]
            Res[i]=Res[i]-Res[j]*cof
            n+=1
            print(Res,n)
            L[i,j]=cof
for j in range(4):
    L[j,j]=1
for j in range(4):
    for i in range(j,4):
        U[j,i]=Res[j][i]
#Backward
for j in range(4):
    Res[j]=Res[j]/Res[j][j]
    print(Res)
for j in range(3,0,-1):
    mult=Res[j]
    for i in range(j-1,-1,-1):
        Res[i]=Res[i]-Res[i][j]*mult
    print(Res)
for j in range(4):
    normA+=max(A[j][0:4])
    normInvA+=max(A[j][5:9])
cond=normA*normInvA
#output
print(Res)
print("Determinant:",det)
print("Cond:",cond)
for i in range(4):
    print('x'+str(i)+'='+str(Res[i][4]))
print("Inverse:")
for i in range(4):
    for j in range(5,9):
        st+=str(round(Res[i][j],2))+' '
        #a1[i,j-5] = A[i][j-5]
        inv[i,j-5]=Res[i][j]
    print(st)
    st=''
print(inv)
print(a1)
a2 = Inverse(a1)
print("Inverse M", a2)
print("L*U:")
for i in range(4):
    for j in range(4):
        st+=str(round(L[i][j],2))+' '
    st+='  '
    for j in range(4):
        st+=str(round(U[i][j],2))+' '
    print(st)
    st=''
print(a1)
invAA= np.dot(a1,a2)
#print(np.dot(a1,a2))
temp=np.zeros((4,4))
for i in range(4):
    for j in range(4):
        temp[i,j] = round(invAA[i][j],1)

a3 = np.dot(a1,inv)
#print(np.dot(a1,inv))
temp1 = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        temp1[i,j] = round(a3[i][j],1)
print(temp)
print(temp1)