def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[i],arr[min_ind] = arr[min_ind],arr[i]

        

l=[10,5,8,2,-4,-2,15]
selectionSort(l)
print(l)