import random
from time import perf_counter


def generate_array(size):
    arr = []
    for i in range(size):
        arr.append(i)

    return shuffle(arr)


def shuffle(arr):
    for i in range(len(arr)):
        rand_index = random.randint(0, len(arr) - 1)
        arr[i], arr[rand_index] = arr[rand_index], arr[i]

    return arr


def time_testing():

    arr = generate_array(1000000)

    start = perf_counter()
    # Call the function you want to test here.
    sorted = merge_sort(arr)

    end = perf_counter()
    print(f"Time: {end - start}")


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


time_testing()
