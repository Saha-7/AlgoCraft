l=[4,-1,2,-7,4,3]

def kadane(arr):
    maxSum=arr[0]
    curSum =0

    for n in arr:
        curSum = max(curSum,0)
        curSum+=n
        maxSum=max(maxSum,curSum)
    return maxSum

print(kadane(l))