# WRITING A FILE
# write() method to write to the file.
# but first need to open it in write mode.

f = open("untitled_file2.txt", "w")
f.write("Hello, world! I'm Soikot Shahriar.")
f.close()

with open("untitled_file.txt", "a") as f:
    f.write("Hey I am also inside there.")