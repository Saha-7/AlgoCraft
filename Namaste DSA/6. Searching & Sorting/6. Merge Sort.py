def mergeSort(arr,s,e):
    
    if e-s+1<=1:
        return arr
        
    m = (s+e)//2
    
    mergeSort(arr,s,m)
    
    mergeSort(arr,m+1,e)
    
    merge(arr,s,m,e)
    
    return arr
    
def merge(arr,s,m,e):
    left=arr[s:m+1]
    right=arr[m+1:e+1]
    
    i=0
    j=0
    new=s
    
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[new]=left[i]
            i+=1
            new+=1
        else:
            arr[new]=right[j]
            j+=1
            new+=1
            
    while i<len(left):
        arr[new]=left[i]
        i+=1
        new+=1
        
    while j<len(right):
        arr[new]=right[j]
        j+=1
        new+=1
        

arr=[3,2,4,1,6]
s=0
e=len(arr)-1
print(mergeSort(arr,s,e))


