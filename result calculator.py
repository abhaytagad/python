s1=int(input(" enter the marks of the subject s1:"))
s2=int(input(" enter the marks of the subject s2:"))
s3=int(input(" enter the marks of the subject s3:"))
s4=int(input(" enter the marks of the subject s4:"))
s5=int(input(" enter the marks of the subject s5:"))
gap="|"
print("_"*43)
print(f"{gap} {'subject':7s} {gap} {'marks out of  100':13s} {gap} {'  grade':9s} {gap}")
print("_"*43)
s=[s1,s2,s3,s4,s5]
g=['FC','SC','TC','F']
b=['s1','s2','s3','s4','s5']
sum=0
for i in range(0,5):
    if s[i]>=40 and s[i]<50:
     
         print(f"{gap} {b[i]:^7s} {gap} {s[i] :^17d} {gap}     {g[2]:5s} {gap}")
    elif s[i]>=50 and s[i]<60:
         print(f"{gap} {b[i]:^7s} {gap} {s[i] :^17d} {gap}     {g[1]:5s} {gap}")
     
          
    elif s[i]>=60 and s[i]<=100:
          print(f"{gap} {b[i]:^7s} {gap} {s[i]:^17d} {gap}     {g[0]:5s} {gap}")
    else:
          print(f"{gap} {b[i]:^7s} {gap} {s[i] :^17d} {gap}     {g[3]:5s} {gap}")
          
    sum+=s[i]
          
 
print("_"*43) 
#print(sum)  
score_aggregate=(sum/500)*100

print(f" score aggregate:{sum/500:%}")    

if score_aggregate>=75:
        print(" with distinction")   
        