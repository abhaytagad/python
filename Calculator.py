
'''def add(a,b):
    print(a+b)
def sustr(a,b):
    return a-b
    
def mult(a,b):
    return a*b
    
def div(a, b):
    
    return a/b'''
    
print("select the opperation:", "\n +","\n -","\n ×","\n /","\n //")

S=input()
print("enter the first number:")
a=int(input())
print("enter the second number:")
b=int(input())
print("answer is :")
if  S=="+":
    z=a+b
    print(z)
   # print(add)
elif  S=="-":
    x=a-b
    print(x)
   #print(sustr)
elif S=="×":
    m=a*b
    print(m)
    #print(mult)
elif S=="/":
    d=a/b
    print(d)
   #prin(div)
elif S=="//":
    t=a//b
    print(t)
 