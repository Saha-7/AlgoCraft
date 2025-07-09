def search(l,x):
    low=0
    high=len(l)-1

    while low<=high:
        mid=(low+high)//2

        if l[mid]==x:
            return mid
        elif x<l[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1


print(search([10,20,30,45,67],89))
print(search([10,20,30,45,67],20))
