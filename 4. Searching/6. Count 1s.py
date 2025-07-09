
def fastOccurence(arr,x): 
    low=0
    high=len(arr)-1

    while low<=high:
        mid=(low+high)//2
        if x<arr[mid]:
            high=mid-1
        elif x>arr[mid]:
            low=mid+1
        else:
            if mid==0 or arr[mid]!=arr[mid-1]:
                return mid
            else :
                high=mid-1
    return -1


def count(arr):
    first=fastOccurence(arr,1)

    if first==-1:
        return 0
    
    else:
        return len(arr)-first
    




arr = [0, 0, 0, 1, 1, 1, 1]
print(count(arr))  



