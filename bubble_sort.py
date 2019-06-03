from random import randint
from decorators import find_time_for_execute as ft

@ft
def bubble_sort(list):
    #пузырьковая сортировка
    k = len(list)-1
    for z in range(0,k):
        for x in range(0,k-z):
            if list[x] > list [x+1]:
                list[x],list[x+1] = list[x+1], list[x]

    return list



if __name__ == '__main__':

    numbers = [randint(1,20) for _ in range(1000)]
    print(numbers)
    print(bubble_sort(numbers))
