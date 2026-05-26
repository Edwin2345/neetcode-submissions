class Solution:
    def hammingWeight(self, n: int) -> int:
        #use a shifitng bitmask and add to see if one
        oneCount = 0
        for i in range(32):
            if n & (1 << i):
               oneCount += 1
        return oneCount