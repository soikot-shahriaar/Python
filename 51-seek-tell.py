# seek() function allows us to move the current position within a file to a specific point.
# The position is specified in bytes, and we can move either forward or backward from the current position.

# tell() function returns the current position within the file, in bytes.
# This can be useful for keeping track of our location within the file or for seeking to a specific position relative to the current position.

with open("abc.txt", "r") as f:
    print(type(f))
    # move to the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)