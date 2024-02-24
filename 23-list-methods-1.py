myList = [11, 45, 1, 2, 4, 6, 1, 1]
print(myList)

myList.append(7)  # appends items to the end of the existing list.
print(myList) # [11, 45, 1, 2, 4, 6, 1, 1, 7]

myList.sort()  # sorts the list in ascending order.
print(myList) # [1, 1, 1, 2, 4, 6, 7, 11, 45]

myList.sort(reverse=True)  # sorts the list in descending order.
print(myList) # [45, 11, 7, 6, 4, 2, 1, 1, 1]

myList.reverse()  # reverses the order of the list.
print(myList) # [1, 1, 1, 2, 4, 6, 7, 11, 45]

print(myList.index(11))  # returns the index of the first occurrence of the list item.
print(myList.count(1))  # returns the count of the number of items with the given value.