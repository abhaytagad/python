
X=[[1, 2, 3],
       [4, 5,6],
       [7, 8, 9]]
       
Y=[[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]
r=[[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]      
for i in range(len(X)):
    for j in range(len(X[0])):
        r[i][j]=X[i][j]+Y[i][j]
            
print(r)            