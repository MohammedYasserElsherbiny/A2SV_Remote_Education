class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        w1=""
        w2=""

        for s in word1:
            w1+=s
        for s in word2:
            w2+=s
        return w1==w2
        
