from random import randint
from decorators import find_time_for_execute as ft

@ft
def merge_sort(list):
    n = len(list)
    if n < 2:
        return list

    left = merge_sort(list[:n//2])
    right = merge_sort(list[n//2:n])

    i = j = 0
    res =[]
    while i < len(left) or j < len(right):
        if not i < len(left):
            res.append(right[j])
            j += 1
        elif not j < len(right):
            res.append(left[i])
            i += 1
        elif left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    return res


if __name__ == '__main__':

    numbers = [randint(1,11) for _ in range(500000)]

    print(numbers)
    print(f'Количество сортируемых элементов - {len(numbers)}')
    print(merge_sort(numbers))
