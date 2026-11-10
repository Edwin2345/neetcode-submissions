#Q: Zero Indexed or 1 Indexed?
#P: exatcly 1 solution
#P: return smaller index first
#Q: unqiue values?

class Solution:
    #O(N^2) TC, O(1) SC
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                   return [i,j]

        #should never be reached
        return [-1,-1]