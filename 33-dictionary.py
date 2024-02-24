# ## Python Dictionaries
# Dictionaries are ordered collection of data items. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brackets {}.

info = {"name": "Rahim", "age": 21, "eligible": True}

print(info)
print(info.keys())
print(info.values())
print(info.items())
print("\n")

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")
print("\n")

for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")