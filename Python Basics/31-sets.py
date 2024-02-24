# # Python Sets
# Sets are unordered collection of data items. They store multiple items in a single variable.
# Set items are separated by commas and enclosed within curly brackets {}.
# Sets are unchangeable, meaning we cannot change items of the set once created.
# Sets do not contain duplicate items.

set_A = {2, 4, 2, 6}
print(set_A)

info = {"red", 19, False, 5.9, 19}
print(info)

skt = set()  # Empty Set 
print(type(skt))
 
print("\nSet Elements:")
for value in info:
    print(value) # not in an ordered way