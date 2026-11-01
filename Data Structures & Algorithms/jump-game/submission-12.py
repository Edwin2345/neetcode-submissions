class Solution:
    #recursive function -> memoized
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def canJumpToEnd(i):
            #reached last index
            if i == len(nums) - 1:
               return True 
            #jumped too far
            if i > len(nums) - 1:
               return False
            #already computed if possible to jump
            if i in cache:
               return cache[i] 

            #otherwise try jump values from 1 to nums[i]
            for j in range(1, nums[i] + 1):
                if canJumpToEnd(i + j):
                   cache[i] = True 
                   return cache[i]

            #unable to reach end
            cache[i] = False
            return cache[i]

        return canJumpToEnd(0)  
        