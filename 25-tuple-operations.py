# # Manipulating Tuples
# Tuples are immutable, hence if we want to add, remove or change tuple items, then first we must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

# Tuple Operations
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2)
print(len(tuple1)) # 9
print(tuple1.count(3)) # 2
print(tuple1.index(1)) # 1
print(tuple1.index(3, 4, 8)) # 7