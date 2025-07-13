arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]

def merge(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=j=0

    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    
    while i<m:
        res.append(a[i])
        i+=1
    while j<n:
        res.append(b[j])
        j+=1
    return res

arr=merge(arr1,arr2)
print(arr)
