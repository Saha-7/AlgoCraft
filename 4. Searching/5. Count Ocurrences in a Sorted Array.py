def lastOccurence(arr,x): 
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
            else :
                low=mid+1
    return -1


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



def countOccurr(arr,x):
    first= fastOccurence(arr,x)

    if first==-1:
        return 0
    else:
        return lastOccurence(l,x)-first+1













l = [10, 20, 20, 20, 30, 30]

print(10, countOccurr(l, 10))
print(20, countOccurr(l, 20))
print(30, countOccurr(l, 30))
print(25, countOccurr(l, 25))