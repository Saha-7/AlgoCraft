class Solution:
    def findMin(self, nums: list[int]) -> int:
        left=0
        right=len(nums)-1

        while left<right:
            mid=(left+right)//2

            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        
        return nums[left]

            

sol=Solution()
ans=sol.findMin([3,4,5,6,1,2])

print(ans)