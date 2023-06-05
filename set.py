s={1,2,2,3,4,7,8,9,9,}
print(s)
print(type(s)) # set does not reapete the element
s1={2,6,5,4,7,8,7}
print(s.union(s1)) # this function will merge two sets
s.update(s1) # this will update set 
print(s)

s3=s.intersection(s1)    # this will take the intersection of the two sets
print(s3)
s.intersection_update(s1)
print(s)
