class Solution(object):
    def arrayChange(self, nums, operations):
        mp1={}
        mp2={}
        #print(len(nums),len(operations))
        for i in range(len(nums)):
            mp1[i]=nums[i]
            mp2[nums[i]]=i
            #print(str(i)+"->"+str(mp1[i]))
            #print(str(mp2[nums[i]])+"<-"+str(nums[i]))

        #mp1[mp2[operations[i][0]]]=operations[i][1] operations
        
        for i in range(len(operations)):
            #print("form "+str(operations[i][0])+" that is at index "+str(mp2[operations[i][0]])+" to "+str(operations[i][1]))
            mp1[mp2[operations[i][0]]]=operations[i][1]
            mp2[operations[i][1]]=mp2[operations[i][0]]
            #print(i)

        lis=[]

        for i in range(len(nums)):
            lis.append(mp1[i])
        
        #print(lis)
        return lis
        
