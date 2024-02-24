list_A = [11, 45, 1, 2, 4, 6, 1, 1]

list_M = list_A.copy()  # returns copy of the list without modifying original list.
list_A.insert(1, 89)  # inserts an item at the given index.
print(list_A) # [11, 89, 45, 1, 2, 4, 6, 1, 1]

list_M = [90, 60, 40]
list_K = list_A + list_M
print(list_K) # [11, 89, 45, 1, 2, 4, 6, 1, 1, 90, 60, 40] 

list_A.extend(list_M)  # adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print(list_A) # [11, 89, 45, 1, 2, 4, 6, 1, 1, 90, 60, 40]  