

x=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        
            b=int(input("enter the element:"))
            x[i][j]=b
print(" x=",x)
 
r=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i]=x[i][j]
        
print("transpose of matrix x=",r)        