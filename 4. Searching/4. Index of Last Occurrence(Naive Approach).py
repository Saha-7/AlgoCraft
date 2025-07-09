# Least Efficient
## Time Complexity -> O(n)
def lastOccurence(arr,n, x):  ## Naive Approach
    for i in reversed(range(len(arr))):
        if arr[i]==x:
            return i
    return -1


   
n=5
arr=[5, 10, 10, 15, 15]
x=15
print(lastOccurence(arr, n, x))

