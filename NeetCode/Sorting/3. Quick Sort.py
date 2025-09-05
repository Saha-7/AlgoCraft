def quickSort(arr, s, e):
    if e-s+1<=1:
        return arr
    
    pivot = arr[e]
    left = s # pointer for left side

    # Partition
    for i in range(s,e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left+=1
    
    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # quick sor left side
    quickSort(arr, s, left-1)

    # quick sort right side
    quickSort(arr, left+1, e)


    return arr










arr = [0, 15, 20, 40, 8, 11, 55, 24, 45, 100]

s=0
e=len(arr)-1

ans=quickSort(arr, s, e)
print(ans)