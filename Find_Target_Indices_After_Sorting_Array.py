class Solution(object):
    def targetIndices(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            
        
        ans=[]
        for i in range(len(nums)):
            if nums[i]==target:
                ans.append(i)
        return ans
        
