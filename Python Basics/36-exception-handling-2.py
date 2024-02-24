try:
    nums = int(input("Enter an Integer Index: "))
    a = [6, 3]
    print(a[nums])

except ValueError:
    print("Entered number is not an Integer.")

except IndexError:
    print("Index Error")