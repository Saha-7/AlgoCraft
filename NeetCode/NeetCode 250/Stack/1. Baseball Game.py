class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res =[]
        total=0
        for ele in operations:
            if ele=='+':
                res.append(res[-1] + res[-2])
            elif ele=='D':
                res.append(res[-1]*2)
            elif ele=='C':
                res.pop()
            else:
                res.append(int(ele))
   
        while len(res):
            total+=res.pop()
        return total
        

sol = Solution()
ans=sol.calPoints(["1","2","+","C","5","D"])
print(ans)