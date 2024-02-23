class Solution(object):
    def findWinners(self, matches):
        oneLos=[]
        win=[]
        ans=[]
        mp={}
        for match in matches:
            if match[1] not in mp:
                mp[match[1]]=0
            if match[0] not in mp:
                mp[match[0]]=0
            mp[match[1]]+=1
        
        for i in mp:
            if mp[i] == 0:
                win.append(i)
            if mp[i] == 1:
                oneLos.append(i)
        ans.append(sorted(win))
        ans.append(sorted(oneLos))
        return ans
        

        
        
        
