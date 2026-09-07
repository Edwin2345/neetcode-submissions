class Solution:
    #Top Down DP approach: O(N^2) as need to check up to n-1 indices for idnex 1
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def calcMinJumpsToTop(index):
            #already at top
            if index == len(nums) - 1:
               return 0
            #computed min jumps at this index already
            if index in cache:
               return cache[index]

            #otherwise, try 1 jump of lengths 1 to nums[i]
            minNumJumps = float("inf")
            maxReachableIndex = min(len(nums) - 1, index + nums[index])

            for newIndex in range(index + 1, maxReachableIndex + 1):
                minNumJumps = min(minNumJumps, 1 + calcMinJumpsToTop(newIndex))

            cache[index] = minNumJumps
            return cache[index]
        
        return calcMinJumpsToTop(0)
        