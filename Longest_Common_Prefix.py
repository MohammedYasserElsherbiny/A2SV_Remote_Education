class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        else:
            s1=max(strs)
            s2=min(strs)
            i=0
            matching=0
            while i<len(s2) and s1[i]==s2[i]:
                i+=1
                matching+=1
            return s1[0:matching]
        
