#Q: Zero Indexed or 1 Indexed?
#P: exatcly 1 solution
#P: return smaller index first
#Q: unqiue values?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndexMap = {}

        for i,n in enumerate(nums):
            #check if solution found
            if (target-n) in numToIndexMap:
               return [numToIndexMap[target-n], i] 
               
            #add to map if not there
            if n not in numToIndexMap:
               numToIndexMap[n] = i

        #no solution found
        return [-1,-1] 