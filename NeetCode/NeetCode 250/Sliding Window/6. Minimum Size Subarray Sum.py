class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        length=float('inf') # +ve infinity
        total=0

        for r in range(len(nums)):
            total+=nums[r]

            while total>=target:
                length=min(length,r-l+1)
                total-=nums[l]
                l+=1
        
        if length==float('inf'):
            return 0
        else:
            return length
        

target = 10
nums = [2,1,5,1,5,3]
sol = Solution()
ans = sol.minSubArrayLen(target,nums)
print(ans)