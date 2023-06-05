
num=int(input("enter the number :"))

flag=True

if num==0 or num==1:

    print(num,"is not a prime")

elif num<0:
    print("invalid input")

else:
    for i in range(2,num):
        if num%i==0:
    
            flag=False

            break
if flag==True:
    print(num,"is prime number")

else:

    print(num,"is not a prime number")