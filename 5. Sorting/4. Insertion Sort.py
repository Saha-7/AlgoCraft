l=[10,5,8,2,-4,-2,15]

def insertion_sort(arr):
    for i in range(len(arr)):
        j=i-1
        while j>=0 and arr[j+1]<arr[j]:
            temp = arr[j+1]
            arr[j+1] =arr[j]
            arr[j] =temp
            j-=1

insertion_sort(l)
print(l)
