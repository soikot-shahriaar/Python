# update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)  # {122: 45, 123: 89, 567: 69, 670: 69, 222: 67, 566: 90}

# clear() method removes all the items from the list.
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
print(ep1.clear())  # None

# pop() method removes the key-value pair whose key is passed as a parameter.
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
print(ep1.pop(122))  # 45

# popitem() method removes the last key-value pair from the dictionary.
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
print(ep1.popitem())  # (670, 69)

# the del keyword to remove a dictionary item.
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
del ep1[122]
print(ep1)  # {123: 89, 567: 69, 670: 69}