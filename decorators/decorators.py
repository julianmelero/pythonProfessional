from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        total_seconds = (end - start).total_seconds()
        print("Time:" + str(total_seconds))
    return wrapper


@execution_time
def sum(a, b):
    return a + b

@execution_time
def exec():
    print('Executing function...')
    for i in range(100000000):
        pass


exec()
sum(150000,5)


