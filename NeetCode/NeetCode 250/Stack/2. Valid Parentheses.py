class Solution:
    def isValid(self, s: str) -> bool:
        d={ "(":")","{":"}","[":"]" }
        stak = []

        for char in s:
            if char in d:
                stak.append(char)
            else:
                if stak==[] or char!=d[stak.pop()]:
                    return False
        
        return True if stak==[] else False
    


sol=Solution()

answer = sol.isValid("[(])")
print(answer)