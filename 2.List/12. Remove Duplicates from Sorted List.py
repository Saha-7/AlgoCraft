def removeDuplicates(l):
    left=1
    for i in range(1,len(l)):
        if l[i]!=l[i-1]:
            left+=1
    return left






arr=[10, 20, 20, 30, 30, 30, 30]
print(removeDuplicates(arr))