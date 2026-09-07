class Solution:
   # dynamic programming: top down
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def canJumpToEnd(index):
            #check if at end
            if index == len(nums) - 1:
               return True
            #already compute if reachable or not
            if index in cache:
               return cache[index] 
            
            #otherwise -> see if you can reach end by taking jumps
            for j in range(1, nums[index] + 1):
                newIndex = index + j
                if newIndex >= len(nums):
                   break
                if canJumpToEnd(newIndex):              
                   return True 

            #not reachable at all
            cache[index] = False
            return cache[index]

        return canJumpToEnd(0)
        