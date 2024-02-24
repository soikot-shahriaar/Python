# There are four types of arguments that we can provide in a function.

# ### Default arguments:
# We can provide a default value while creating a function.

# ### Keyword arguments:
# We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name.

# ### Required arguments:
# In case we don't pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

# ### Variable-length arguments:
# Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

def average(a, b, c=1):
    print("The average is ", (a + b + c) / 3)
average(4, 6)

def average(*numbers):
    # print(type(numbers))  # <class 'tuple'>
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
average(5, 6, 7, 1)

def name(**name):
    # print(type(name))  # <class 'dict'>
    print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Buchanan", lname="Barnes", fname="James")