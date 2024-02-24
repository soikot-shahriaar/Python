a = "!!!Soikot!!! !!!!!!!!! Shahriar"
str1 = "Welcome to the Console!!!"
print(str1.center(60)) # aligns the string to the center as per the parameters given by the user.
print(str1.center(60, "-")) 

print(a.count("!")) # counts the number of times the given value has occurred within the given string.

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python")) # checks if the string starts with a given value. If yes then return True, else return False.

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) # checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "His name is Thomas. He is an good person."
print(str1.find("name")) # searches strings
print(str1.index(".")) # searches the index 

str1 = "WelcomeToTheConsole"
print(str1.isalnum()) # returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "Welcome001"
print(str1.isalpha()) # returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "hello world" 
print(str1.islower()) # returns True if all the characters in the string are lower case, else it returns False. 