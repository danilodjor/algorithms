def binary_search(arr, k):
    left_idx = 0
    right_idx = len(arr)-1

    while left_idx <= right_idx:
        mid_idx = left_idx + (right_idx - left_idx)//2
        
        # Cut the array in half from the side where the element surely is not present
        if arr[mid_idx] < k:
            left_idx = mid_idx + 1
        elif arr[mid_idx] > k:
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1