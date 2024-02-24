tup = (1, 2, 76, 342, 32, "Black", True)
# tup[0] = 90 # TypeError: 'tuple' object does not support item assignment
print(tup)
print(type(tup)) # <class 'tuple'>
print(len(tup)) # 7
print(tup[0]) # 1
print(tup[-1]) # True
print(tup[2]) # 76

if 342 in tup:
    print("Yes")
else:
    print("No")
    
tup2 = tup[1:4]
print(tup2) # (2, 76, 342) # It's a new tuple