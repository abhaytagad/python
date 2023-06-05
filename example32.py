L=[]
n=int(input(" enter the len of array:"))
cout=0
while cout<n:
    ele=int(input("enter the element:"))
    L.append(ele)
    cout+=1
mul=1

for i in range(len(L)):
    mul=mul*L[i]
for i in range(len(L)):
    if L[i]==mul/L[i]:
        print(L[i])