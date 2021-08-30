

def remove_duplicates(my_list):
    """Remove duplicates from a list."""    
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    return new_list 

def remove_duplicates_set(my_list):
    """Remove duplicates from a list."""
    return set(my_list)

my_list = {1,2,3,4,5,6,2,4,6}

new_list = remove_duplicates(my_list)
new_list = remove_duplicates_set(my_list)
for e in new_list:
    print(e)
