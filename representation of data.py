gap="|"
fmt=f"{gap} {' Year':5s} {gap} {'Starting balance':16s} {gap} {' Interest':9s} {gap} {'Ending balance':13s} {gap}"
print("_"*57)
print(fmt)
print("_"*57)
L=[["Year",'Starting balance','interest','Ending values'], [1, 10000, 500, 10500],[2, 10500,525,11025],[3,11025,551.25,11576.25],[4,11576.25,578.81,12155.06],[5,12155.06, 607.75, 12762.82]]

for data in L[1:] :
    rec=f"{gap} {data[0]:5d} {gap} {data[1]:16.2f} {gap} {data[2]: 9.2f} {gap} {data[3]:14.2f} {gap}"
    print(rec)
print("_"*57)
h=L[5]
print(" Ending balance :","$",h[3])
b=0
for i in L[1:]:
    b=b+i[2]
print(" Total intrest earned","$",b)