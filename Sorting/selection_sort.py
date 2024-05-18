def selection_sort(arr):
    if len(arr) == 1:
        return arr
    
    # Keep the left portion of the array sorted - in the beginning its only 1 element
    for sorted_end in range(len(arr)-1):
        # In the rest of the array find the smallest number and place it at position sorted_end
        min_idx = sorted_end
        for i in range(sorted_end + 1, len(arr)):
            if arr[i] < arr[min_idx]:
                min_idx = i
                
        # Exchange values - smallest goes to the front, and the one from the front is pushed back
        arr[sorted_end], arr[min_idx] =  arr[min_idx], arr[sorted_end]

    return arr