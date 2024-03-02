class Solution(object):
    def minPairSum(self, nums):
        nums=sorted(nums)

        mx=0
        for i in range(len(nums)/2):
            mx=max(mx,nums[i]+nums[len(nums)-i-1])
        return mx
