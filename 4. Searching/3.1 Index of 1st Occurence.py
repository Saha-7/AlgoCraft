#Most Efficient
def firstOccurence(arr, n, x):
    low=0 
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if(x>arr[mid]):
            low=mid+1 
        elif(x<arr[mid]):
            high=mid-1 
        else:
            if mid==0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high=mid-1
    
    return -1
        
        
        
        
    
n=5
arr=[5, 10, 10, 15, 15]
x=15
print(firstOccurence(arr, n, x))