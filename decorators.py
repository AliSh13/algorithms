from datetime import datetime
from functools import wraps

def find_time_for_execute(func):
    #декоратор проверки времени выполнянения
    is_evaluating = False
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal is_evaluating
        if is_evaluating:
            return func(*args, **kwargs)
        else:
            start = datetime.now()
            is_evaluating = True
            try:
                my_func = func(*args, **kwargs)
            finally:
                 is_evaluating = False
            end = datetime.now()

            print(f'Время выполнения функции {func.__name__} составило : {end - start} c')
            return my_func
    return wrapper
