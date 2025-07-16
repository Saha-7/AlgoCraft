def bubble_Sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    

value = [2,10,7,8,1]
bubble_Sort(value)
print(value)  