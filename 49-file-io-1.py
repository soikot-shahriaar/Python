# open() function to open a file. 
# It takes two arguments: the name of the file and the mode in which the file should be opened. 
# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

# READING A FILE
# read() method reads the entire contents of the file and returns it as a string.

f = open("untitled_file.txt", "r")
text = f.read()
print(text)
f.close()