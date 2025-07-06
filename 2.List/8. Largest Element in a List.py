l= [1,34,7,43,78,55]

def largest(arr):
    big=arr[0]
    for ele in arr:
        if ele>big:
            big=ele
    return big

ans=largest(l)
print(ans)
