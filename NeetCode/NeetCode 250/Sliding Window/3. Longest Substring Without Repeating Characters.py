class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        length=0
        charset=set()

        for right in range(len(s)):

            while s[right] in charset:
                charset.remove(s[left])
                left+=1

            tempWindowlength = right-left+1
            length = max(length, tempWindowlength)
            charset.add(s[right])

        return length