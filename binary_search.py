from random import randint

numbers = [x for x in range(1,100000)]
print(numbers)

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

print(binary_search(numbers, 5))
