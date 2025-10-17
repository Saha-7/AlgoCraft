arr=[10, 8, 20, 5, 13, 2]

def selection_Sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index]>arr[j]:
                min_index=j

        arr[min_index], arr[i] = arr[i], arr[min_index]
    


    

selection_Sort(arr)

print(arr)