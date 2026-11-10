#Q: Zero Indexed or 1 Indexed?
#P: exatcly 1 solution
#P: return smaller index first
#Q: unqiue values?

class Solution:
    #O(N) TC, O(N) SC for map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i,n in enumerate(nums):
            if target - n in numMap:
               return [numMap[target - n], i]
            else:
               numMap[n] = i 

        #should never be reached
        return [-1,-1]