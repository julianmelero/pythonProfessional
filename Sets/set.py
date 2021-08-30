""""Set is an inmutable sctructure data"""


my_set = {1, "Hello", (1, 2, 3), True}

print(my_set)


my_list = (4,5,6,7,8)

# Create Set

my_set = set(my_list)
print(my_set)

# Add set

my_set.add(my_list)
print(my_set)

# Add update

my_set.update(my_list)
print(my_set)

# Remove
my_set.remove(my_list)
print(my_set)

#Discard
# Delete element (exist and not exist)
my_set.discard(my_list)
print(my_set)

# .pop() --> delete random element
# .clear() --> delete all elements


# .union() --> return a new set with elements from both sets
# .intersection() --> return a new set with elements common to both sets
# .difference() --> return a new set with elements in the first set not in the second   
my_set = {1, "Hello", (1, 2, 3), True}
my_list = {4,5,6,7,8}
my_set2 = my_set.union(my_list)
my_set3 = my_set | my_list
my_set4 = my_set & my_list
my_set5 = my_set - my_list
my_set6 = my_set ^ my_list
print(my_set3)
print(my_set4)
print(my_set5)
print(my_set6)
