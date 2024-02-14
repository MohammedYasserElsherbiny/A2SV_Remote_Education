class Solution(object):
    def finalValueAfterOperations(self, operations):
        val=0
        for op in operations:
            if op[0]=='-' or op[2]=='-':
                val-=1
            else:
                val+=1
        return val
        
