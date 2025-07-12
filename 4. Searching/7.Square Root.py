## Naive Approach
# def squareT(x):
#     i=1
#     while i*i<=x:
#         i+=1
#     return i-1


def squareT(x):
    l=0
    r=x
    res=0
    while l<=r:
        m= (l+r)//2
        if m**2>x:
            r=m-1
        elif m**2<x:
            l=m+1
            res=m
        else:
            return m
    



value = int(input('Enter number: '))
ans=squareT(value)
print(ans)  