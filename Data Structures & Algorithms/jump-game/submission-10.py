class Solution:
    #1dp dp top down
    def canJump(self, nums: List[int]) -> bool:

        cache = {}
        def canReachEnd(index):
            #at last index -> return true
            if index == len(nums) - 1:
               return True
            #already checked if reahable
            if index in cache:
               return cache[index] 

            #otherwise check if reachable if you make a jump of size 1 to size nums[index]: 
            maxReachableIndex = min(len(nums) - 1, index + nums[index])
            for newIndex in range(index + 1, maxReachableIndex + 1):
                if canReachEnd(newIndex):
                   return True
            
            #else, we can't jum pto end at this end
            cache[index] = False
            return cache[index]

        return canReachEnd(0)
        