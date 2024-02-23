class Solution(object):
    def minDeletionSize(self, strs):
        cols, rows = len(strs[0]),len(strs)
        arr = [[0] * rows for _ in range(cols)]  
        for i in range(rows):
            for j in range(cols):
                arr[j][i]=strs[i][j]
        
        ans=0

        for i in arr:
            if i != sorted(i):
                ans += 1
        
        return ans
        
