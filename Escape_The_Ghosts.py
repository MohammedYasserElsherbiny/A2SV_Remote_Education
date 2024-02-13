class Solution(object):
    def escapeGhosts(self, ghosts, target):
        myDis=abs(target[0]) + abs(target[1])
        ghostsDis=10000000
        for one in ghosts :
            ghostsDis=min(ghostsDis , abs(target[0]-one[0])+abs(target[1]-one[1]))
        
        final=min(ghostsDis,myDis)

        if final == myDis and myDis!=ghostsDis:
            return True
        return False
        
