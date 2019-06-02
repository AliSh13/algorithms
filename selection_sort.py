#from random import randint

#numbers = [randint(1,100) for i in range(1,31)]

def find_small(array):
    #находит минимальный элемент
    small = array[0]
    small_index = 0
    for i in range(1, len(array)):
        if array[i] < small:
            small = array[i]
            small_index = i
    return small_index

def selection_sort(array):
    #сортировка выбором
    new_arr = []
    for i in range(len(array)):
        small = find_small(array)
        new_arr.append(array.pop(small))
    return new_arr

#print(numbers)
#print(selection_sort(numbers))
