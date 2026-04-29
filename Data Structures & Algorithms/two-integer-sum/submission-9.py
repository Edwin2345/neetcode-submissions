class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenBefore = {}
        for i,n in enumerate(nums):
            if target-n in seenBefore:
                return [seenBefore[target-n],i]
            seenBefore[n] = i
        
        #not found
        return [-1,-1]