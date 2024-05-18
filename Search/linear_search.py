def linear_search(arr, k):
    for i, item in enumerate(arr):
        if item == k:
            return i
    return -1