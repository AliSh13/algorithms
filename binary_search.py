from decorators import find_time_for_execute as ft


@ft
def binary_search(arr, item):
    # бинарный поиск
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid
    return None

if __name__ == '__main__':

    numbers = [x for x in range(1000,10000)]
    print(numbers)
    print(binary_search(numbers, 4302))
