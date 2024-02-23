class Solution(object):
    def plusOne(self, digits):
        num=0
        for i in range(len(digits)):
            num*=10
            num+=int(digits[i])
        
        num+=1
        ans=[]

        while num:
            ans.append(num%10)
            num/=10
        
        ans.reverse()
        return ans
            
        
        
