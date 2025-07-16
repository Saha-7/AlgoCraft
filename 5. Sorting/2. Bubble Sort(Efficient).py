def bubble_Sort(arr):
    n=len(arr)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            return

value = [10,20,30,40,50]
bubble_Sort(value)
print(value)  