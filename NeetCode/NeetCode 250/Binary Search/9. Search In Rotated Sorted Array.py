class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # Find pivot (minimum element)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        left, right = 0, len(nums) - 1
        
        # Determine search range
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot  # Search right part
        else:
            right = pivot - 1  # Search left part
        
        # Binary search
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    

sol=Solution()
ans=sol.search([3,4,5,6,1,2], 1)

print(ans)