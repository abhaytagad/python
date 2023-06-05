L=[]
x=0
n=int(input("enter the size of array:"))
while x<n:
    e=int(input("enter the element of array:"))
    L.append(e)
    x+=1
print(L)
b=0
print("the inversions are:")
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]>L[j] and i<j:
            print((L[i],L[j]))
            b+=1
print("the inversion count is :",b)