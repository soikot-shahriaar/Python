# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

questions = [
    [
        "What is the capital city of Bangladesh?",
        "Delhi",
        "Moscow",
        "Dhaka",
        "Khulna",
        3,
    ],
    [
        "What is the official language of Bangladesh?",
        "Arabic",
        "Bengali",
        "Urdu",
        "Hindi",
        2,
    ],
    [
        "What is the national animal of Bangladesh.",
        "Tiger",
        "Lion",
        "Bear",
        "Dolphin",
        1,
    ],
    ["What currency is used in Bangladesh?", "Taka", "USD", "Won", "Dinar", 1],
    [
        "What two countries border Bangladesh?",
        "China and Sri Lanka",
        "Nepal and Bhutan",
        "India and Myanmar",
        "Pakistan and Tibet",
        3,
    ],
    [
        "What body of water borders Bangladesh to the south?",
        "Gulf of Mexico",
        "Bay of Fundy",
        "Bay of Bengal",
        "Dead Sea",
        3,
    ],
    [
        "What flower is featured on the national emblem of Bangladesh?",
        "Water lily",
        "Tulip",
        "Sunflower",
        "Rose",
        1,
    ],
]

levels = [1000, 50000, 100000, 500000, 1000000, 5000000, 10000000]

money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Tk. {levels[i]}:")
    print(f"{question[0]}")
    print(f"1. {question[1]}          2. {question[2]} ")
    print(f"3. {question[3]}          4. {question[4]} ")
    reply = int(input("Enter your Answer (1-4) or 0 to quit: "))
    if reply == 0:
        money = levels[i - 1] 
        break
    if reply == question[-1]:
        print(f"Correct Answer ! you have won Tk. {levels[i]}")
        if i == 3:
            money = 100000
        elif i == 9:
            money = 1000000
        elif i == 14:
            money = 10000000
    else:
        print("Wrong Answer!")
        break

print(f"Your take home Money is {money}")