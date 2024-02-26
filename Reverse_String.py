class Solution(object):
    def reverseString(self, s):
        for i in range(len(s)//2):
            lastIdx=len(s)-i-1

            temp=s[lastIdx]
            s[lastIdx]=s[i]
            s[i]=temp
        return s

        
