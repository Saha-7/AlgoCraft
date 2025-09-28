class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        uniq = set()
        for ele in nums:
            if ele in uniq:
                return True
            else:
                uniq.add(ele)
        return False
        