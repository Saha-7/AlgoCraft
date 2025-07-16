## Naive Approach
# def squareT(x):
#     i=1
#     while i*i<=x:
#         i+=1
#     return i-1


def squareT(x):
    left=0
    right=x
    answer=0

    while left<=right:
        mid = (left+right)//2
        if mid**2==x:
            return mid
        elif mid*mid<x:
            left=mid+1
            answer=mid
        else:
            right=mid-1
    return answer

    



value = int(input('Enter number: '))
ans=squareT(value)
print(ans)  