class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n=len(temp)
        result=[0]*n
        stak =[]

        for current_i,current_t in enumerate(temp):
            while stak and stak[-1][1] < current_t:
                old_index, old_temp = stak.pop()
                result[old_index] = current_i - old_index
            
            stak.append((current_i, current_t))
        
        return result
