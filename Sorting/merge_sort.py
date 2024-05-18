def merge_sort(arr: list):
    if len(arr) > 1:
        N = len(arr)//2

        left = arr[0:N] # creates a new list -> not references
        right = arr[N:]

        merge_sort(left)
        merge_sort(right)

        i,j,k = 0,0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        if i < len(left):
            while k < len(arr):
                arr[k] = left[i]
                k += 1
                i += 1
        elif j < len(right):
            while k < len(arr):
                arr[k] = right[j]
                k += 1
                j += 1