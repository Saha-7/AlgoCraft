def findlength(arr):
    length=0
    l=0

    for r in range(len(arr)):
        if arr[l]!=arr[r]:
            l=r
        length = max(r-l+1, length)
    return length




l=[4,2,2,3,3,3]

print(findlength(l))