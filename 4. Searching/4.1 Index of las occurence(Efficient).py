


def lastOccurence(arr,n,x): 
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2

        if x<arr[mid]:
            high=mid-1
        elif x>arr[mid]:
            low=mid+1
        else:
            if mid==len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low=mid+1
    return -1
        
        
    
n=5
arr=[5, 10, 10, 15, 15]
x=15
print(lastOccurence(arr, n, x))
