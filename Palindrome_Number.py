class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return 0
        else:
            x=str(x)
            y=x[::-1]
            if x==y:
                return 1
            return 0
        
