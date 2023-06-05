x=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        
            b=int(input("enter the element:"))
            x[i][j]=b
print(" x=",x)
y=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(y)):
    for j in range(len(y[0])):
        
            b=int(input("enter the element:"))
            y[i][j]=b
print(" y=",y)
sum=0
r=[[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
            for  k in range(len(y)):
                r[i][j]+=x[i][k]*y[k][j]
       
print("the multiplication xy=",r)     