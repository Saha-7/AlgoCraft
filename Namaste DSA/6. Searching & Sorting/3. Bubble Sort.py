arr=[10, 8, 20, 5, 13, 2]

def bubbleSort(arr):
    n=len(arr)

    for i in range(n-1):
        swapped=False
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True

    if swapped==True:
        return arr

print(bubbleSort(arr))