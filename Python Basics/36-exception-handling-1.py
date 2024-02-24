# try...except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

# a = int(input("Enter the Number: "))
# print(f"Multiplication table of {a} is: ")
# for i in range(1, 11):
#     print(f"{a} X {i} = {a*i}")

# try...except

a = input("Enter the Number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid Input!")
print("End of Program!")