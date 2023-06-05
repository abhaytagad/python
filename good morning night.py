import time

print("Enter your name:")
name=input()
H=int(time.strftime('%H'))
if (0<=H<=12):
    print("Good morning",name)
    
elif(12<H<=15):
    print("Good afternoon", name)
elif(15<H<=20):
    print("Good evining",name)
    
elif(20<H<=24):
    print("Good night",name)

