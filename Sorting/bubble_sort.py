def bubble_sort(arr):
    if len(arr) == 1:
        return arr
    
    # At the end of the array you place largest elements, and it grows in each iteration, until the whole array is that
    for i in range(len(arr)-1, -1, -1):
        # Start from the beginning of the array and swap elements until the end
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
        
    return arr