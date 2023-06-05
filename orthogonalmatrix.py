L=[[0,0,0],[0,0,0],[0,0,0]]

r=int(input("enter if there is any scalar taken out of the matrix:"))


for i in range(len(L)):


    for j in range(len(L)):

        n=int(input("enter the element:"))

        L[i][j]=float(n/r)
        

print(L)

A=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):

    for j in range(len(A)):

        A[i][j]=L[j][i]

print(A)

LA=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(L)):

    for j in range(len(L)):

        for k in range(len(L)):

            LA[i][j]+=L[i][k]*A[k][j]

print(LA)

I=[[1,0,0],[0,1,0],[0,0,1]]

if LA==I:

    print("given matrix is orthogonal matrix:")

else:

    print("given matrix is not orthogonal matrix:")