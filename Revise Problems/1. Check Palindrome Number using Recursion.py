class Solution:
    def isPalin(self,N):
        #code here
        return self.checkpal(N,N,0)

    def checkpal(self,original,current,reverse):

        if current==0:
            if reverse==original:
                return 1
            else:
                return 0
        
        lastDigit = current%10

        reverse = reverse*10 + lastDigit

        current = current//10

        return self.checkpal(original,current, reverse)

obj = Solution()

print(obj.isPalin(1001))
print(obj.isPalin(100))
print(obj.isPalin(2010))
print(obj.isPalin(5643))





