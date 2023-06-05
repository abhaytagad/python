n=int(input("how many numbers ?:"))


for i in range(1,n):
    if i%4==0 and (i%100)!=0 or i%400==0:
        print(f"the {i} is a leep year")
        
    