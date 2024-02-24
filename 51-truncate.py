# truncate() function
# When we open a file in Python using the open function, we can specify the mode in which we want to open the file. If we specify the mode as 'w' or 'a', the file is opened in write mode and we can write to the file. However, if we want to truncate the file to a specific size, we can use the truncate function.

with open("sample.txt", "w") as f:
    f.write("Hello World3!")
    f.truncate(3)

with open("sample.txt", "r") as f:
    print(f.read())