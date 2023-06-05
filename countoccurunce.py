s=str(input("enter the string:"))
w=str(input("enter the word:"))
x=0
for t in s.split():
    if w==t:
        x+=1
print(x)