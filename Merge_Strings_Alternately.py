class Solution(object):
    def mergeAlternately(self, word1, word2):
        i1=0
        i2=0
        turn=1
        res=""
        for i in range (len(word1)+len(word2)):
            if turn %2== 1 and i1<len(word1):
                res+=word1[i1]
                i1+=1
            elif i2<len(word2):
                res+=word2[i2]
                i2+=1
            else:
                res+=word1[i1]
                i1+=1
            turn+=1
        return res
        
