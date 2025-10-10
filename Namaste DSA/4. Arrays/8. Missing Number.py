
def missingNumber( nums: list[int]) -> int:

    n = len(nums)
    totalSum = n*(n+1)//2
    currentSum = 0

    for i in range(len(nums)):
        currentSum+=nums[i]
        
    return totalSum-currentSum



print(missingNumber([1,0,2,5,3]))