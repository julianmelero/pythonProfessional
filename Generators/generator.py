def my_gen():
    """Generator Example"""
    n = 1    
    yield n
    n = 2
    yield n
    n = 3
    yield n



gen = my_gen()
try:
    while True:
        print(next(gen))
except StopIteration:
    print("StopIteration")


# Generator Expression
gen = (x ** 2 for x in range(1, 11))    # Generator Expression
for e in gen:
    print(e)