cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# checks if items of given set are present in another set.
print(cities.isdisjoint(cities2)) # False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2)) # False
cities3 = {"Seoul", "Madrid", "Kabul"}
# checks if all the items of a particular set are present in the original set.
print(cities.issuperset(cities3)) # False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
# checks if all the items of the original set are present in the particular set.
print(cities2.issubset(cities)) # True

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
# add a single item to the set
print(cities) # {'Tokyo', 'Delhi', 'Helsinki', 'Berlin', 'Madrid'}

# If we want to add more than one item, simply create another set or any other iterable object (list, tuple, dictionary), and use the update() method to add it into the existing set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities) # {'Warsaw', 'Berlin', 'Tokyo', 'Delhi', 'Helsinki', 'Madrid', 'Seoul'}