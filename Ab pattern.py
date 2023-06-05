l=int(input("l:"))

b=int(input("b:"))

for i in range(1,b+1):
      
      for j in range(1,l+1):
          
          if i==1 or i==b:
          
              if j%2!=0:
              
                  print('A',end=" ")
              
              else:
                  
                  print('b',end=" ")
                  
          elif j==1 or j==l:
              
              print('A',end=" ")
              
          else:
              
              print(end="  ")
              
      print("\n")      