L=[]
x=0
n=int(input("enter the size of array:"))
while x<n:
    e=int(input("enter the element of array:"))
    L.append(e)
    x+=1
print(L)
print("the absolute differnce between first and last element of array:",abs(L[0]-L[n-1])) 