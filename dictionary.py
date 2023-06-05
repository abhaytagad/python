d1 = { "Abhay" : 20, "Asmita" : 24 , "Papa" : 46 , "Mhatari":42}
print(d1["Mhatari"])

d1["Aniket"] = 22 # we can add information in dictionary by using it
print(d1)
d1["Dada"]={ 2020 : 70, 2019 : 71 } # by using this function we can another dictionary in the old
print(d1)
print(d1["Dada"] [2020]) # this will print the object from the inner dictionary
del d1["Dada"]  # this will delete the element from dictionary
print(d1)

d2=d1.copy() # this will make the new dictionary which will be the copy of old one s
#del d2["Abhay"]
print(d2)

d2.update({"mammi":43}) # we can update element in dictionary
print(d2)

print(d2.keys())

print(d2.items())
