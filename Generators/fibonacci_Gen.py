import time

def FiboGen(max):
    """Generator that yields numbers in the Fibonacci sequence."""
    a, b = 0, 1
    while b < max:
        yield b
        a, b = b, a + b


fibo = FiboGen(15000)

for e in fibo:
    print(e)
    time.sleep(0.4)


