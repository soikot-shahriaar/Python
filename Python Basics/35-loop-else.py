for i in []:
    print(i)
else:
    print("No Item")

i = 0
while i < 3:
    print(i)
    i = i + 1
    if i == 2:
        break
else:
    print("sorry no i")

for x in range(3):
    print("iteration number {} in for loop".format(x + 1))
else:
    print("else in loop")
print("out of loop")