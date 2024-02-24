def calculateGMean(a, b):
    gMean = (a * b) / (a + b)
    print(gMean)

def isGreater(a, b):
    if a > b:
        print("First number is Greater")
    else:
        print("Second number is Greater or Equal")

def isLesser(a, b):
    pass

a = 9
b = 8
calculateGMean(a, b)
calculateGMean(8, 7)

isGreater(34, 90)