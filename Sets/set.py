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

