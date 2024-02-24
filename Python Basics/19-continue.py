for i in range(1,11):
    if i == 6 or i == 9:
        print("Skipped this Line!")
        continue
    print("5 X", i, "=", 5 * i)