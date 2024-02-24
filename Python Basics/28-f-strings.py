letter = "Hey my name is {} and I am from {}"
name = "Shahriar"
country = "Bangladesh"
print(letter.format(name, country))

letter = "Hey my name is {1} and I am from {0}"
country = "Bangladesh"
name = "Shahriar"
print(letter.format(country, name))

# f-strings
country = "Bangladesh"
name = "Soikot"
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999999
print(f"For only {price:.2f} dollars!")