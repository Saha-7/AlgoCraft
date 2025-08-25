def merge(a, low, mid, high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]

    m=len(left)
    n=len(right)
    i=j=0 
    k=low

    while k<m and k<n:
        if left[i]<right[j]:
            a[k]=left[i]
            i+=1
            k+=1
        else:
            a[k]=right[j]
            j+=1
            k+=1
    
    while i<m:
        a[k]=left[i]
        i+=1
        k+=1

    while j<n:
        a[k]=right[j]
        j+=1
        k+=1

    


a = [10, 15, 20, 40, 8, 11, 55]

merge(a, 0, 3, 6)

print(a)