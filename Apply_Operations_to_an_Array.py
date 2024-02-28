class Solution(object):
    def applyOperations(self, nums):
        cnt=0
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            if nums[i]==0:
                cnt+=1
        
        if nums[len(nums)-1]==0:
            cnt+=1

        ans=[]

        for i in range(len(nums)):
            if nums[i] !=0:
                ans.append(nums[i])
        
        for i in range(cnt):
            ans.append(0)

        return ans        
        
        
