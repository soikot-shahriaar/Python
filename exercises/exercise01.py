# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime


import time

currentTime = time.strftime("%H:%M:%S")
print("Time is Now:", currentTime)

greetingTime = int(time.strftime("%H"))

if 6 <= greetingTime < 11:
    print("Good Morning")
if 11 <= greetingTime < 16:
    print("Good Noon")
elif 16 <= greetingTime < 18:
    print("Good Afternoon")
elif 18 <= greetingTime < 20:
    print("Good Evening")
elif 20 <= greetingTime < 24 or 0 <= greetingTime < 6:
    print("Good Night")