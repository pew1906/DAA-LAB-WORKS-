# Assignment 01: Compare Merge Sort and Quick Sort
import random
import timeit

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

size = 10000
data = [random.randint(1, 100000) for _ in range(size)]

merge_time = timeit.timeit(stmt="merge_sort(data.copy())",
                           globals=globals(), number=1)
quick_time = timeit.timeit(stmt="quick_sort(data.copy())",
                           globals=globals(), number=1)

print(f"Merge Sort Time: {merge_time:.4f} seconds")
print(f"Quick Sort Time: {quick_time:.4f} seconds")
