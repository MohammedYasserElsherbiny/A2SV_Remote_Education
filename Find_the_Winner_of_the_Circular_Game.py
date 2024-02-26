class Solution(object):
    def findTheWinner(self, n, k):
        
        lis=[]
        for j in range(n):
            lis.append(j+1)

        i=0
        sz=n
        # 5  i=8  sz=1
        # 
        while True:
            if sz == 1:
                return lis[0]
            
            i=(i+k-1)%sz
            lis.pop(i)
            sz-=1

        


        
