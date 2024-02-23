class Solution(object):
    def missingNumber(self, nums):
        ans=-1
        for i in range(len(nums)+1):
            if i not in nums:
                ans=i
            if ans != -1:
                return ans
        
