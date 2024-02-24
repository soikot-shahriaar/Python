myList = [3, 5, 6, "skt", True, 6]

print(myList)
print(type(myList))
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])
print(myList[4])
print(myList[5])
# print(marks[6]) #IndexError

# Negative index to positive index
print(myList[-3])  # Negative index
print(myList[len(myList) - 3])  # Positive index
print(myList[6 - 3])  # Positive index
print(myList[3])  # Positive index

if "6" in myList:
    print("Yes")
else:
    print("No")

# Same thing applies for strings as well!
if "iar" in "shahriar":
    print("Yes")