class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(word):
            start, end = 0, len(word) - 1
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return isPal(s[left + 1:right + 1]) or isPal(s[left:right])
            left += 1
            right -= 1

        return True


s="abca"
solObj = Solution()
print(solObj.validPalindrome(s))
