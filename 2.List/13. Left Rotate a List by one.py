l=[1,2,3,4,5,6,7]

def leftRotate(arr):
    firstElement=arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1]=firstElement

    return arr

print(leftRotate(l))