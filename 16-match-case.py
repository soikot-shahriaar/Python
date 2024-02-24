x = int(input("Enter the value of x: "))

match x:  # x is the variable to match
    case 0:  # if x is 0
        print("x is zero")
    case 4:
        print("case is 4")
        
    # case with if-condition
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 100:
        print(x, "is greater than 100")
    case _:
        print(x)