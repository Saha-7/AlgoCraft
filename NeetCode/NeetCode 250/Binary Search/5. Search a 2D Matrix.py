class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1
        while top<=bot:
            row=(top+bot)//2
            if target<matrix[row][0]:
                bot=row-1
            elif target>matrix[row][-1]:
                top=row+1
            else:
                break
        
        if not (top<=bot):
            return False
        
        l,r=0,COLS-1
        while l<=r:
            mid=(l+r)//2
            if target==matrix[row][mid]:
                return True
            elif target>matrix[row][mid]:
                l=mid+1
            else:
                r=mid-1
        return False 
    


sol=Solution()
ans=sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
print(ans)