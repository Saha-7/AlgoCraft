class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size=len(nums)
        ans=[0]*2*size

        for i,ele in enumerate(nums):
            ans[i]=ele
            ans[i+size]=ele
        return ans