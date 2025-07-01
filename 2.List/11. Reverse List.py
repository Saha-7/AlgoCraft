l= [1,34,43,55]


def Reverse(arr):
    left=0
    right=len(arr)-1

    if left<right:
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
        right-=1
    return arr

ans=Reverse(l)
print(ans)