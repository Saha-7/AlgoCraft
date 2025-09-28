from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        d = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')] +=1
            
            d[tuple(count)].append(s)
        
        return list(d.values)
