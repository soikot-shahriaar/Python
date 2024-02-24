# union() method returns a new set whereas update() method adds item into the existing set from another set.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6}
set1.update(set2)
print(set1, set2) # {1, 2, 3, 4, 5, 6} {4, 5, 6}


# intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
set1 = {1, 4, 3}
set2 = {4, 2, 1}
print(set1.intersection(set2)) # {1, 4}
set1.intersection_update(set2)
print(set1, set2) # {1, 4} {1, 2, 4}

# this method prints only items that are not similar to both the sets.
# symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3) # {'Delhi', 'Seoul', 'Berlin', 'Kabul'}
cities.symmetric_difference_update(cities2)
print(cities) # {'Delhi', 'Kabul', 'Seoul', 'Berlin'}

# this method prints only items that are only present in the original set and not in both the sets.
# difference() method returns a new set whereas difference_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3) # {'Madrid', 'Tokyo', 'Berlin'} 
print(cities.difference(cities2)) # {'Madrid', 'Tokyo', 'Berlin'}  