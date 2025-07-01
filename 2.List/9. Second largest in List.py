l= [1,34,7,43,78,55]

def Secondlargest(arr):
    large=l[0]
    seclarge=None
    if len(arr)<=1:
        return None
    for ele in arr[1:]:
        if ele>large:
            large=ele
            seclarge=large
        else:
            if seclarge!=None or ele>seclarge:
                seclarge=ele
    return seclarge

ans=Secondlargest(l)
print(ans)