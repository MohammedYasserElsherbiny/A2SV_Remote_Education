class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        mx=-1
        tempLen=0
        for num in nums:
            if num == 1:
                tempLen+=1
            else :
                if tempLen>mx:
                    mx=tempLen
                tempLen=0
        
        if tempLen > mx:
            mx=tempLen
        return mx
        
