from random import randint
from decorators import find_time_for_execute as ft


@ft
def quick_sort(array):
    #быстрая сортировка
    if array == []:
        return array
    else:
        choice = array[len(array)//2 ]
        less = [i for i in array if i < choice]
        #если элементы сортируемого списка не уникальны
        mid = [i for i in array if i == choice]
        greater =  [i for i in array if i > choice]
        return quick_sort(less)  + mid + quick_sort(greater)

if __name__ == '__main__':

    numbers = [randint(1,11) for i in range(500000)]
    print(numbers)
    print(quick_sort(numbers))
