class Solution(object):
    def convertTemperature(self, celsius):
       lst = ["" for _ in range(2)]
       lst[0]=celsius+273.15
       lst[1]=celsius*1.80+32.00
       return lst
       
        
