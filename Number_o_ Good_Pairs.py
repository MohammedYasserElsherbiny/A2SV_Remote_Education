class Solution(object):
    def numIdenticalPairs(self, nums):
        cnt=0
        lenght=len(nums)
        for i in range(lenght):
            for j in range(lenght):
                if i == j:
                    continue
                if nums[i] == nums[j]:
                    cnt+=1
        return cnt/2
        
