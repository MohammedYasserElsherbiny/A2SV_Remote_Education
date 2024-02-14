class Solution(object):
    def defangIPaddr(self, address):
        a = address.replace('.','[.]')
        return a
        
