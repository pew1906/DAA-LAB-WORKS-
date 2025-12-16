# Assignment 05: Performance Comparison of Sequential and Parallel Merge Sort
import multiprocessing
import time
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
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def sequential_mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = sequential_mergesort(arr[:mid])
    right = sequential_mergesort(arr[mid:])
    return merge(left, right)

def parallel_mergesort(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) < 50000: 
        return sequential_mergesort(arr)

    mid = len(arr) // 2
    with multiprocessing.Pool(processes=2) as pool:
        left, right = pool.map(sequential_mergesort, [arr[:mid], arr[mid:]])
    return merge(left, right)

if __name__ == "__main__":
    import random

    N = 200000
    arr = [random.randint(0, 1000000) for _ in range(N)]

    start = time.time()
    seq_sorted = sequential_mergesort(arr)
    end = time.time()
    print("Sequential MergeSort Time:", round(end - start, 4), "seconds")

    start = time.time()
    par_sorted = parallel_mergesort(arr)
    end = time.time()
    print("Parallel MergeSort Time:", round(end - start, 4), "seconds")

    print("Sorting Correct?", seq_sorted == par_sorted)
