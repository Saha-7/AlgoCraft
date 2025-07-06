l= [1,34,43,55]

def Sorted(arr)->bool:
    if len(arr)<=1:
        return True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
    

ans=Sorted(l)
print(ans)