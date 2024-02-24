str1 = "We wish you Eid Mubarak"
print(str1.isprintable()) # returns True if all the values within the given string are printable, if not, then return False.

str1 = "         "  # using Space Bar
str2 = "  "  # using Tab Button
print(str1.isspace()) # returns True only and only if the string contains white spaces, else returns False.
print(str2.isspace())

str1 = "World Health Organization"
str2 = "To kill a Mocking bird"
print(str1.istitle()) # returns True only if the first letter of each word of the string is capitalized, else it returns False.
print(str2.istitle())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # capitalizes each letter of the word within the string.

str1 = "Python is a Interpreted Language"
print(str1.swapcase()) # changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.