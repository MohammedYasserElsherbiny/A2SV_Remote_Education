class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        s+=' '

        for i in range(len(t)):
            if t[i] != s[i]:
                return t[i]
        
