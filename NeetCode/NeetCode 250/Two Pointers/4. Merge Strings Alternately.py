class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        word=[]
        i = j = 0
        while i<m or j<n:
            if i<m:
                word.append(word1[i])
            if j<n:
                word.append(word2[j])
            i+=1
            j+=1
        
        return "".join(word)

        
newObj = Solution()
w1="tfujui"
w2="xxxxxxxxxx"
print(newObj.mergeAlternately(w1,w2))