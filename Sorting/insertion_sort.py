def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    
    # Iterate through all elements
    for i in range(1, len(arr)):
        # Starting from the current element, place the index pointer at the position in front of the first element that is smaller than the current one
        j = i
        while j >= 0 and arr[j] >= arr[i]:
            j-=1
        j+=1

        # Move all elements from the place j to i-1 1 place in the front
        temp = arr[i]
        k = i
        while k != j:
            arr[k] = arr[k-1]
            k -= 1
        
        # Insert the current element
        arr[k] = temp

    return arr