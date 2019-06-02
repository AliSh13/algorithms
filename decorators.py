from datetime import datetime
from functools import wraps

def find_time_for_execute(func):
    #декоратор проверки времени выполнянения
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        my_func = func(*args, **kwargs)
        end = datetime.now()
        print(f'Время выполнения функции {func.__name__} составило : {end - start} c')
        return my_func
    return wrapper
