S1="code zinger university"
S2="university"
space=" "
start=0
for i in range(len(S1)):
    result=""
    
    if S1[i]==space:
        for j in range(start,i):
            result+=S1[j]
            
        start=i+1
        if result==S2:
            print(start-1-len(result))
            
         
    elif i==len(S1)-1:
         
         for j in range(start,i+1):
            result+=S1[j]
            
         start=i+1
         
         if result==S2:
            print(start-len(result))         