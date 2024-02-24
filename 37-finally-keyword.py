def func1():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the Index: "))
        print("Value of Index", i, "is", l[i])
        return 1

    except:
        print("Some Error Occurred")
        return 0

    finally:
        print("I am always Executed")

print(func1())