arr=[10, 8, 20, 5, 13, 2]

def insertion_Sort(arr):
    for i in range(len(arr)):
        j=i-1

        while j>=0 and arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j-=1
    return arr
    
    


    

insertion_Sort(arr)

print(arr)